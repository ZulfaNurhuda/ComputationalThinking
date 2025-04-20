""" KETERANGAN PROGRAM """
# +--------------------------------------- +
# | PROGRAM <Poin Pelari>                  |
# +--------------------------------------- +
# | Menentukan poin dan waktu total pelari |
# | dalam 3 kali kesempatan                |
# +--------------------------------------- +

# +---------------+-----------+
# | KAMUS PROGRAM | TIPE DATA |
# +---------------+-----------+
# | waktu_tahap_1 | integer   |
# | waktu_tahap_2 | integer   |
# | waktu_tahap_3 | integer   |
# | waktu_total   | integer   |
# | batas_1       | integer   |
# | batas_2       | integer   |
# | batas_3       | integer   |
# | poin_total    | integer   |
# +---------------+-----------+

""" ALGORITMA PROGRAM """
# INPUT WAKTU SETIAP TAHAP
waktu_tahap_1 = int(input("Masukkan waktu tahap 1 (menit): "))
waktu_tahap_2 = int(input("Masukkan waktu tahap 2 (menit): "))
waktu_tahap_3 = int(input("Masukkan waktu tahap 3 (menit): "))

# HITUNG WAKTU TOTAL
waktu_total = waktu_tahap_1 + waktu_tahap_2 + waktu_tahap_3

# INISIASI BATAS
batas_1 = 15
batas_2 = 15
batas_3 = 15

# HITUNG POIN TOTAL
poin_total = 45 - waktu_tahap_1 - waktu_tahap_2 - waktu_tahap_3

# APABILA TAHAP 1 KURANG DARI 5 MENIT MAKA BATAS TAHAP 2 BERTAMBAH 2 MENIT
if (waktu_tahap_1 < 5):
    batas_2 += 2

# APABILA TAHAP 2 KURANG DARI 5 MENIT MAKA BATAS TAHAP 3 BERTAMBAH 2 MENIT
if (waktu_tahap_2 < 5):
    batas_3 += 2

# APABILA WAKTU TOTAL DIBAWAH 30 MENIT, POIN BERTAMBAH 10
if (waktu_total < 30):
    poin_total += 10

# APABILA SALAH SATU TAHAP LEBIH DARI BATAS WAKTU, MAKA GUGUR DENGAN 0 POIN
if (waktu_tahap_1 > batas_1):
    waktu_total = waktu_tahap_1
    poin_total = 0
elif (waktu_tahap_2 > batas_2):
    waktu_total = waktu_tahap_1 + waktu_tahap_2
    poin_total = 0
elif (waktu_tahap_3 > batas_3):
    poin_total = 0

# PRINT KELUARAN TOTAL WAKTU DAN TOTAL POIN
print(f"Total waktu yang dihabiskan adalah {waktu_total} menit Poin yang didapatkan adalah {poin_total}.")