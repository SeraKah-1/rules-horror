#!/usr/bin/env python3
"""Local campaign journal, deterministic rolls and structural validation."""
import argparse, hashlib, json, os, pathlib, sys, tempfile, zipfile

FILES = ('CANON.md', 'STATE.json', 'EVENTS.jsonl')
MAPS = ('player','actors','locations','items','pending','established','knowledge','perception','devices','preferences')

def require(ok, msg):
    if not ok: raise ValueError(msg)

def packed(o):
    return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')

def sha(b): return hashlib.sha256(b).hexdigest()
def read_json(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
def atomic(p, b):
    p = pathlib.Path(p)
    fd, name = tempfile.mkstemp(dir=p.parent, prefix='.save-')
    try:
        with os.fdopen(fd,'wb') as f:
            f.write(b); f.flush(); os.fsync(f.fileno())
        os.replace(name,p)
    finally:
        if os.path.exists(name): os.unlink(name)

def state_check(s, old=None):
    require(isinstance(s,dict),'state must be an object')
    for k in ('revision','world_time'):
        require(type(s.get(k)) is int and s[k]>=0, f'invalid {k}')
    for k in ('campaign_id','seed'):
        require(isinstance(s.get(k),str) and bool(s[k].strip()),f'invalid {k}')
    for k in MAPS: require(isinstance(s.get(k),dict),f'invalid {k}')
    for a in [s['player'],*s['actors'].values()]:
        require(isinstance(a,dict),'invalid actor')
        loc=a.get('location')
        require(loc is None or (isinstance(loc,str) and loc in s['locations']),'invalid actor location')
    if old is not None:
        require(s['revision']==old['revision']+1,'revision must increment')
        require(s['campaign_id']==old['campaign_id'] and s['seed']==old['seed'],'campaign or seed changed')
        require(s['world_time']>=old['world_time'],'world time moved backward')
        for k,v in old['established'].items():
            require(k in s['established'] and s['established'][k]==v,'established fact changed')
        for k,v in old['pending'].items():
            if isinstance(v,dict) and v.get('status') in ('resolved','cancelled'):
                require(s['pending'].get(k)==v,'closed pending event changed')

def event_check(e):
    require(isinstance(e,dict),'event must be an object')
    require(isinstance(e.get('action'),str) and bool(e['action'].strip()),'missing action')
    for k in ('causes','rolls'): require(isinstance(e.get(k),list),f'invalid {k}')
    for k in ('outcome','perceived'): require(k in e and isinstance(e[k],(str,dict,list)),f'invalid {k}')

def make_record(s,e,canon,prev):
    event_check(e)
    r={'revision':s['revision'],'event':e,'state':s,'canon_sha256':canon,'prev_sha256':prev}
    r['sha256']=sha(packed(r)); return r

def load(d, check_cache=True):
    d=pathlib.Path(d); c=sha((d/FILES[0]).read_bytes()); raw=(d/FILES[2]).read_bytes()
    require(raw.endswith(b'\n'),'incomplete journal')
    old=None; prev=None; last=None
    for i,line in enumerate(raw.splitlines()):
        r=json.loads(line); require(isinstance(r,dict),'invalid journal record')
        require(r.get('sha256')==sha(packed({k:v for k,v in r.items() if k!='sha256'})),'record hash mismatch')
        require(r.get('prev_sha256')==prev and r.get('canon_sha256')==c,'chain or canon mismatch')
        require(r.get('revision')==i,'journal revision mismatch')
        event_check(r['event']); state_check(r['state'],old)
        require(r['state']['revision']==i,'state revision mismatch')
        old=r['state']; prev=r['sha256']; last=r
    require(last is not None,'empty journal')
    if check_cache: require(read_json(d/FILES[1])==old,'state cache differs; recover from journal')
    return d,c,raw,last

def cache(d,s): atomic(d/FILES[1],packed(s)+b'\n')
def status(s): return {'ok':True,'campaign_id':s['campaign_id'],'revision':s['revision']}

def cmd_init(a):
    d=pathlib.Path(a.directory); c=pathlib.Path(a.canon).read_bytes(); s=read_json(a.state)
    require(bool(c.strip()),'empty canon'); state_check(s); require(s['revision']==0,'initial revision must be zero')
    d.mkdir(parents=True,exist_ok=True)
    require(not any((d/f).exists() for f in FILES),'campaign files already exist')
    e={'action':'initialize','causes':[],'outcome':'initial state established','perceived':'','rolls':[]}
    r=make_record(s,e,sha(c),None)
    atomic(d/FILES[0],c); atomic(d/FILES[2],packed(r)+b'\n'); cache(d,s)
    load(d); return status(s)

def cmd_commit(a):
    d,c,raw,last=load(a.directory); old=last['state']; require(old['revision']==a.expected,'stale revision')
    s=read_json(a.state); e=read_json(a.event); state_check(s,old)
    r=make_record(s,e,c,last['sha256']); atomic(d/FILES[2],raw+packed(r)+b'\n'); cache(d,s)
    load(d); return status(s)

def cmd_audit(a): return status(load(a.directory)[3]['state'])
def cmd_recover(a):
    d,_,_,last=load(a.directory,False); cache(d,last['state']); return cmd_audit(a)

def cmd_roll(a):
    s=load(a.directory)[3]['state']; require(s['revision']==a.expected,'stale revision')
    require(0<=a.probability<=1,'probability out of range'); require(bool(a.key.strip()),'empty roll key')
    h=hashlib.sha256(packed([s['seed'],s['campaign_id'],a.expected,a.key])).digest()
    u=int.from_bytes(h[:8],'big')/2**64
    return {'revision':a.expected,'key':a.key,'probability':a.probability,'value':u,'success':a.probability==1 or u<a.probability}

def cmd_export(a):
    d,_,_,last=load(a.directory); dest=pathlib.Path(a.output); require(not dest.exists(),'backup already exists')
    dest.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED) as z:
        for f in FILES: z.write(d/f,f)
    with zipfile.ZipFile(dest) as z: require(z.testzip() is None and set(z.namelist())==set(FILES),'backup verification failed')
    return {**status(last['state']),'backup':str(dest)}

def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='cmd',required=True)
    specs={'init':[('canon',str),('state',str)],'commit':[('expected',int),('state',str),('event',str)],'audit':[],'recover':[],'roll':[('expected',int),('key',str),('probability',float)],'export':[('output',str)]}
    for name,fields in specs.items():
        sp=sub.add_parser(name); sp.add_argument('directory')
        for field,t in fields: sp.add_argument(field,type=t)
    a=p.parse_args()
    try: print(json.dumps(globals()['cmd_'+a.cmd](a),ensure_ascii=False)); return 0
    except (OSError,ValueError,KeyError,TypeError,zipfile.BadZipFile) as e:
        print(json.dumps({'ok':False,'error':str(e)},ensure_ascii=False),file=sys.stderr); return 1
if __name__=='__main__': sys.exit(main())
