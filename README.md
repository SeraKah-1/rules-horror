# Rules Horror

Plugin ChatGPT untuk bermain horor berbahasa Indonesia. Dunia mengikuti sebab-akibat, informasi yang diterima karakter bisa keliru, dan konsekuensi mengikuti kondisi dunia.

Pilih **Rules Horror** di ChatGPT dan ketik `Mulai Rules Horror` untuk bermain. Ketik `Rules Horror custom` untuk mengatur kampanye atau `/continue` untuk lanjut. Pakai `/save` untuk mengekspor cadangan kampanye. Jika sesi baru kehilangan akses ke simpanan, unggah cadangan itu saat melanjutkan.

[Instruksi GM](skills/rules-horror/SKILL.md) dan [panduan skill](skills/rules-horror/README.md) ada di dalam paket. Intelligent UI dan penyimpanan mengikuti kemampuan sesi ChatGPT yang menjalankan permainan. [Panduan penyimpanan](skills/rules-horror/refs/storage.md)

## Mengemas plugin

Dari direktori repo, jalankan perintah berikut untuk membuat arsip dengan manifes di akar.

```sh
zip -r ../rules-horror-plugin.zip plugin.json skills -x '*/__pycache__/*' '*.pyc'
```
