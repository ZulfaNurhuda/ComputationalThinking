""" KETERANGAN PROGRAM """
# +----------------------------------------+
# | PROGRAM <Mencari Mobil>                |
# +----------------------------------------+
# | Mencari mobil di dalam bangunan parkir |
# | menggunakan analisis plat nomor,       |
# | jumlah digit, dan banyak digit pada    |
# | plat nomor                             |
# +----------------------------------------+

# +--------------------+-----------+
# | KAMUS              | TIPE DATA |
# +--------------------+-----------+
# | plat_nomor         | string    |
# | jumlah_digit       | integer   |
# | banyak_digit       | integer   |
# | jumlah_digit_mobil | integer   |
# | banyak_digit_mobil | integer   |
# +--------------------+-----------+

# +------------------+-----------+------------------------------------------------+
# | VARIABEL ITERASI | TIPE DATA | KETERANGAN                                     |
# +------------------+-----------+------------------------------------------------+
# | i                | integer   | variabel iterasi, terdapat pada 1x pengulangan |
# | number           | integer   | variabel iterasi, terdapat pada 1x pengulangan |
# +------------------+-----------+------------------------------------------------+

""" ALGORITMA PROGRAM """
# INPUT PLAT NOMOR, JUMLAH DIGIT, DAN BANYAK DIGITNYA
plat_nomor = input("Masukkan nomor plat mobil: ")
jumlah_digit = int(input("Masukkan jumlah digit: "))
banyak_digit = int(input("Masukkan banyak digit: "))

# INISIALISASI STRING BERISI ANGKA 0 - 9
angka = [str(number) for number in range(9)]

# INISIALISASI JUMLAH DIGIT DAN BANYAK DIGIT PLAT NOMOR ASLI
jumlah_digit_mobil = 0
banyak_digit_mobil = 0

# PENGULANGAN UNTUK MENENTUKAN JUMLAH DIGIT DAN BANYAK DIGIT DARI INPUT
for i in plat_nomor:
    # APABILA TERMASUK ANGKA -> MENCEGAH ERROR INTEGER
    if ('0' <= i <= '9'):
        jumlah_digit_mobil += int(i)
        banyak_digit_mobil += 1

# KONDISIONAL, APABILA TIDAK DIAWALI DENGAN D, BERARTI BUKAN MOBILNYA
if (plat_nomor[0] == "D"):
    # KONDISIONAL, APABILA JUMLAH DIGIT DAN BANYAK DIGIT DI INPUT SAMA DENGAN JUMLAH DIGIT DAN BANYAK DIGIT PLAT NOMOR ASLI
    if (jumlah_digit == jumlah_digit_mobil and banyak_digit == banyak_digit_mobil):
        print("Mobil Tuan Leo ditemukan!")
    else:
        print("Bukan mobil Tuan Leo!")
else:
    print("Bukan mobil Tuan Leo!")