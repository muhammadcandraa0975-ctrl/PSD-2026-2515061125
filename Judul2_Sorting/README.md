# Judul Program
Implementasi Algoritma Bubble Sort pada Pengurutan Tinggi Badan Siswa

## Deskripsi Singkat
Program ini saya buat untuk mengurutkan data tinggi badan siswa menggunakan algoritma **Bubble Sort**. Pertama Pengguna (user) diminta untuk memasukkan jumlah siswa dan tinggi badan masing-masing siswa. Setelah itu data tersebut akan ditampilkan, sebelum dan sesudah proses pengurutan. Jadi dengan adanya program ini, data tinggi badan siswa bisa tersusun dari yang paling rendah sampai yang paling tinggi sehingga lebih mudah untuk dilihat dan dibandingkan.

Algoritma yang saya gunakan pada program ini adalah **Bubble Sort**, yaitu algoritma pengurutan yang bekerja dengan cara membandingkan dua data yang bersebelahan, lalu menukarnya jika urutannya masih salah. Proses ini dilakukan secara berulang sampai semua data terurut dengan benar dan struktur data yang digunakan adalah **List (Array 1 Dimensi)**, karena data tinggi badan siswa disimpan dalam satu baris data yang nantinya diproses dalam proses pengurutan.


## Source Code dan Penjelasan
<img width="1596" height="1040" alt="Cuplikan layar 2026-04-28 210318" src="https://github.com/user-attachments/assets/bd4336f4-fcd0-4921-b32f-a4bdabd62eb6" />
<img width="1600" height="1050" alt="Cuplikan layar 2026-04-28 210247" src="https://github.com/user-attachments/assets/3f0b367c-1ac3-4145-a06d-939efbdaa427" />


### 1. Fungsi Tukar

```python
def tukar(arr, i, j):
```

Bagian ini adalah fungsi untuk menukar dua data yang ada di dalam array. Fungsi ini dipakai kalau ada data yang urutannya masih salah.

```python
temp = arr[i]
```

Data pada indeks `i` disimpan dulu ke variabel sementara supaya datanya tidak hilang saat ditukar.

```python
arr[i] = arr[j]
```

Data pada indeks `j` dipindahkan ke indeks `i`.

```python
arr[j] = temp
```

Data yang tadi disimpan sementara dimasukkan ke indeks `j`. Jadi posisi kedua data sudah berhasil ditukar.

---

### 2. Fungsi Bubble Sort

```python
def bubble_sort(arr, n):
```

Bagian ini adalah fungsi utama untuk melakukan pengurutan data dengan Bubble Sort.

```python
for i in range(n - 1):
```

Perulangan pertama dipakai untuk menentukan berapa kali proses pengurutan dilakukan. Kalau jumlah data ada `n`, biasanya cukup `n-1` kali.

```python
for j in range(n - i - 1):
```

Perulangan kedua dipakai untuk membandingkan data yang posisinya bersebelahan.

```python
if arr[j] > arr[j + 1]:
```

Bagian ini mengecek apakah data kiri lebih besar dari data kanan. Kalau iya, berarti urutannya salah.

```python
tukar(arr, j, j + 1)
```

Kalau urutannya salah, data akan ditukar menggunakan fungsi `tukar`.

---

### 3. Fungsi Main

```python
def main():
```

Ini adalah fungsi utama yang menjalankan semua proses program.

```python
try:
```

Bagian ini dipakai untuk mencoba menerima input dari pengguna.

```python
n = int(input("Masukkan jumlah siswa: "))
```

Pengguna diminta memasukkan jumlah data yang ingin diurutkan.

```python
except ValueError:
```

Bagian ini akan dijalankan kalau pengguna salah input, misalnya memasukkan huruf.

```python
print("Input tidak valid!")
```

Menampilkan pesan kalau input salah.

```python
return
```

Program berhenti kalau input jumlah data tidak benar.

```python
tinggi = []
```

Membuat list kosong untuk menyimpan data tinggi badan.

```python
print("Masukkan tinggi badan siswa:")
```

Menampilkan perintah untuk mulai input data.

```python
for i in range(n):
```

Perulangan untuk input data sebanyak jumlah yang sudah dimasukkan.

```python
while True:
```

Dipakai supaya kalau input salah, program bisa meminta input ulang.

```python
try:
```

Mencoba menerima input tinggi badan.

```python
data = int(input(f"Tinggi siswa ke-{i+1}: "))
```

Pengguna memasukkan tinggi badan siswa.

```python
tinggi.append(data)
```

Data yang dimasukkan langsung disimpan ke dalam list.

```python
break
```

Kalau input benar, keluar dari perulangan.

```python
except ValueError:
```

Kalau input salah, program masuk ke bagian ini.

```python
print("Input tidak valid, silakan masukkan angka!")
```

Menampilkan pesan error dan meminta input ulang.

---

### 4. Menampilkan Data Sebelum Sorting

```python
print(f"Tinggi sebelum diurutkan: {tinggi}")
```

Bagian ini menampilkan data sebelum diurutkan supaya bisa dilihat urutan awalnya.

---

### 5. Menjalankan Bubble Sort

```python
bubble_sort(tinggi, n)
```

Bagian ini menjalankan fungsi Bubble Sort untuk mulai mengurutkan data.

---

### 6. Menampilkan Hasil Sorting

```python
print("Tinggi setelah diurutkan:", end=" ")
```

Menampilkan tulisan bahwa data sudah selesai diurutkan.

```python
for i in range(n):
```

Perulangan untuk menampilkan semua data hasil sorting.

```python
print(tinggi[i], end=" ")
```

Menampilkan data satu per satu.

```python
print()
```

Membuat baris baru supaya tampilan lebih rapi.

---

### 7. Menjalankan Program

```python
if __name__ == "__main__":
```

Bagian ini digunakan supaya program bisa dijalankan langsung.

```python
main()
```

Menjalankan fungsi utama program.


## Output Program

### Screenshot Output
<img width="1449" height="405" alt="Cuplikan layar 2026-04-28 094722" src="https://github.com/user-attachments/assets/b61c3de5-3f94-4c5d-8612-4f44af1aec07" />

## Penjelasan Output Program

Pada saat program dijalankan, pengguna diminta untuk memasukkan jumlah siswa yang datanya ingin diurutkan. Selanjutnya pengguna diminta memasukkan tinggi badan masing-masing siswa.

Setelah semua data berhasil dimasukkan, program akan menampilkan data sebelum proses pengurutan dilakukan. Kemudian program menjalankan algoritma Bubble Sort dengan metode ascending, yaitu mengurutkan data dari yang paling kecil ke yang paling besar dengan cara membandingkan dua data yang berdekatan atau bersebelahan dan menukar jika urutannya belum sesuai.

Setelah proses sorting selesai, program akan menampilkan hasil akhir yaitu berupa data tinggi badan yang sudah terurut secara ascending. Output ini menunjukkan bahwa algoritma Bubble Sort berhasil bekerja dengan baik sesuai studi kasus yang dibuat tanpa mengalami error.

## Link vidio youtube
https://youtu.be/dm3M7jBXLkg
