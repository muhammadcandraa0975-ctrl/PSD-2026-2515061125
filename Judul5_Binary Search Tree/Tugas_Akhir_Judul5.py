class Node:
    def __init__(self, nomor):
        self.nomor = nomor
        self.left = None
        self.right = None


class BSTNomorAntrian:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nomor):
        if root is None:
            return Node(nomor)

        if nomor < root.nomor:
            root.left = self.insert_node(root.left, nomor)

        elif nomor > root.nomor:
            root.right = self.insert_node(root.right, nomor)

        return root

    def insert(self, nomor):
        self.root = self.insert_node(self.root, nomor)

    def find_min_node(self, root):
        current = root

        while current is not None and current.left is not None:
            current = current.left

        return current

    def delete_node(self, root, nomor):
        if root is None:
            return None

        if nomor < root.nomor:
            root.left = self.delete_node(root.left, nomor)

        elif nomor > root.nomor:
            root.right = self.delete_node(root.right, nomor)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                successor = self.find_min_node(root.right)

                root.nomor = successor.nomor

                root.right = self.delete_node(root.right, successor.nomor)

        return root

    def delete(self, nomor):
        self.root = self.delete_node(self.root, nomor)

    def level_order(self, root):
        if root is None:
            print("(kosong)")
            return

        queue = []
        queue.append(root)

        while len(queue) > 0:
            current = queue.pop(0)

            print(current.nomor, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        print()

    def find_successor(self, root, nomor):
        current = root
        successor = None

        while current is not None:
            if nomor < current.nomor:
                successor = current
                current = current.left

            elif nomor > current.nomor:
                current = current.right

            else:
                break

        if current is None:
            return None, False

        if current.right is not None:
            successor = self.find_min_node(current.right)

        if successor is None:
            return None, False

        return successor.nomor, True

    def find_predecessor(self, root, nomor):
        current = root
        predecessor = None

        while current is not None:
            if nomor > current.nomor:
                predecessor = current
                current = current.right

            elif nomor < current.nomor:
                current = current.left

            else:
                break

        if current is None:
            return None, False

        if current.left is not None:
            temp = current.left

            while temp.right is not None:
                temp = temp.right

            predecessor = temp

        if predecessor is None:
            return None, False

        return predecessor.nomor, True


def main():
    bst = BSTNomorAntrian()

    pilih = 0

    while pilih != 6:
        print("\n=== BST NOMOR ANTRIAN BANK ===")
        print("1. Tambah Nomor Antrian")
        print("2. Hapus Nomor Antrian")
        print("3. Tampilkan Nomor Antrian")
        print("4. Cari Nomor Setelahnya")
        print("5. Cari Nomor Sebelumnya")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih: "))

        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                x = int(input("Masukkan nomor antrian: "))
                bst.insert(x)

                print(f"Nomor antrian {x} berhasil ditambahkan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                x = int(input("Hapus nomor antrian: "))
                bst.delete(x)

                print(f"Nomor antrian {x} berhasil dihapus")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("Daftar nomor antrian: ", end="")
            bst.level_order(bst.root)

        elif pilih == 4:
            try:
                x = int(input("Cari nomor setelah: "))

                ans, found = bst.find_successor(bst.root, x)

                if found:
                    print(f"Nomor setelahnya adalah {ans}")

                else:
                    print("Tidak ada nomor setelahnya")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 5:
            try:
                x = int(input("Cari nomor sebelumnya: "))

                ans, found = bst.find_predecessor(bst.root, x)

                if found:
                    print(f"Nomor sebelumnya adalah {ans}")

                else:
                    print("Tidak ada nomor sebelumnya")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 6:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()