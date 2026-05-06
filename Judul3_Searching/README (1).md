# Judul Program
Implementasi Sequential Search pada Pencarian Nama Peserta Seminar

## Deskripsi Singkat
Program ini dibuat untuk mensimulasikan proses pencarian nama peserta seminar yang sudah terdaftar dalam sebuah daftar peserta. Dalam program ini, data peserta disimpan menggunakan struktur data **List (array satu dimensi)**. Pengguna dapat memasukkan nama peserta yang ingin dicari, kemudian program akan melakukan pencarian untuk mengecek apakah nama tersebut ada di dalam daftar.

Algoritma yang diterapkan pada program ini adalah **Sequential Search (Linear Search)**, yaitu metode pencarian data dengan cara memeriksa elemen satu per satu secara berurutan mulai dari data pertama hingga data terakhir. Jika data yang dicari ditemukan, program akan menampilkan jumlah kemunculan nama tersebut. Jika tidak ditemukan, program akan memberikan informasi bahwa data tidak ada di dalam daftar.

## Source Code dan Penjelasan
<img width="1499" height="989" alt="Cuplikan layar 2026-05-05 204343" src="https://github.com/user-attachments/assets/f99f7b4c-aa37-4902-8f5b-aaf8f57598ff" />
<img width="1503" height="114" alt="Cuplikan layar 2026-05-05 204443" src="https://github.com/user-attachments/assets/609c7d24-da61-4d62-a192-eecddad2786c" />

### 1. Fungsi Sequential Search

```python
def sequential_search(data, n, target):
```

Bagian ini adalah fungsi untuk melakukan proses pencarian data menggunakan algoritma Sequential Search.

```python
i = 0
```

Variabel `i` digunakan sebagai indeks awal untuk memulai pencarian dari data pertama.

```python
counter = 0
```

Variabel `counter` digunakan untuk menghitung berapa kali data yang dicari ditemukan.

```python
while i < n:
```

Perulangan ini digunakan untuk memeriksa seluruh data satu per satu mulai dari indeks pertama sampai indeks terakhir.

```python
if data[i].lower() == target.lower():
```

Bagian ini digunakan untuk membandingkan data pada list dengan data yang dicari. Fungsi `lower()` dipakai agar huruf besar dan kecil dianggap sama.

```python
counter += 1
```

Jika data yang dicari ditemukan, maka jumlah pencarian akan ditambah satu.

```python
i += 1
```

Indeks berpindah ke data berikutnya untuk melanjutkan proses pencarian.

```python
return counter
```

Setelah semua data selesai diperiksa, fungsi akan mengembalikan jumlah data yang ditemukan.

---

### 2. Fungsi Main

```python
def main():
```

Ini adalah fungsi utama yang menjalankan seluruh program.

```python
data = ["Zaidan", "Zizo", "Nayla", "Nino", "Evan", "Dimas", "Nino", "Reza"]
```

Bagian ini digunakan untuk menyimpan daftar nama peserta seminar ke dalam list.

```python
n = len(data)
```

Bagian ini digunakan untuk menghitung jumlah data yang ada di dalam list.

```python
print(f"Daftar peserta seminar: {data}")
```

Menampilkan seluruh daftar nama peserta seminar.

```python
while True:
```

Perulangan ini digunakan agar program terus meminta input sampai pengguna memasukkan data yang benar.

```python
target = input("Masukkan nama peserta yang ingin dicari: ")
```

Pengguna diminta memasukkan nama peserta yang ingin dicari.

```python
if target.strip() != "":
```

Bagian ini digunakan untuk mengecek apakah input kosong atau tidak. Fungsi `strip()` digunakan untuk menghapus spasi kosong.

```python
break
```

Jika input benar atau tidak kosong, program keluar dari perulangan.

```python
else:
```

Bagian ini dijalankan jika kondisi sebelumnya tidak terpenuhi.

```python
print("Input tidak boleh kosong!")
```

Menampilkan pesan error jika pengguna tidak memasukkan data.

---

### 3. Menjalankan Sequential Search

```python
counter = sequential_search(data, n, target)
```

Bagian ini memanggil fungsi Sequential Search untuk mencari nama peserta seminar.

---

### 4. Menampilkan Hasil Pencarian

```python
if counter > 0:
```

Bagian ini mengecek apakah data ditemukan.

```python
print(f"Nama {target} ditemukan sebanyak {counter} kali.")
```

Jika data ditemukan, program akan menampilkan jumlah data yang ditemukan.

```python
else:
```

Bagian ini dijalankan jika data tidak ditemukan.

```python
print(f"Nama {target} tidak ditemukan.")
```

Program akan menampilkan bahwa data tidak ditemukan.

---

### 5. Menjalankan Program

```python
if __name__ == "__main__":
```

Bagian ini digunakan untuk memastikan program dijalankan langsung dari file utama.

```python
main()
```

Menjalankan fungsi utama program.


## Output Program
### Screenshot Output
<img width="1481" height="224" alt="Cuplikan layar 2026-05-05 204231" src="https://github.com/user-attachments/assets/ae50147d-1731-4c17-8998-35e95db6ba37" />


## Penjelasan Output Program
Pada saat program dijalankan, sistem akan menampilkan daftar nama peserta seminar yang sudah tersimpan di dalam list. Setelah itu pengguna diminta memasukkan nama peserta yang ingin dicari.

Program kemudian melakukan proses pencarian menggunakan algoritma Sequential Search, yaitu dengan memeriksa data satu per satu mulai dari data pertama hingga data terakhir.

Jika nama peserta ditemukan, program akan menampilkan informasi bahwa nama tersebut ditemukan beserta jumlah kemunculannya. Jika nama yang dimasukkan tidak ada di dalam daftar, program akan menampilkan pesan bahwa nama tidak ditemukan.

## Link vidio youtube
https://youtu.be/i7-1BE0wWuc?si=aFsNIq3zvYtFLDAE

## Pencarian Data Menggunakan Interpolation Search

<img width="960" height="1280" alt="WhatsApp Image 2026-05-06 at 19 51 45" src="https://github.com/user-attachments/assets/957fed4a-842e-4999-ae5b-8144214dbb5b" />
<img width="960" height="1280" alt="WhatsApp Image 2026-05-06 at 19 51 46" src="https://github.com/user-attachments/assets/232b1859-102a-4926-ae0a-ca6f6a687bf3" />
