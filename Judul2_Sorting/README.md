# Judul Program
Implementasi Algoritma Bubble Sort pada Pengurutan Tinggi Badan Siswa

## Deskripsi Singkat
Program ini saya buat untuk mengurutkan data tinggi badan siswa menggunakan algoritma **Bubble Sort**. Pertama Pengguna(user) diminta untuk memasukkan jumlah siswa dan tinggi badan masing-masing siswa. Setelah itu data tersebut akan ditampilkan, sebelum dan sesudah proses pengurutan. Jadi dengan adanya program ini, data tinggi badan siswa bisa tersusun dari yang paling rendah sampai yang paling tinggi sehingga lebih mudah untuk dilihat dan dibandingkan.

Algoritma yang saya gunakan pada program ini adalah **Bubble Sort**, yaitu algoritma pengurutan yang bekerja dengan cara membandingkan dua data yang bersebelahan, lalu menukarnya jika urutannya masih salah. Proses ini dilakukan secara berulang sampai semua data terurut dengan benar dan Struktur data yang digunakan adalah **List (Array 1 Dimensi)**, karena data tinggi badan siswa disimpan dalam satu baris data yang nantinya diproses dalam proses pengurutan.

## Source Code dan Penjelasan
<img width="1708" height="1035" alt="Cuplikan layar 2026-04-28 094504" src="https://github.com/user-attachments/assets/0d194b3f-1bc7-4ec4-b689-a2fac4859e62" />
<img width="1713" height="1039" alt="Cuplikan layar 2026-04-28 094525" src="https://github.com/user-attachments/assets/fd28ca66-9c2d-4cab-b43a-97307364acad" />




### 1. Fungsi Tukar

```python
def tukar(arr, i, j):
```

Baris ini digunakan untuk membuat fungsi `tukar` yang berfungsi menukar dua data dalam array.

```python
temp = arr[i]
```

Menyimpan nilai sementara dari indeks `i`.

```python
arr[i] = arr[j]
```

Memindahkan nilai indeks `j` ke indeks `i`.

```python
arr[j] = temp
```

Mengisi indeks `j` dengan nilai yang disimpan sementara.

---

### 2. Fungsi Bubble Sort

```python
def bubble_sort(arr, n):
```

Membuat fungsi untuk proses pengurutan Bubble Sort.

```python
for i in range(n - 1):
```

Perulangan untuk jumlah putaran sorting.

```python
for j in range(n - i - 1):
```

Perulangan untuk membandingkan data yang berdekatan.

```python
if arr[j] > arr[j + 1]:
```

Mengecek apakah data sebelah kiri lebih besar.

```python
tukar(arr, j, j + 1)
```

Menukar posisi data jika urutannya salah.

---

### 3. Fungsi Main

```python
def main():
```

Fungsi utama program.

```python
n = int(input("Masukkan jumlah siswa: "))
```

Input jumlah data siswa.

```python
tinggi = []
```

Membuat list kosong.

```python
for i in range(n):
```

Perulangan input data.

```python
data = int(input(f"Tinggi siswa ke-{i+1}: "))
```

Input data tinggi badan.

```python
tinggi.append(data)
```

Menambahkan data ke list.

---

### 4. Menampilkan Data Awal

```python
print(f"Tinggi sebelum diurutkan: {tinggi}")
```

Menampilkan data sebelum sorting.

---

### 5. Menjalankan Bubble Sort

```python
bubble_sort(tinggi, n)
```

Memanggil fungsi Bubble Sort.

---

### 6. Menampilkan Hasil

```python
for i in range(n):
```

Perulangan menampilkan data.

```python
print(tinggi[i], end=" ")
```

Menampilkan data hasil sorting.

---

### 7. Menjalankan Program

```python
if __name__ == "__main__":
```

Mengecek file utama.

```python
main()
```

Menjalankan program.

## Output Program

### Screenshot Output
<img width="1449" height="405" alt="Cuplikan layar 2026-04-28 094722" src="https://github.com/user-attachments/assets/b61c3de5-3f94-4c5d-8612-4f44af1aec07" />

## Penjelasan Output Program

Pada saat program dijalankan, pengguna diminta untuk memasukkan jumlah siswa yang datanya ingin diurutkan. Selanjutnya pengguna di minta memasukkan tinggi badan masing-masing siswa.

Setelah semua data berhasil dimasukkan, program akan menampilkan data sebelum proses pengurutan dilakukan. Kemudian program menjalankan algoritma Bubble Sort dengan metode ascending, yaitu mengurutkan data dari yang paling kecil ke yang paling besar dengan cara membandingkan dua data yang berdekatan atau bersebelahan dan menukar jika urutannya belum sesuai.

Setelah proses sorting selesai, program akan menampilkan hasil akhir yaitu berupa data tinggi badan yang sudah terurut secara ascending. Output ini menunjukkan bahwa algoritma Bubble Sort berhasil bekerja dengan baik sesuai studi kasus yang dibuat tanpa mengalami error.

