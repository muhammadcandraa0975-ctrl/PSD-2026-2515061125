def sequential_search(data, n, target):
    i = 0
    counter = 0

    while i < n:
        if data[i].lower() == target.lower():
            counter += 1
        i += 1

    return counter


def main():
    data = ["Zaidan", "Zizo", "Nayla", "Nino", "Evan", "Dimas", "Nino", "Reza"]
        
    n = len(data)

    print(f"Daftar peserta seminar: {data}")

    while True:
        target = input("Masukkan nama peserta yang ingin dicari: ")

        if target.strip() != "":
            break
        else:
            print("Input tidak boleh kosong!")

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Nama {target} ditemukan sebanyak {counter} kali.")
    else:
        print(f"Nama {target} tidak ditemukan.")


if __name__ == "__main__":
    main()