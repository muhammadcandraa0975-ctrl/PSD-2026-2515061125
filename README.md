# Judul Program
Implementasi Queue Array pada Sistem Antrian Pasien Klinik

## Deskripsi Singkat
Program ini dibuat untuk mensimulasikan sistem antrian pasien di sebuah klinik menggunakan struktur data Queue berbasis array. Dalam program ini, pasien yang datang lebih dulu akan dilayani lebih dulu sesuai dengan konsep FIFO (First In First Out). Pengguna dapat menambahkan pasien ke dalam antrian, memanggil pasien, melihat pasien yang berada di antrian paling depan, serta menampilkan seluruh daftar antrian pasien.

Algoritma struktur data yang diterapkan pada program ini adalah Queue (Antrian) menggunakan array. Operasi utama yang digunakan yaitu enqueue untuk menambahkan data ke antrian, dequeue untuk menghapus data dari antrian, peek untuk melihat data terdepan, dan display untuk menampilkan seluruh isi antrian. Program juga menggunakan percabangan, perulangan, serta validasi input agar program dapat berjalan dengan baik dan tidak mudah mengalami error.
## Source Code dan Penjelasan
<img width="1493" height="901" alt="Cuplikan layar 2026-05-12 105108" src="https://github.com/user-attachments/assets/71986a80-ba8c-4bb0-96bc-1dd75be15bed" />
<img width="1503" height="885" alt="Cuplikan layar 2026-05-12 105151" src="https://github.com/user-attachments/assets/0fc64526-f822-4a90-aa56-df2e47aa74a1" />
<img width="1498" height="789" alt="Cuplikan layar 2026-05-12 105246" src="https://github.com/user-attachments/assets/98794e96-b60a-4d9d-9287-dd341a4267e0" />

### 1. Membuat Class Queue

```python
class QueueArray:
```

Bagian ini digunakan untuk membuat class QueueArray sebagai struktur utama program antrian pasien.

---

### 2. Constructor / Inisialisasi Data

```python
def __init__(self, max_size=100):
```

Bagian ini adalah constructor yang akan dijalankan pertama kali saat objek queue dibuat.

```python
self.MAXN = max_size
```

Menyimpan kapasitas maksimal queue.

```python
self.q = [None] * self.MAXN
```

Membuat array kosong untuk menyimpan data pasien.

```python
self.front_idx = -1
```

Variabel ini digunakan untuk menandai posisi depan queue.

```python
self.rear_idx = -1
```

Variabel ini digunakan untuk menandai posisi belakang queue.

---

### 3. Fungsi Mengecek Queue Kosong

```python
def is_empty(self):
```

Fungsi ini digunakan untuk mengecek apakah queue kosong atau tidak.

```python
return self.front_idx == -1
```

Jika `front_idx` bernilai `-1`, berarti queue kosong.

---

### 4. Fungsi Mengecek Queue Penuh

```python
def is_full(self):
```

Fungsi ini digunakan untuk mengecek apakah queue sudah penuh.

```python
return (self.rear_idx + 1) % self.MAXN == self.front_idx
```

Jika posisi belakang berikutnya sama dengan posisi depan, maka queue dianggap penuh.

---

### 5. Fungsi Enqueue

```python
def enqueue(self, x):
```

Fungsi ini digunakan untuk menambahkan pasien ke dalam antrian.

```python
if self.is_full():
```

Mengecek apakah queue penuh.

```python
print("Antrian penuh")
```

Menampilkan pesan jika queue penuh.

```python
return
```

Menghentikan fungsi jika queue penuh.

```python
if self.is_empty():
```

Mengecek apakah queue masih kosong.

```python
self.front_idx = 0
self.rear_idx = 0
```

Jika queue kosong, maka posisi depan dan belakang diisi indeks pertama.

```python
else:
```

Bagian ini dijalankan jika queue tidak kosong.

```python
self.rear_idx = (self.rear_idx + 1) % self.MAXN
```

Posisi belakang digeser ke indeks berikutnya.

```python
self.q[self.rear_idx] = x
```

Menyimpan nama pasien ke dalam queue.

```python
print(f"Pasien {x} berhasil masuk antrian")
```

Menampilkan pesan bahwa pasien berhasil masuk antrian.

---

### 6. Fungsi Dequeue

```python
def dequeue(self):
```

Fungsi ini digunakan untuk memanggil atau menghapus pasien dari antrian depan.

```python
if self.is_empty():
```

Mengecek apakah queue kosong.

```python
print("Antrian kosong")
```

Menampilkan pesan jika queue kosong.

```python
return
```

Menghentikan fungsi jika queue kosong.

```python
print(f"Pasien {self.q[self.front_idx]} dipanggil")
```

Menampilkan pasien yang berada di antrian paling depan.

```python
if self.front_idx == self.rear_idx:
```

Mengecek apakah queue hanya memiliki satu data.

```python
self.front_idx = -1
self.rear_idx = -1
```

Jika hanya ada satu data, queue dikosongkan kembali.

```python
else:
```

Bagian ini dijalankan jika queue masih memiliki lebih dari satu data.

```python
self.front_idx = (self.front_idx + 1) % self.MAXN
```

Posisi depan digeser ke data berikutnya.

---

### 7. Fungsi Peek

```python
def peek(self):
```

Fungsi ini digunakan untuk melihat pasien paling depan tanpa menghapus data.

```python
if self.is_empty():
```

Mengecek apakah queue kosong.

```python
print("Antrian kosong")
```

Menampilkan pesan jika queue kosong.

```python
return
```

Menghentikan fungsi jika queue kosong.

```python
print(f"Pasien terdepan: {self.q[self.front_idx]}")
```

Menampilkan pasien yang berada di antrian paling depan.

---

### 8. Fungsi Display

```python
def display(self):
```

Fungsi ini digunakan untuk menampilkan seluruh isi queue.

```python
if self.is_empty():
```

Mengecek apakah queue kosong.

```python
print("Antrian kosong")
```

Menampilkan pesan jika queue kosong.

```python
return
```

Menghentikan fungsi jika queue kosong.

```python
print("Daftar antrian pasien: ", end="")
```

Menampilkan tulisan daftar antrian pasien.

```python
i = self.front_idx
```

Variabel `i` digunakan untuk memulai penelusuran queue dari depan.

```python
while True:
```

Perulangan digunakan untuk menampilkan seluruh isi queue.

```python
print(self.q[i], end=" ")
```

Menampilkan isi queue satu per satu.

```python
if i == self.rear_idx:
```

Mengecek apakah data sudah sampai di posisi belakang queue.

```python
break
```

Menghentikan perulangan jika sudah mencapai data terakhir.

```python
i = (i + 1) % self.MAXN
```

Berpindah ke indeks berikutnya.

```python
print()
```

Membuat baris baru agar output lebih rapi.

---

### 9. Fungsi Main

```python
def main():
```

Fungsi utama program.

```python
queue = QueueArray()
```

Membuat objek queue.

```python
pilih = 0
```

Variabel untuk menyimpan pilihan menu.

```python
while pilih != 5:
```

Perulangan menu akan terus berjalan sampai pengguna memilih keluar.

```python
print("\n=== SISTEM ANTRIAN PASIEN ===")
```

Menampilkan judul program.

```python
print("1. Tambah Pasien")
print("2. Panggil Pasien")
print("3. Lihat Antrian Depan")
print("4. Tampilkan Antrian")
print("5. Keluar")
```

Menampilkan daftar menu program.

```python
try:
```

Digunakan untuk mencoba menerima input.

```python
pilih = int(input("Pilih menu: "))
```

Pengguna diminta memilih menu.

```python
except ValueError:
```

Dijalankan jika input salah.

```python
print("Input tidak valid!")
```

Menampilkan pesan error.

```python
continue
```

Mengulang kembali menu.

---

### 10. Pilihan Menu

```python
if pilih == 1:
```

Jika pengguna memilih menu tambah pasien.

```python
nama = input("Masukkan nama pasien: ")
```

Meminta input nama pasien.

```python
queue.enqueue(nama)
```

Menambahkan pasien ke queue.

```python
elif pilih == 2:
```

Jika pengguna memilih panggil pasien.

```python
queue.dequeue()
```

Menjalankan proses dequeue.

```python
elif pilih == 3:
```

Jika pengguna memilih lihat antrian depan.

```python
queue.peek()
```

Menampilkan pasien paling depan.

```python
elif pilih == 4:
```

Jika pengguna memilih tampilkan antrian.

```python
queue.display()
```

Menampilkan seluruh isi queue.

```python
elif pilih == 5:
```

Jika pengguna memilih keluar.

```python
print("Program selesai.")
```

Menampilkan pesan program selesai.

```python
else:
```

Dijalankan jika pilihan menu tidak tersedia.

```python
print("Pilihan tidak valid!")
```

Menampilkan pesan error pilihan menu.

---

### 11. Menjalankan Program

```python
if __name__ == "__main__":
```

Digunakan untuk memastikan file dijalankan sebagai program utama.

```python
main()
```

Menjalankan fungsi utama program.


## Output Program
<img width="765" height="786" alt="Cuplikan layar 2026-05-12 210311" src="https://github.com/user-attachments/assets/e1472948-c7b4-4abb-9fcb-15402a6355f8" />
<img width="771" height="944" alt="Cuplikan layar 2026-05-12 210333" src="https://github.com/user-attachments/assets/5a4b1e31-d701-4ae7-abd0-a589e6c4eb0c" />

## Penjelasan Output Program
Pada saat program dijalankan, sistem akan menampilkan menu utama yang berisi beberapa pilihan, seperti menambah pasien, memanggil pasien, melihat antrian paling depan, menampilkan seluruh antrian, dan keluar dari program.

Ketika pengguna memilih menu tambah pasien, nama pasien yang dimasukkan akan disimpan ke dalam antrian menggunakan proses enqueue. Pasien yang pertama masuk akan berada di posisi paling depan dalam antrian.

Saat menu tampilkan antrian dipilih, program akan menampilkan seluruh daftar pasien sesuai urutan antrian dari depan ke belakang.

Jika pengguna memilih menu lihat antrian depan, program akan menampilkan nama pasien yang berada di posisi paling depan tanpa menghapus data dari antrian.

Ketika menu panggil pasien dipilih, pasien yang berada di antrian paling depan akan dipanggil dan dihapus dari antrian menggunakan proses dequeue.

Program ini menggunakan konsep FIFO (First In First Out), yaitu data atau pasien yang pertama masuk akan menjadi yang pertama keluar atau dipanggil.

## Link vidio youtube
https://youtu.be/qTZyoBkjHeg?si=4nekLFYcQIOmG2fb
