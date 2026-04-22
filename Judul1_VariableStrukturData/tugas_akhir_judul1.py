def menu():
    print("1. Tampilkan kursi")
    print("2. Pesan kursi")
    print("3. Keluar")

def main():
    kursi = [[0 for _ in range(2)] for _ in range(3)]
    running = True

    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            print("Denah Kursi:")
            for i in range(3):
                for j in range(2):
                    print(kursi[i][j], end=" ")
                print()

        elif choice == 2:
            try:
                i = int(input("Masukkan baris (0-2): "))
                j = int(input("Masukkan kolom (0-1): "))

                if kursi[i][j] == 0:
                    kursi[i][j] = 1
                    print("Kursi berhasil dipesan")
                else:
                    print("Kursi sudah terisi")

            except (ValueError, IndexError):
                print("Input tidak valid!")

        elif choice == 3:
            running = False
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
