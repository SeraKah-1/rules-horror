# Rules Horror — v2.0

Paket skill untuk bermain langsung melalui ChatGPT, bukan game yang berjalan sendiri. `SKILL.md` adalah instruksi inti; `refs/` adalah referensi; `scripts/save_engine.py` membantu menyimpan dan mengaudit kampanye. Tidak ada skenario atau spoiler kampanye asli di paket ini.

## Cara pakai di ChatGPT
Jika punya akses Skills, unggah paket skill sesuai UI yang tersedia. Bila tidak, buat Project khusus Rules Horror, gunakan mode Chat dan GPT-6.2 High jika tersedia, unggah SKILL.md serta lima file referensi dan skrip (ekstrak ZIP dahulu). Tambahkan instruksi proyek: "Gunakan SKILL.md Rules Horror saat saya meminta bermain. Ikuti referensi dan gunakan skrip simpanan jika tersedia. Jangan mulai kampanye sebelum saya memintanya." Bisa juga unggah paket ZIP di chat dan minta ChatGPT mengekstrak serta mengikuti SKILL.md; ini membutuhkan akses alat file/Python. Paket tidak otomatis memasang skill atau plugin pada akun.

Panggil dengan `Mulai Rules Horror`, `Rules Horror /new`, `Quick Start`, atau berikan preferensi langsung. Untuk setup khusus tulis `Rules Horror custom`. Untuk lanjut: `/continue` dan unggah backup jika save tidak tersedia. Gunakan `/save` untuk menghasilkan cadangan (mengandung spoiler, jangan dibaca saat bermain). `/audit` untuk mengecek konsistensi tanpa spoiler. `/ooc` untuk diskusi di luar permainan.

Paket dirancang untuk native Intelligent UI bila tersedia; bukan UI custom yang terus berjalan sendiri. Jika UI tidak tersedia, gameplay tetap teks. File runtime mungkin hilang, backup manual diperlukan. Validator hanya mengecek integritas struktural; belum menjamin kualitas prosa, kausalitas semantik, atau bebas sycophancy. Gameplay belum diuji end-to-end di ChatGPT.

## Perubahan v2.0
Horror Director aktif, tekanan berbasis waktu/kondisi, anti-stagnasi, payoff, scene framing, prosa sensoris, opsi tindakan adaptif. File `refs/horror-direction.md` dan `refs/choices.md` baru. Save lama dapat ditambah field state tanpa retcon; kampanye baru lebih cocok bila ancaman sebelumnya tidak ditetapkan. Skrip penyimpanan dipertahankan, bukan mesin ancaman otomatis. Uji perilaku baru adalah skenario manual, belum diuji end-to-end.
