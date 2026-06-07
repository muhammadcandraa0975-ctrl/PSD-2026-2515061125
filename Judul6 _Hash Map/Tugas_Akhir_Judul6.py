class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)

        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return

            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)

        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current

            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)

        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:

                if prev is None:
                    self.table[index] = current.next

                else:
                    prev.next = current.next

                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\nData Akun Game:")

        for i in range(self.SIZE):
            print(f"{i}: ", end="")

            current = self.table[i]

            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()

    hashmap.insert(1001, "DragonX")
    hashmap.insert(1002, "Shadow")
    hashmap.insert(1003, "Raptor")

    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM AKUN GAME ONLINE ===")
        print("1. Cari Akun")
        print("2. Tambah Akun")
        print("3. Hapus Akun")
        print("4. Tampilkan Data Akun")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                id_player = int(input("Masukkan ID Player: "))

                hasil = hashmap.search(id_player)

                if hasil is not None:
                    print("Username:", hasil.value)
                else:
                    print("Akun tidak ditemukan!")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                id_player = int(input("Masukkan ID Player: "))
                username = input("Masukkan Username: ")

                hashmap.insert(id_player, username)

                print("Akun berhasil ditambahkan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            try:
                id_player = int(input("Masukkan ID Player yang akan dihapus: "))

                if hashmap.remove_key(id_player):
                    print("Akun berhasil dihapus")
                else:
                    print("Akun tidak ditemukan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 4:
            hashmap.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()