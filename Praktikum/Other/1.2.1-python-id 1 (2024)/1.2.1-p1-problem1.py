""" KETERANGAN PROGRAM """
# +----------------------------------------+
# | PROGRAM <Waktu Pelari>                 |
# +----------------------------------------+
# | Menghitung waktu maksimal untuk pelari |
# | dari 3 kali percobaan lari             |
# +----------------------------------------+

# +---------------+-----------+
# | KAMUS PROGRAM | TIPE DATA |
# +---------------+-----------+
# | waktu_1       | integer   |
# | waktu_2       | integer   |
# | waktu_3       | integer   |
# | waktu_akhir   | integer   |
# +---------------+-----------+

""" ALGORITMA PROGRAM """
# INPUT WAKTU SETIAP WAKTU LARI
waktu_1 = int(input("Masukkan waktu lari pertama: "))
waktu_2 = int(input("Masukkan waktu lari kedua: "))
waktu_3 = int(input("Masukkan waktu lari ketiga: "))

# INISIASI WAKTU AKHIR
waktu_akhir = 0

# PENCABANGAN UNTUK MENGANALISIS WAKTU PALING MAKSIMAL
if (waktu_1 >= waktu_2 >= waktu_3):
    waktu_akhir = (waktu_1 + waktu_2) / 2
elif (waktu_1 >= waktu_3 >= waktu_2):
    waktu_akhir = (waktu_1 + waktu_3) / 2
elif (waktu_2 >= waktu_1 >= waktu_3):
    waktu_akhir = (waktu_2 + waktu_1) / 2
elif (waktu_2 >= waktu_3 >= waktu_1):
    waktu_akhir = (waktu_2 + waktu_3) / 2
elif (waktu_3 >= waktu_1 >= waktu_2 ):
    waktu_akhir = (waktu_3 + waktu_1) / 2
else:
    waktu_akhir = (waktu_3 + waktu_2) / 2

# PRINT KELUARAN WAKTU AKHIR PESERTA
print(f"Waktu akhir peserta adalah {waktu_akhir} detik.")