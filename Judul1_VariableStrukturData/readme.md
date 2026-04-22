# 🎬 Implementasi List 2 Dimensi pada Sistem Pemesanan Kursi Bioskop

## 📌 Deskripsi
Program ini merupakan implementasi struktur data **List 2 Dimensi (List 2D)** menggunakan bahasa Python.  
Program ini digunakan untuk mensimulasikan sistem pemesanan kursi bioskop.

List 2D digunakan karena memiliki struktur baris dan kolom yang sesuai dengan denah kursi bioskop.

---

## 🎯 Fitur Program
- Menampilkan denah kursi
- Memesan kursi
- Validasi input
- Keluar dari program

---

## 🧠 Penjelasan Kode

### 1. Inisialisasi List 2D
```python
kursi = [[0 for _ in range(2)] for _ in range(3)]

### 2. Menu Program
Program memiliki menu untuk memilih aksi yang akan dilakukan oleh pengguna, yaitu:
- Menampilkan kursi
- Memesan kursi
- Keluar dari program

---

### 3. Perulangan Program
Program menggunakan perulangan `while` agar dapat berjalan terus sampai pengguna memilih keluar.

---

### 4. Menampilkan Kursi
Program menggunakan perulangan bersarang (`for`) untuk menampilkan seluruh isi kursi berdasarkan baris dan kolom.

---

### 5. Pemesanan Kursi
Pengguna memasukkan nomor baris dan kolom kursi. Program akan mengecek apakah kursi masih kosong atau sudah terisi.

---

### 6. Validasi Input
Program menggunakan `try-except` untuk menangani kesalahan input agar program tidak error saat dijalankan.

---

## ▶️ Contoh Output

---

## 🎥 Link Video Presentasi
Masukkan link YouTube kamu di sini

---

## 🧾 Kesimpulan
List 2 Dimensi sangat cocok digunakan untuk merepresentasikan data berbentuk tabel seperti kursi bioskop karena memiliki struktur baris dan kolom yang jelas.
