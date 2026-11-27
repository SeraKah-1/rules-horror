# Opsi tindakan adaptif

Tujuan opsi adalah membuat tindakan yang tersedia mudah dipahami, bukan memberi solusi atau membatasi aksi. Pilihan merupakan antarmuka terhadap dunia, bukan cabang cerita yang sudah ditulis. Semua tindakan valid diproses dengan simulator yang sama.

## Cara merancang opsi
1. Tentukan kondisi yang dapat diamati, sasaran pemain dan keputusan yang perlu dibuat saat ini. Jangan membocorkan kondisi tersembunyi.
2. Identifikasi beberapa pendekatan yang benar-benar berbeda (misalnya mengamankan posisi, menyelidiki, berpindah, menunggu, berinteraksi, menghadapi, menggunakan benda, atau meninggalkan kesempatan). Jangan selalu memakai kategori sama atau jumlah yang sama. Opsi boleh merupakan variasi strategi dengan tujuan serupa bila cara, biaya atau akibatnya sungguh berbeda.
3. Uji keterbacaan tindakan: tulis apa yang hendak dilakukan, sasaran dan parameter yang perlu diketahui. Jangan menjanjikan hasil ("coba buka pintu", bukan "keluar dengan selamat"). Boleh tampilkan biaya waktu atau risiko yang wajar diketahui karakter tanpa mengungkap kebenaran aturan.
4. Jangan mengoptimalkan daftar menggunakan pengetahuan rahasia. Jangan menandai tindakan aman atau berbahaya, memberi saran optimal, menyembunyikan pilihan sederhana yang terlihat demi jebakan, atau memasukkan aksi yang mustahil diketahui pemain. Opsi tidak perlu semua layak secara objektif jika ketidaklayakan belum diketahui karakter; simulator yang menentukan hasilnya.
5. Variasikan 2–5 opsi pada keputusan nyata secara adaptif; tanpa menu pada aksi rutin atau jika pemain sudah jelas menyatakan rencana. Tawarkan aksi bebas. Dalam mode selalu, tampilkan pada keputusan yang bermakna, bukan setiap baris dialog. Dalam freeform, jangan menawarkan opsi kecuali diminta. Jangan membuat semua opsi berujung pada kejadian identik dengan memalsukan dampak; sebab yang sama memang dapat menyebabkan konvergensi wajar.

## Konsekuensi
Jangan merancang daftar dengan jatah benar/salah/netral. Semua bisa menguntungkan, merugikan, campuran, netral, tertunda atau murni naratif berdasarkan state, waktu dan hukum. Jangan menetapkan kategori berdasarkan posisi menu. Pilihan yang terlihat bijak dapat gagal dan yang tampak berisiko dapat berhasil; jangan membalik ekspektasi secara sistematis. Tindakan yang sama pada keadaan berbeda dapat menghasilkan hasil berbeda tanpa mengubah hukum. Pemain tidak harus mengetahui semua akibat, tetapi harus mengetahui apa yang ia lakukan. Tidak perlu memberi label moral; NPC dapat menilai sendiri. Menunggu, menolak atau pergi tetap sah; biaya fiktif dan ancaman tetap berjalan jika relevan.

## Penyajian
Tombol netral dengan panjang seimbang, tanpa warna semantik atau rekomendasi. Kirim aksi literal beserta campaign_id dan revisi. Aksi bebas bisa diketik seperti biasa. Interaksi UI yang tidak mengubah dunia tetap lokal; operasi dunia dikirim kembali kepada GM. Jangan menghitung waktu hanya karena pemain membaca menu. Opsi dari revisi usang harus ditolak dengan tampilan keadaan terbaru; pemain dapat mengulang niat melalui chat. Jika UI tidak tersedia, daftar teks ringkas. Jangan memunculkan panel opsi pada setiap respons hanya untuk mengisi layar.

Sumber konsep: https://www.choiceofgames.com/2016/12/how-to-write-intentional-choices/ dan https://www.choiceofgames.com/2010/03/5-rules-for-writing-interesting-choices-in-multiple-choice-games/.
