""" IDENTITAS """
# Nama: Muhammad Zulfa Fauzan Nurhuda
# NIM: 19624258
# Tanggal: 07 Desember 2024

""" KETERANGAN PROGRAM """
# PROGRAM <Mencari Jumlah>
# Mencari jumlah dari f(x) -> faktor prima terbesar dari x, dengan interval ditentukan oleh [m, n]

# KAMUS | DICTIONARY
# m: integer
# n: integer
# hasil_total: integer
# (Variabel fungsi/prosedur dapat dilihat di masing masing variabel lokal fungsi/prosedur)

""" ALGORITMA PROGRAM """
def apakahPrima(nomor):
    """ Keterangan: [FUNGSI] apakahPrima """
    # FUNGSI <Menentukan apakah bilangan prima>
    # Menentukan apakah bilangan yang akan dicari merupakan bilangan prima

    # KAMUS LOKAL | LOCAL DICTIONARY
    # (parameter) nomor: integer
    # (variabel iterasi) i: integer

    """ ALGORITMA FUNGSI """
    # Apabila nomor yang dimasukkan dibawah 2, langsung return false
    if nomor < 2:
        return False
    
    # Lakukan iterasi untuk memfilter apakah bilangan tersebut prima
    for i in range(2, int(nomor**0.5) + 1):
        if nomor % i == 0:
            return False
        
    # Apabila berhasil melewati iterasi, berarti bilangan prima
    return True

def cariPrimaTerbesar(nomor):
    """ Keterangan: [FUNGSI] cariPrimaTerbesar """
    # FUNGSI <Menentukan bilangan prima terbesar>
    # Menentukan bilangan prima terbesar dari suatu bilangan

    # KAMUS LOKAL | LOCAL DICTIONARY
    # (parameter) nomor: integer
    # faktor: integer
    # terbesar: integer

    """ ALGORITMA FUNGSI """
    # Apabila nomor yang dimasukkan dibawah 2, langsung return 0, karena tidak ada bilangan primanya
    if nomor < 2:
        return 0

    # Inisialisasi variabel faktor dan variabel terbesar untuk menampung nilai
    faktor = 2
    terbesar = 0

    # Lakukan iterasi dengan while untuk mencari faktor prima terbesar
    while nomor > 1:
        if nomor % faktor == 0:
            if apakahPrima(faktor):
                terbesar = faktor
            nomor //= faktor
        else:
            faktor += 1
    
    # Return bilangan prima terbesar bilangan tersebut
    return terbesar

def jumlahkanFaktorPrima(m, n):
    """ Keterangan: [FUNGSI] jumlahkanFaktorPrima """
    # FUNGSI <Menjumlahkan faktor prima terbesar>
    # Mencari jumlah faktor prima terbesar dengan interval ditentukan oleh [m, n]

    # KAMUS LOKAL | LOCAL DICTIONARY
    # (parameter) m: integer
    # (parameter) n: integer
    # total: integer
    # (variabel iterasi) i: integer

    """ ALGORITMA FUNGSI """
    # Inisialisasi total sebagai 0
    total = 0

    # Lakukan iterasi dengan batas interval [m, n], kemudian jumlahkan faktor prima terbesarnya
    for i in range(m, n+1):
        total += cariPrimaTerbesar(i)

    # Return total dari semua faktor prima terbesar dalam interval [m, n]
    return total

# Masukkan pengguna untuk nilai m dan n sebagai batas interval
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

# Tentukan hasil total dengan fungsi jumlahkanFaktorPrima
hasil_total = jumlahkanFaktorPrima(m, n)

# Print informasi hasil total jumlah faktor prima terbesar
print(f"Jumlah faktor prima terbesar adalah {hasil_total}.")