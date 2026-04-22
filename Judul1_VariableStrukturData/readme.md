# 🎬 Sistem Pemesanan Kursi Bioskop (List 2 Dimensi)

Proyek ini adalah simulasi sederhana sistem pemesanan kursi bioskop yang mengimplementasikan konsep **Struktur Data List 2 Dimensi** menggunakan bahasa pemrograman Python.

## 📝 Deskripsi
Program ini memungkinkan pengguna untuk melihat denah kursi yang tersedia, memilih lokasi kursi berdasarkan koordinat baris dan kolom, serta memperbarui status kursi tersebut secara otomatis setelah dipesan. Ini adalah bagian dari tugas mata kuliah **Praktikum Struktur Data (PSD) 2026**.

## ✨ Fitur Utama
- **Visualisasi Denah**: Menampilkan grid kursi dalam format baris dan kolom.
- **Pemesanan Kursi**: Input interaktif untuk memilih kursi (Baris & Kolom).
- **Validasi Status**: Sistem akan mengecek apakah kursi sudah terisi atau masih kosong sebelum memproses pesanan.
- **Simbol Status**:
  - `[O]` : Kursi Kosong/Tersedia.
  - `[X]` : Kursi Terisi/Sudah Dipesan.

## 🛠️ Logika Struktur Data
Program menggunakan *Nested List* (List di dalam List) untuk merepresentasikan matriks kursi:
```python # Contoh inisialisasi grid
denah = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]
