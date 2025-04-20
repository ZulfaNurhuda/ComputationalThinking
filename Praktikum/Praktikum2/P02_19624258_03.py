""" IDENTITAS """
# Nama: Muhammad Zulfa Fauzan Nurhuda
# NIM: 19624258
# Tanggal: 31 Oktober 2024

""" KETERANGAN PROGRAM """
# PROGRAM <Kemungkinan ID Pengguna>
# Menentukan kemungkinan id pengguna berdasarkan faktor prima nomor urut dan dibatasi oleh [batas atas, batas bawah]

# KAMUS | DICTIONARY
# nomor_urut: integer
# batas_bawah: integer
# batas_atas: integer
# faktor prima: array[integer]
# id_pengguna: array[integer]
# banyak_kemungkinan_id: integer
# i: integer (terdapat pada 2x pengulangan, line 35 dan line 49)
# _: integer (terdapat pada 1x pengulangan, line 59)

""" ALGORITMA PROGRAM """
# INPUT NOMOR URUT, BATAS BAWAH, DAN BATAS ATAS
nomor_urut = int(input("Masukkan Nomor Urut: "))
batas_bawah = int(input("Masukkan batas bawah (x): "))
batas_atas = int(input("Masukkan batas atas (y): "))

# INISIALISASI ARRAY FAKTOR PRIMA
faktor_prima = []

# CEK FAKTOR PRIMA 2
if nomor_urut % 2 == 0:
    faktor_prima += [2]
    while nomor_urut % 2 == 0:
        nomor_urut //= 2

# CEK FAKTOR PRIMA YANG GANJIL DIMULAI DARI 3, 5, 7 ... DST
for i in range(3, int(nomor_urut ** 0.5) + 1, 2):
    if nomor_urut % i == 0:
        faktor_prima += [i]
        while nomor_urut % i == 0:
            nomor_urut //= i

# JIKA SISA NYA LEBIH BESAR DARI 2, MAKA DIHITUNG SEBAGAI FAKTOR PRIMA
if (nomor_urut > 2):
    faktor_prima += [nomor_urut]

# INISIALISASI ARRAY ID PENGGUNA
id_pengguna = []

# PENGULANGAN UNTUK MEMASTIKAN VALIDASI ID PENGGUNA DARI FAKTOR PRIMA YANG TERSEDIA
for i in range(batas_bawah, batas_atas + 1):
    for faktor in faktor_prima:
        if (i % faktor == 0):
            id_pengguna += [i]

# INISIALISASI KEMUNGKINAN ID PENGGUNA
banyak_kemungkinan_id = 0

# PENGULANGAN UNTUK MENCARI TOTAL BANYAK KEMUNGKINAN ID PENGGUNA
for _ in id_pengguna:
    banyak_kemungkinan_id += 1

# KONDISIONAL, APABILA BANYAK KEMUNGKINAN ID LEBIH DARI 0, MAKA CETAK KEMUNGKINAN ID PENGGUNA
if (banyak_kemungkinan_id > 0):
    print(f"Id Pengguna yang valid = {id_pengguna}")
else:
    print("Tidak ada Id Pengguna yang valid.")