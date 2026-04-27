# Judul Program
Implementasi Algoritma Bubble Sort pada Pengurutan Tinggi Badan Siswa

## Deskripsi Singkat
Program ini dibuat untuk mengurutkan data tinggi badan siswa menggunakan algoritma **Bubble Sort**. Pengguna(user) diminta memasukkan jumlah siswa dan tinggi badan masing-masing siswa, kemudian data tersebut akan ditampilkan sebelum dan sesudah proses pengurutan.Jadi dengan adanya program ini, data tinggi badan siswa bisa tersusun dari yang paling rendah sampai yang paling tinggi sehingga lebih mudah untuk dilihat dan dibandingkan.

Algoritma yang digunakan pada program ini adalah **Bubble Sort**, yaitu algoritma pengurutan yang bekerja dengan cara membandingkan dua data yang bersebelahan, lalu menukarnya jika urutannya masih salah. Proses ini dilakukan secara berulang sampai semua data terurut dengan benar. Struktur data yang digunakan adalah **List (Array 1 Dimensi)**, karena data tinggi badan siswa disimpan dalam satu baris data yang nantinya diproses dalam proses pengurutan.

## Source Code dan Penjelasan

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
![Output Program](output-program.png)

### Penjelasan Output
Pada saat program dijalankan, pengguna diminta untuk memasukkan jumlah siswa yang datanya ingin diurutkan. Setelah itu, pengguna memasukkan tinggi badan masing-masing siswa sesuai jumlah yang sudah ditentukan.

Setelah semua data berhasil dimasukkan, program akan menampilkan data tinggi badan sebelum dilakukan proses pengurutan. Selanjutnya, program menjalankan algoritma Bubble Sort dengan cara membandingkan dua data yang berdekatan dan menukarnya jika urutannya belum sesuai.

Setelah proses pengurutan selesai, program menampilkan hasil akhir berupa data tinggi badan yang sudah terurut dari yang paling rendah ke yang paling tinggi. Output ini menunjukkan bahwa program berhasil berjalan sesuai dengan studi kasus yang dibuat tanpa mengalami error.
