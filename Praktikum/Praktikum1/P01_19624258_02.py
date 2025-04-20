""" IDENTITAS """
# Nama: Muhammad Zulfa Fauzan Nurhuda
# NIM: 19624258
# Tanggal: 17 Oktober 2024

""" KETERANGAN PROGRAM """
# PROGRAM <Peserta Terkualifikasi>
# Menentukan banyak peserta terkualifikasi beserta dollar kompeng yang akan diterima

# KAMUS | DICTIONARY
# dollar: integer
# min_waktu: integer
# waktu_leo: integer
# waktu_deb: integer
# waktu_sal: integer
# terkualifikasi: integer
# hadiah_per_orang: integer

""" ALGORITMA PROGRAM """
# INPUT JUMLAH DOLLAR YANG TERSEDIA MENJADI HADIAH
dollar = int(input("Masukkan nilai N: "))

# INPUT MINIMAL WAKTU UNTUK TERKUALIFIKASI
min_waktu = int(input("Masukkan nilai T: "))

# INPUT WAKTU LARI TUAN LEO, NONA DEB, DAN NONA SAL
waktu_leo = int(input("Masukkan waktu lari Tuan Leo: "))
waktu_deb = int(input("Masukkan waktu lari Nona Deb: "))
waktu_sal = int(input("Masukkan waktu lari Nona Sal: "))

# INISIALISASI TERKUALIFIKASI
terkualifikasi = 0

# ANALISIS SIAPA SAJA YANG TERKUALIFIKASI
if (waktu_leo <= min_waktu):
    terkualifikasi += 1
if (waktu_deb <= min_waktu):
    terkualifikasi += 1
if (waktu_sal <= min_waktu):
    terkualifikasi += 1

# APABILA ADA YANG TERKUALIFIKASI
if (terkualifikasi > 0):
    # MENENTUKAN HADIAH PER ORANG
    hadiah_per_orang = int(dollar / terkualifikasi)

    # PRINT KELUARAN INFORMASI JUMLAH PESERTA TERKUALIFIKASI DAN HADIAH PER ORANG
    print(f"Terdapat " + str(terkualifikasi) + " peserta yang terkualifikasi dan masing-masing akan mendapatkan $" + str(hadiah_per_orang) + "dollar kompeng.")

# APABILA TIDAK ADA YANG TERKUALIFIKASI
else:
    print("Tidak ada peserta yang terkualifikasi")