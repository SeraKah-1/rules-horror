# Penyimpanan kampanye

Tiga file utama di direktori unik yang dapat ditulis (misalnya `/mnt/data/campaign-<id>` jika tersedia). Jangan menulis save di direktori skill. Jangan menggunakan data dari kampanye lain. CANON.md berisi fakta rahasia awal yang tetap; STATE.json adalah snapshot/cache; EVENTS.jsonl adalah jurnal otoritatif. File ini bukan bagian narasi. Jangan memuat seluruh isi ke UI atau membagikan sebagai teks tanpa permintaan reveal. Backup berisi spoiler.

## Kontrak data
Gunakan objek JSON, ID stabil, waktu dunia dalam detik integer nonnegatif sejak awal. STATE wajib memiliki `campaign_id` (unik), `revision` (0 awal), `world_time` (detik), `seed` (string acak rahasia), `player` (objek), `actors` (objek ID → kondisi), `locations` (objek ID → lokasi), `items` (objek ID → kondisi), `pending` (objek ID → kejadian), `established` (objek ID → fakta objektif tambahan yang sudah ditetapkan), `knowledge` (objek ID → klaim dan sumber), `perception` (objek), `devices` (objek), `preferences` (objek). Tambahkan struktur sesuai dunia, tidak wajib meter angka. Bila player/actor memiliki `location`, ID harus ada di `locations` atau null jika tidak diketahui/tidak berlaku. Catat item di satu lokasi/pemilik kecuali canon mengizinkan pengecualian secara eksplisit. Jangan menghapus item yang berpindah; catat statusnya. Pending memiliki sebab, pemicu, status, dan kondisi pembatalan; status resolved/cancelled tidak boleh diam-diam kembali aktif. Established fakta historis tidak boleh ditimpa; fakta dinamis di tempat lain. Koreksi fakta historis dicatat sebagai entri baru yang menunjuk fakta lama, dengan penjelasan eksplisit, tanpa mengubah catatan lama.

Event awal dan setiap commit memuat revision, action, causes (ID hukum/event/pemicu relevan), outcome (objektif), perceived (yang dapat diketahui pemain), rolls (bila ada), full state, hash canon dan hash rantai. Simpan event baru meskipun aksi tidak signifikan; simpan narasi/tampilan yang direncanakan sebelum disampaikan jika relevan. Riwayat adalah sumber utama; cache dapat direkonstruksi. Gunakan event untuk menelusuri efek tertunda dan sumber informasi. Jangan menulis ulang log. Saat terjadi kesalahan penyajian setelah commit, buat koreksi yang dapat dilacak. Jangan diam-diam memajukan dunia untuk aksi administratif.

## Skrip Python (opsional, disarankan)
Jalankan tanpa network, hanya standard library. Script menerima path absolut/relatif, tidak perlu instalasi dependensi. `python scripts/save_engine.py --help`. Buat berkas draft state awal dan canon di lokasi staging, kemudian:

```
python scripts/save_engine.py init <dir-kampanye> <draft-canon.md> <draft-state.json>
python scripts/save_engine.py audit <dir-kampanye>
python scripts/save_engine.py roll <dir-kampanye> <expected_revision> <roll_key> <probability>
python scripts/save_engine.py commit <dir-kampanye> <expected_revision> <next-state.json> <event.json>
python scripts/save_engine.py recover <dir-kampanye>
python scripts/save_engine.py export <dir-kampanye> <backup.zip>
```

`next-state.json` berisi state lengkap dengan revision = expected_revision + 1. Event draft wajib berisi action (string), causes (array), outcome (string/objek), perceived (string/objek), rolls (array; boleh kosong). Roll memakai kunci stabil per kejadian (bukan memilih kunci setelah melihat hasil); nilai probabilitas 0..1 diputus sebelum roll; rekam hasil lengkap dari script. Audit tidak mencetak isi rahasia, roll dan berkas draft internal jangan ditampilkan dalam narasi. Commit menolak revisi usang, perubahan canon, perubahan seed/campaign ID, waktu mundur, lokasi tak valid dan perubahan fakta established. Log diganti atomik dengan riwayat lama + satu record baru, lalu cache state ditulis atomik. Jika cache gagal ditulis, log tetap otoritatif; recover menulis snapshot dari log. Jalankan satu penulis per kampanye; skrip bukan database multi-user, tidak menjamin validasi semantik. Hash chain mendeteksi perubahan tidak konsisten, bukan perlindungan dari penulis yang sengaja menghitung ulang seluruh log.

Untuk load ZIP, ekstrak tiga nama file yang diharapkan ke direktori baru, jangan ekstrak path lain atau menimpa save aktif. Audit dan recover jika cache saja berbeda. Untuk cabang checkpoint, buat kampanye baru dengan ID dan seed baru atau seed lama jika ingin replay konsisten, catat referensi ID kampanye/revisi lama di event awal atau state, jangan mengubah riwayat asli. Jangan klaim upload proyek/penyimpanan cloud otomatis. Ekspor backup untuk melanjutkan antarchat; jika akses script tidak tersedia, lakukan operasi file yang ekuivalen atau nyatakan keterbatasan dan jangan berpura-pura menyimpan.
