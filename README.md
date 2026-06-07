# Implementasi Hash Map Menggunakan Metode Separate Chaining pada Sistem Akun Game Online

## Deskripsi Singkat

Program ini dibuat untuk mengelola data akun game online menggunakan struktur data Hash Map dengan metode Separate Chaining. Setiap akun memiliki ID Player sebagai key dan Username sebagai value. Program menyediakan fitur untuk mencari akun berdasarkan ID Player, menambahkan akun baru, menghapus akun, serta menampilkan seluruh data akun yang tersimpan.

Metode Separate Chaining digunakan untuk menangani collision pada Hash Map dengan memanfaatkan linked list pada setiap bucket. Dengan menggunakan Hash Map, proses pencarian, penambahan, dan penghapusan data dapat dilakukan dengan lebih efisien.

---

# Source Code dan Penjelasan

## 1. Membuat Class Node

```python
class Node:
```

Bagian ini digunakan untuk membuat class Node sebagai tempat penyimpanan data pada Hash Map.

```python
def __init__(self, key, value):
```

Constructor yang dijalankan saat node baru dibuat.

```python
self.key = key
```

Digunakan untuk menyimpan ID Player.

```python
self.value = value
```

Digunakan untuk menyimpan Username.

```python
self.next = None
```

Digunakan untuk menghubungkan node dengan node berikutnya pada linked list.

---

## 2. Membuat Class HashMapSeparateChaining

```python
class HashMapSeparateChaining:
```

Bagian ini digunakan untuk membuat class utama Hash Map.

```python
def __init__(self, size=10):
```

Constructor class Hash Map.

```python
self.SIZE = size
```

Menyimpan ukuran Hash Table.

```python
self.table = [None] * self.SIZE
```

Membuat Hash Table kosong.

---

## 3. Fungsi Hash

```python
def hash_function(self, key):
```

Fungsi untuk menentukan indeks penyimpanan data.

```python
return (key % self.SIZE + self.SIZE) % self.SIZE
```

Menghasilkan indeks berdasarkan nilai key.

---

## 4. Fungsi Insert

```python
def insert(self, key, value):
```

Fungsi untuk menambahkan data akun ke Hash Map.

```python
index = self.hash_function(key)
```

Menentukan posisi bucket berdasarkan key.

```python
current = self.table[index]
```

Mengambil node pertama pada bucket tersebut.

```python
while current is not None:
```

Melakukan penelusuran linked list.

```python
if current.key == key:
```

Mengecek apakah key sudah ada.

```python
current.value = value
```

Mengubah value jika key ditemukan.

```python
return
```

Menghentikan proses insert.

```python
current = current.next
```

Berpindah ke node berikutnya.

```python
new_node = Node(key, value)
```

Membuat node baru.

```python
new_node.next = self.table[index]
```

Menghubungkan node baru ke linked list.

```python
self.table[index] = new_node
```

Menjadikan node baru sebagai node pertama pada bucket.

---

## 5. Fungsi Search

```python
def search(self, key):
```

Fungsi untuk mencari data akun berdasarkan ID Player.

```python
index = self.hash_function(key)
```

Menentukan bucket pencarian.

```python
current = self.table[index]
```

Mengambil node pertama pada bucket.

```python
while current is not None:
```

Melakukan penelusuran linked list.

```python
if current.key == key:
```

Mengecek apakah key ditemukan.

```python
return current
```

Mengembalikan data yang ditemukan.

```python
current = current.next
```

Berpindah ke node berikutnya.

```python
return None
```

Mengembalikan None jika data tidak ditemukan.

---

## 6. Fungsi Remove

```python
def remove_key(self, key):
```

Fungsi untuk menghapus data akun.

```python
index = self.hash_function(key)
```

Menentukan bucket yang akan diperiksa.

```python
current = self.table[index]
```

Mengambil node pertama.

```python
prev = None
```

Menyimpan node sebelumnya.

```python
while current is not None:
```

Melakukan penelusuran linked list.

```python
if current.key == key:
```

Mengecek apakah key ditemukan.

```python
if prev is None:
```

Mengecek apakah node yang dihapus adalah node pertama.

```python
self.table[index] = current.next
```

Menghapus node pertama.

```python
else:
```

Jika bukan node pertama.

```python
prev.next = current.next
```

Menghubungkan node sebelumnya ke node setelahnya.

```python
return True
```

Menandakan data berhasil dihapus.

```python
prev = current
```

Memindahkan posisi prev.

```python
current = current.next
```

Berpindah ke node berikutnya.

```python
return False
```

Menandakan data tidak ditemukan.

---

## 7. Fungsi Display

```python
def display(self):
```

Fungsi untuk menampilkan seluruh data akun.

```python
print("\nData Akun Game:")
```

Menampilkan judul data.

```python
for i in range(self.SIZE):
```

Melakukan perulangan seluruh bucket.

```python
print(f"{i}: ", end="")
```

Menampilkan nomor bucket.

```python
current = self.table[i]
```

Mengambil node pertama.

```python
while current is not None:
```

Melakukan penelusuran linked list.

```python
print(f"({current.key}, {current.value}) -> ", end="")
```

Menampilkan ID Player dan Username.

```python
current = current.next
```

Berpindah ke node berikutnya.

```python
print("NULL")
```

Menandakan akhir linked list.

---

## 8. Fungsi Main

```python
def main():
```

Fungsi utama program.

```python
hashmap = HashMapSeparateChaining()
```

Membuat objek Hash Map.

```python
hashmap.insert(1001, "DragonX")
hashmap.insert(1002, "Shadow")
hashmap.insert(1003, "Raptor")
```

Menambahkan data awal akun game.

```python
pilih = 0
```

Variabel untuk menyimpan pilihan menu.

```python
while pilih != 5:
```

Perulangan menu sampai pengguna memilih keluar.

```python
print("\n=== SISTEM AKUN GAME ONLINE ===")
```

Menampilkan judul program.

```python
print("1. Cari Akun")
print("2. Tambah Akun")
print("3. Hapus Akun")
print("4. Tampilkan Data Akun")
print("5. Keluar")
```

Menampilkan daftar menu.

---

## 9. Menu Cari Akun

```python
if pilih == 1:
```

Menjalankan menu pencarian akun.

```python
id_player = int(input("Masukkan ID Player: "))
```

Meminta pengguna memasukkan ID Player.

```python
hasil = hashmap.search(id_player)
```

Melakukan pencarian data akun.

```python
if hasil is not None:
```

Mengecek apakah akun ditemukan.

```python
print("Username:", hasil.value)
```

Menampilkan username akun.

```python
else:
```

Jika akun tidak ditemukan.

```python
print("Akun tidak ditemukan!")
```

Menampilkan pesan gagal.

---

## 10. Menu Tambah Akun

```python
elif pilih == 2:
```

Menjalankan menu tambah akun.

```python
id_player = int(input("Masukkan ID Player: "))
```

Meminta ID Player baru.

```python
username = input("Masukkan Username: ")
```

Meminta Username baru.

```python
hashmap.insert(id_player, username)
```

Menambahkan akun ke Hash Map.

```python
print("Akun berhasil ditambahkan")
```

Menampilkan pesan berhasil.

---

## 11. Menu Hapus Akun

```python
elif pilih == 3:
```

Menjalankan menu hapus akun.

```python
id_player = int(input("Masukkan ID Player yang akan dihapus: "))
```

Meminta ID Player yang akan dihapus.

```python
if hashmap.remove_key(id_player):
```

Melakukan proses penghapusan.

```python
print("Akun berhasil dihapus")
```

Menampilkan pesan berhasil.

```python
else:
```

Jika akun tidak ditemukan.

```python
print("Akun tidak ditemukan")
```

Menampilkan pesan gagal.

---

## 12. Menu Tampilkan Data Akun

```python
elif pilih == 4:
```

Menjalankan menu tampilkan data akun.

```python
hashmap.display()
```

Menampilkan seluruh data akun yang tersimpan.

---

## 13. Menjalankan Program

```python
if __name__ == "__main__":
```

Digunakan untuk memastikan file dijalankan sebagai program utama.

```python
main()
```

Menjalankan fungsi utama program.
