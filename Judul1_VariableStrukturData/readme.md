👇

📌 README - Program Pemesanan Kursi Sederhana (Python)
🧾 Deskripsi

Program ini adalah aplikasi sederhana berbasis Python yang digunakan untuk melakukan pemesanan kursi. Program ini memanfaatkan struktur data list 2 dimensi (2D) untuk merepresentasikan kursi dalam bentuk baris dan kolom.

Pengguna dapat:

Melihat denah kursi
Memesan kursi
Keluar dari program
🧠 Konsep yang Digunakan

Program ini menggunakan beberapa konsep dasar dalam Python, yaitu:

List 2D (array dua dimensi)
Perulangan (while, for)
Percabangan (if, elif, else)
Penanganan error (try-except)
🪑 Struktur Data Kursi

Kursi disimpan dalam bentuk list 2D:

kursi = [[0 for _ in range(2)] for _ in range(3)]

Keterangan:

Terdiri dari 3 baris dan 2 kolom
Nilai 0 menandakan kursi kosong
Nilai 1 menandakan kursi sudah dipesan

Contoh tampilan awal:

0 0
0 0
0 0
⚙️ Cara Kerja Program
Program menampilkan menu
User memilih menu dengan memasukkan angka
Program menjalankan perintah sesuai pilihan
Program akan terus berjalan sampai user memilih keluar
📋 Menu Program
1. Tampilkan kursi
2. Pesan kursi
3. Keluar
1. Tampilkan Kursi

Menampilkan kondisi kursi saat ini dalam bentuk matriks.

2. Pesan Kursi
User diminta memasukkan nomor baris (0–2)
User diminta memasukkan nomor kolom (0–1)
Jika kursi kosong (0), maka akan diubah menjadi (1)
Jika kursi sudah terisi, akan muncul pesan bahwa kursi tidak tersedia
3. Keluar

Menghentikan program

⚠️ Validasi Input

Program menangani kesalahan input seperti:

Input bukan angka
Input di luar jangkauan indeks

Pesan yang ditampilkan:

Masukkan angka yang valid!

atau

Input tidak valid!
▶️ Cara Menjalankan Program
Pastikan Python sudah terinstall di komputer

Simpan kode program dengan nama:

kursi.py

Jalankan program melalui terminal atau CMD:

python kursi.py
📌 Contoh Penggunaan
1. Tampilkan kursi
2. Pesan kursi
3. Keluar
Pilihan: 2
Masukkan baris (0-2): 1
Masukkan kolom (0-1): 1
Kursi berhasil dipesan
👨‍💻 Author

Nama: Muhammad Candra (silakan ubah jika diperlukan
