# Judul Program
Implementasi Binary Search Tree (BST) pada Sistem Nomor Antrian Bank
# Deskripsi Singkat
Program ini dibuat untuk mensimulasikan sistem nomor antrian pada bank menggunakan struktur data Binary Search Tree (BST). Pada program ini, pengguna dapat menambahkan nomor antrian, menghapus nomor antrian, menampilkan daftar nomor antrian, mencari nomor setelahnya (successor), serta mencari nomor sebelumnya (predecessor).

Binary Search Tree (BST) merupakan struktur data pohon biner yang menyimpan data secara terurut. Data yang memiliki nilai lebih kecil akan ditempatkan di subtree kiri, sedangkan data yang lebih besar ditempatkan di subtree kanan. Dengan metode tersebut, proses pencarian, penambahan, dan penghapusan data dapat dilakukan dengan lebih mudah dan terstruktur.

Program ini juga menggunakan traversal level-order untuk menampilkan seluruh nomor antrian. Selain itu, program memanfaatkan percabangan, perulangan, dan validasi input agar program dapat berjalan dengan baik serta mengurangi terjadinya error saat digunakan.

---

## Source Code dan Penjelasan

### 1. Membuat Class Node

```python
class Node:
```

Bagian ini digunakan untuk membuat class `Node` sebagai tempat penyimpanan data pada Binary Search Tree.

```python
def __init__(self, nomor):
```

Constructor ini dijalankan saat node baru dibuat.

```python
self.nomor = nomor
```

Digunakan untuk menyimpan nomor antrian pada node.

```python
self.left = None
```

Digunakan untuk menyimpan child kiri.

```python
self.right = None
```

Digunakan untuk menyimpan child kanan.

---

### 2. Membuat Class BST

```python
class BSTNomorAntrian:
```

Bagian ini digunakan untuk membuat class utama Binary Search Tree.

```python
def __init__(self):
```

Constructor class BST.

```python
self.root = None
```

Digunakan untuk menyimpan root atau akar pohon BST.

---

### 3. Fungsi Insert Node

```python
def insert_node(self, root, nomor):
```

Fungsi ini digunakan untuk menambahkan node baru ke dalam BST.

```python
if root is None:
```

Mengecek apakah posisi node masih kosong.

```python
return Node(nomor)
```

Jika kosong, maka dibuat node baru.

```python
if nomor < root.nomor:
```

Mengecek apakah nomor lebih kecil dari root.

```python
root.left = self.insert_node(root.left, nomor)
```

Jika lebih kecil, data dimasukkan ke subtree kiri.

```python
elif nomor > root.nomor:
```

Mengecek apakah nomor lebih besar dari root.

```python
root.right = self.insert_node(root.right, nomor)
```

Jika lebih besar, data dimasukkan ke subtree kanan.

```python
return root
```

Mengembalikan root BST.

---

### 4. Fungsi Insert

```python
def insert(self, nomor):
```

Fungsi ini digunakan untuk memanggil proses insert node.

```python
self.root = self.insert_node(self.root, nomor)
```

Menambahkan data ke BST mulai dari root.

---

### 5. Fungsi Mencari Node Minimum

```python
def find_min_node(self, root):
```

Fungsi ini digunakan untuk mencari node dengan nilai terkecil.

```python
current = root
```

Variabel `current` digunakan untuk penelusuran node.

```python
while current is not None and current.left is not None:
```

Perulangan dilakukan selama masih ada child kiri.

```python
current = current.left
```

Berpindah terus ke kiri untuk mencari nilai terkecil.

```python
return current
```

Mengembalikan node minimum.

---

### 6. Fungsi Delete Node

```python
def delete_node(self, root, nomor):
```

Fungsi ini digunakan untuk menghapus node dari BST.

```python
if root is None:
```

Mengecek apakah node kosong.

```python
return None
```

Jika kosong, fungsi berhenti.

```python
if nomor < root.nomor:
```

Mengecek apakah nomor lebih kecil dari root.

```python
root.left = self.delete_node(root.left, nomor)
```

Jika lebih kecil, pencarian dilakukan ke subtree kiri.

```python
elif nomor > root.nomor:
```

Mengecek apakah nomor lebih besar dari root.

```python
root.right = self.delete_node(root.right, nomor)
```

Jika lebih besar, pencarian dilakukan ke subtree kanan.

```python
if root.left is None and root.right is None:
```

Mengecek apakah node adalah leaf.

```python
return None
```

Jika leaf, node langsung dihapus.

```python
elif root.left is None:
```

Mengecek apakah child kiri kosong.

```python
return root.right
```

Menggantikan node dengan child kanan.

```python
elif root.right is None:
```

Mengecek apakah child kanan kosong.

```python
return root.left
```

Menggantikan node dengan child kiri.

```python
successor = self.find_min_node(root.right)
```

Mencari successor dari subtree kanan.

```python
root.nomor = successor.nomor
```

Mengganti data node dengan successor.

```python
root.right = self.delete_node(root.right, successor.nomor)
```

Menghapus node successor lama.

```python
return root
```

Mengembalikan root BST.

---

### 7. Fungsi Delete

```python
def delete(self, nomor):
```

Fungsi untuk memanggil proses delete.

```python
self.root = self.delete_node(self.root, nomor)
```

Menghapus node dari BST.

---

### 8. Fungsi Level Order

```python
def level_order(self, root):
```

Fungsi ini digunakan untuk menampilkan isi BST secara level-order.

```python
if root is None:
```

Mengecek apakah BST kosong.

```python
print("(kosong)")
```

Menampilkan pesan jika BST kosong.

```python
queue = []
```

Membuat queue sementara.

```python
queue.append(root)
```

Memasukkan root ke queue.

```python
while len(queue) > 0:
```

Perulangan dilakukan selama queue masih berisi data.

```python
current = queue.pop(0)
```

Mengambil data paling depan dari queue.

```python
print(current.nomor, end=" ")
```

Menampilkan nomor antrian.

```python
if current.left is not None:
```

Mengecek child kiri.

```python
queue.append(current.left)
```

Memasukkan child kiri ke queue.

```python
if current.right is not None:
```

Mengecek child kanan.

```python
queue.append(current.right)
```

Memasukkan child kanan ke queue.

```python
print()
```

Membuat baris baru agar output rapi.

---

### 9. Fungsi Successor

```python
def find_successor(self, root, nomor):
```

Fungsi ini digunakan untuk mencari nomor setelahnya.

```python
current = root
```

Variabel `current` digunakan untuk penelusuran.

```python
successor = None
```

Variabel untuk menyimpan successor.

```python
while current is not None:
```

Perulangan pencarian node.

```python
if nomor < current.nomor:
```

Mengecek apakah nomor lebih kecil.

```python
successor = current
```

Node saat ini menjadi kandidat successor.

```python
current = current.left
```

Berpindah ke subtree kiri.

```python
elif nomor > current.nomor:
```

Mengecek apakah nomor lebih besar.

```python
current = current.right
```

Berpindah ke subtree kanan.

```python
break
```

Menghentikan pencarian jika node ditemukan.

```python
if current.right is not None:
```

Mengecek apakah memiliki subtree kanan.

```python
successor = self.find_min_node(current.right)
```

Mencari nilai minimum di subtree kanan.

```python
return successor.nomor, True
```

Mengembalikan successor.

---

### 10. Fungsi Predecessor

```python
def find_predecessor(self, root, nomor):
```

Fungsi ini digunakan untuk mencari nomor sebelumnya.

```python
predecessor = None
```

Variabel untuk menyimpan predecessor.

```python
if nomor > current.nomor:
```

Mengecek apakah nomor lebih besar.

```python
predecessor = current
```

Node saat ini menjadi kandidat predecessor.

```python
current = current.right
```

Berpindah ke subtree kanan.

```python
elif nomor < current.nomor:
```

Mengecek apakah nomor lebih kecil.

```python
current = current.left
```

Berpindah ke subtree kiri.

```python
while temp.right is not None:
```

Mencari node terbesar di subtree kiri.

```python
temp = temp.right
```

Berpindah ke kanan terus menerus.

```python
return predecessor.nomor, True
```

Mengembalikan predecessor.

---

### 11. Fungsi Main

```python
def main():
```

Fungsi utama program.

```python
bst = BSTNomorAntrian()
```

Membuat objek BST.

```python
pilih = 0
```

Variabel untuk menyimpan pilihan menu.

```python
while pilih != 6:
```

Perulangan menu sampai pengguna memilih keluar.

```python
print("\n=== BST NOMOR ANTRIAN BANK ===")
```

Menampilkan judul program.

```python
print("1. Tambah Nomor Antrian")
print("2. Hapus Nomor Antrian")
print("3. Tampilkan Nomor Antrian")
print("4. Cari Nomor Setelahnya")
print("5. Cari Nomor Sebelumnya")
print("6. Keluar")
```

Menampilkan daftar menu program.

```python
pilih = int(input("Pilih: "))
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

---

### 12. Pilihan Menu

```python
if pilih == 1:
```

Menu tambah nomor antrian.

```python
x = int(input("Masukkan nomor antrian: "))
```

Meminta input nomor antrian.

```python
bst.insert(x)
```

Menambahkan nomor ke BST.

```python
elif pilih == 2:
```

Menu hapus nomor antrian.

```python
bst.delete(x)
```

Menghapus nomor dari BST.

```python
elif pilih == 3:
```

Menu tampilkan nomor antrian.

```python
bst.level_order(bst.root)
```

Menampilkan isi BST.

```python
elif pilih == 4:
```

Menu mencari successor.

```python
ans, found = bst.find_successor(bst.root, x)
```

Mencari nomor setelahnya.

```python
elif pilih == 5:
```

Menu mencari predecessor.

```python
ans, found = bst.find_predecessor(bst.root, x)
```

Mencari nomor sebelumnya.

```python
elif pilih == 6:
```

Menu keluar program.

```python
print("Program selesai.")
```

Menampilkan pesan selesai.

---

### 13. Menjalankan Program

```python
if __name__ == "__main__":
```

Digunakan untuk memastikan file dijalankan langsung.

```python
main()
```

Menjalankan fungsi utama program.
