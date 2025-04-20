""" IDENTITAS """
# Nama: Muhammad Zulfa Fauzan Nurhuda
# NIM: 19624258
# Tanggal: 17 Oktober 2024

""" KETERANGAN PROGRAM """
# PROGRAM <Menentukan Kelulusan>
# Menentukan kelulusan dengan rata-rata 3 nilai kuis

# KAMUS | DICTIONARY
# kuis_1: integer
# kuis_2: integer
# kuis_3: integer
# rata_rata: integer

""" ALGORITMA PROGRAM """
# INPUT NILAI KUIS 1, KUIS 2, DAN KUIS 3
kuis_1 = int(input("Masukkan nilai kuis pertama: "))
kuis_2 = int(input("Masukkan nilai kuis kedua: "))
kuis_3 = int(input("Masukkan nilai kuis ketiga: "))

# MENGHITUNG RATA-RATA 3 KUIS
rata_rata = (kuis_1 + kuis_2 + kuis_3) / 3

# MENGANALISIS RATA-RATA NILAI DAN PREDIKATNYA
if (rata_rata >= 80):
    print("Tuan Leo mendapatkan nilai Lulus Memuaskan.")
elif (80 > rata_rata >= 70):
    print("Tuan Leo mendapatkan nilai Lulus.")
else:
    print("Tuan Leo mendapatkan nilai Tidak Lulus.")