""" IDENTITAS """
# Nama: Muhammad Zulfa Fauzan Nurhuda
# NIM: 19624258
# Tanggal: 31 Oktober 2024

""" KETERANGAN PROGRAM """
# PROGRAM <Menentukan Pengunjung Yang Bisa Mendapat Konsumsi>
# Menentukan pengunjung mana yang bisa dan tidak untuk mendapat konsumsi, dan mencatat berapa pengunjung yang mendapat konsumsi dan berapa yang mencoba lebih dari satu.

# KAMUS | DICTIONARY
# stop: boolean
# data_tiket: array[string]
# lebih_dari_satu: array[string]
# nomor_tiket: string
# total_konsumsi: integer
# total_lebih_dari_satu: integer
# _: string (terdapat pada 2x pengulangan, line 49 dan line 56)

""" ALGORITMA PROGRAM """
# INISIALISASI ARRAY DATA TIKET DAN DATA LEBIH DARI SATU
data_tiket = []
lebih_dari_satu = []

# INISIALISASI STOP, UNTUK MENENTUKAN APAKAH ITERASI SUDAH HARUS STOP ATAU BELUM (KARENA TIDAK DIPERBOLEHKAN MENGGUNAKAN BREAK)
stop = False

# PENGULANGAN UNTUK MEMASTIKAN NOMOR TIKET SUDAH PERNAH MENDAPAT KONSUMSI ATAU BELUM
while not stop:
    nomor_tiket = str(input("Masukkan nomor tiket pengunjung: "))

    # KONDISIONAL, XXX UNTUK KELUAR PENGULANGAN
    if (nomor_tiket == "XXX"):
        stop = True

    # JIKA BUKAN XXX, PROSES NOMOR TIKET
    else:
        if (nomor_tiket not in data_tiket):
            print("Pengunjung tersebut bisa mendapat konsumsi.")
            data_tiket += [nomor_tiket]
        elif (nomor_tiket in data_tiket):
            print("Pengunjung tersebut tidak bisa mendapat konsumsi lagi.")
            if (nomor_tiket not in lebih_dari_satu):
                lebih_dari_satu += [nomor_tiket]

# INISIALISASI TOTAL PENGUNJUNG YANG MENDAPAT KONSUMSI
total_konsumsi = 0

# PENGULANGAN UNTUK MENENTUKAN PENGUNJUNG YANG MENDAPAT KONSUMSI
for _ in data_tiket:
    total_konsumsi += 1

# INISIALISASI TOTAL PENGUNJUNG YANG MENCOBA LEBIH DARI SATU KALI
total_lebih_dari_satu = 0

# PENGULANGAN UNTUK MENENTUKAN PENGUNJUNG YANG MENCOBA LEBIH DARI SATU KALI
for _ in lebih_dari_satu:
    total_lebih_dari_satu += 1

# BERIKAN KELUARAN DATA TOTAL PENGUNJUNG YANG MENDAPAT KONSUMSI
print(f"Total pengunjung yang mendapat konsumsi: {total_konsumsi}")

# APABILA ADA YANG MENCOBA LEBIH DARI SEKALI, BERIKAN KELUARAN DATANYA
if (total_lebih_dari_satu > 0):
    print(f"Total pengunjung yang mencoba mendapat konsumsi lebih dari satu kali: {total_lebih_dari_satu}")