""" IDENTITAS """
# Nama: Muhammad Zulfa Fauzan Nurhuda
# NIM: 19624258
# Tanggal: 31 Oktober 2024

""" KETERANGAN PROGRAM """
# PROGRAM <Menentukan Luas Tanah Minimum Untuk Membangun Rumah>
# Menentukan luas tanah minimum untuk membangun rumah berdasarkan nilai n dari data input.

# KAMUS | DICTIONARY
# banyak_data: integer
# data: array[integer]
# minimum: integer
# dipilih: integer
# i: integer (terdapat pada 3x pengulangan, line 22, line 28, dan line 37)

""" ALGORITMA PROGRAM """
# INPUT BANYAK TANAH YANG AKAN DIMASUKKAN KE DALAM DATA
banyak_data = int(input("Masukkan banyak data: "))

# INPUT DATA LUAS TANAH BERDASARKAN BANYAK TANAH YANG ADA
data = [int(input(f"Masukkan luas tanah ke-{i + 1}: ")) for i in range(banyak_data)]

# INPUT MINIMUM LUAS TANAH UNTUK MEMBANGUN RUMAH
minimum = int(input("Tentukan luas tanah minimum: "))

# SORTING ARRAY, AGAR TERURUT DARI KECIL KE BESAR
for i in range(1, banyak_data):
    for j in range(0, banyak_data - 1):
        if (data[j] > data[j + 1]):
            data[j], data[j + 1] = data[j + 1], data[j]

# INISIALISASI TANAH YANG DIPILIH
dipilih = 0

# LAKUKAN PENGULANGAN UNTUK MENENTUKAN TANAH TERKECIL YANG LEBIH BESAR SAMA DENGAN MINIMUM
for i in data:
    if (dipilih == 0):
        if (i >= minimum):
            dipilih += i

# KONDISIONAL, MENENTUKAN APAKAH ADA TANAH YANG DIPILIH, APABILA TIDAK ADA (0), MAKA TIDAK
if (dipilih > 0):
    print(f"Luas tanah terkecil yang dapat dipilih adalah {dipilih}.")
else:
    print("Tuan Leo tidak dapat membangun rumah.")