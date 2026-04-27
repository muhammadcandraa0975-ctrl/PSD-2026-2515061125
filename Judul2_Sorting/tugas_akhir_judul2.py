def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah siswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    tinggi = []
    print("Masukkan tinggi badan siswa:")

    for i in range(n):
        while True:
            try:
                data = int(input(f"Tinggi siswa ke-{i+1}: "))
                tinggi.append(data)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print(f"Tinggi sebelum diurutkan: {tinggi}")

    bubble_sort(tinggi, n)

    print("Tinggi setelah diurutkan:", end=" ")
    for i in range(n):
        print(tinggi[i], end=" ")
    print()


if __name__ == "__main__":
    main()