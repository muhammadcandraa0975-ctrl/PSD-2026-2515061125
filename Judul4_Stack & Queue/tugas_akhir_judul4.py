#Implementasi Queue Array pada Sistem Antrian Pasien Klinik
class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Antrian penuh")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"Pasien {x} berhasil masuk antrian")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print(f"Pasien {self.q[self.front_idx]} dipanggil")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print(f"Pasien terdepan: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print("Daftar antrian pasien: ", end="")
        i = self.front_idx
        while True:
            print(self.q[i], end=" ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()


def main():
    queue = QueueArray()
    pilih = 0
    while pilih != 5:
        print("\n=== SISTEM ANTRIAN PASIEN ===")
        print("1. Tambah Pasien")
        print("2. Panggil Pasien")
        print("3. Lihat Antrian Depan")
        print("4. Tampilkan Antrian")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            nama = input("Masukkan nama pasien: ")
            queue.enqueue(nama)
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()