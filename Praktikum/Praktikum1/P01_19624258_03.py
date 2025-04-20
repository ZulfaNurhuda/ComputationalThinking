""" IDENTITAS """
# Nama: Muhammad Zulfa Fauzan Nurhuda
# NIM: 19624258
# Tanggal: 17 Oktober 2024

""" KETERANGAN PROGRAM """
# PROGRAM <Memperbaiki Angka Tertukar>
# Memperbaiki angka yang tertukar dengan input posisi angka yang harus ditukar, dengan metode typecasting

# KAMUS | DICTIONARY
# digit_harga: integer
# harga: integer
# angka_tukar_1: integer
# angka_tukar_2: integer
# string_harga: string
# angka_fix: integer

""" ALGORITMA PROGRAM """
# INPUT DIGIT HARGA
digit_harga = int(input("Masukkan jumlah digit harga: "))

# INPUT HARGA BARANG
harga = int(input("Masukkan harga: "))

# INPUT 2 ANGKA YANG AKAN DITUKAR
angka_tukar_1 = int(input("Masukkan posisi angka pertama yang akan ditukar: "))
angka_tukar_2 = int(input("Masukkan posisi angka kedua yang akan ditukar: "))

# VALIDASI APAKAH HARGA SESUAI DENGAN DIGIT HARGA
if (10 ** (digit_harga - 1) <= harga < 10 ** digit_harga):
    # MENGUBAH INTEGER MENJADI STRING AGAR BISA MENGGUNAKAN METODE TYPECASTING
    string_harga = str(harga)

    # MENGUBAH POSISI ANGKA YANG SALAH
    angka_fix = int(string_harga[:angka_tukar_1-1] + string_harga[angka_tukar_2-1] + string_harga[angka_tukar_1:angka_tukar_2-1] + string_harga[angka_tukar_1-1] + string_harga[angka_tukar_2:])

    # PRINT KELUARAN HASIL ANGKA YANG SUDAH DIPERBAIKI
    print("Harga setelah diperbaiki : " + str(angka_fix))

# APABILA HARGA TIDAK SESUAI DENGAN DIGIT, INFORMASIKAN
else:
    print("Masukan harga tidak valid")