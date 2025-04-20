""" KETERANGAN PROGRAM """
# +-------------------------------------------------------+
# | PROGRAM <Mencetak Kata Dengan Informasi Penting>      |
# +-------------------------------------------------------+
# | Mencetak kata dengan syarat:                          |
# | 1. Kata adalah yang paling banyak frekuensi muncul    |
# | 2. Kata adalah palindrom (KAKAK = KAKAK saat dibalik) |
# +-------------------------------------------------------+

# +--------------------+--------------+
# | KAMUS PROGRAM      | TIPE DATA    |
# +--------------------+--------------+
# | jumlah_kata        | integer      |
# | teks               | string       |
# | kata_dicari        | string       |
# | teks_array         | list[string] |
# | per_kata           | string       |
# | jumlah_kata_dicari | integer      |
# | kata               | string       |
# | panjang_kata       | integer      |
# | kata_dibalik       | string       |
# | max_frekuensi      | string       |
# | informasi_penting  | string       |
# +--------------------+--------------+

# +------------------+-----------+------------------------------------------------+
# | VARIABEL ITERASI | TIPE DATA | KETERANGAN                                     |
# +------------------+-----------+------------------------------------------------+
# | _                | string    | variabel iterasi, terdapat pada 1x pengulangan |
# | i                | integer   | variabel iterasi, terdapat pada 1x pengulangan |
# | huruf            | string    | variabel iterasi, terdapat pada 2x pengulangan |
# | kata             | string    | variabel iterasi, terdapat pada 3x pengulangan |
# +------------------+-----------+------------------------------------------------+

def frekuensiKata(teks: str, kata_dicari: str) -> int:
    """ Keterangan: `[FUNGSI] frekuensiKata` """
    # +-----------------------------------------------+
    # | FUNGSI <Mencari Frekuensi Kemunculan>         |
    # +-----------------------------------------------+
    # | Mencari frekuensi kemunculan kata dari        |
    # | sebuah teks yang didapat dari input pengguna. |
    # +-----------------------------------------------+

    # +--------------------+--------------+
    # | KAMUS LOKAL        | TIPE DATA    |
    # +--------------------+--------------+
    # | teks               | string       |
    # | kata_dicari        | string       |
    # | teks_array         | list[string] |
    # | per_kata           | string       |
    # | jumlah_kata_dicari | integer      |
    # | huruf              | string       |
    # | kata               | string       |
    # +--------------------+--------------+

    """ ALGORITMA FUNGSI """
    # MENGURAIKAN TEKS MENJADI ARRAY YANG BERISI MASING MASING KATA DALAM TEKS
    # [NOTE] ALTERNATIF GUNAKAN teks_array = teks.split(" ") UNTUK MENGURAI KATA MENJADI ARRAY
    teks_array = []
    per_kata = ""
    for huruf in (teks + " "):
        if huruf != " ":
            per_kata += huruf
        else:
            teks_array += [per_kata]
            per_kata = ""

    # MENCARI JUMLAH KATA YANG DICARI DIDALAM TEKS
    jumlah_kata_dicari = 0
    for kata in teks_array:
        if kata == kata_dicari:
            jumlah_kata_dicari += 1

    # KEMBALIKAN HASIL FUNGSI
    return jumlah_kata_dicari

def isPalindrom(kata: str) -> bool:
    """ Keterangan: `[FUNGSI] isPalindrom` """
    # +-------------------------------------+
    # | FUNGSI <Menentukan Palindrom>       |
    # +-------------------------------------+
    # | Menentukan apakah suatu kata adalah |
    # | palindrom atau bukan.               |
    # | Palindrom adalah kata yang apabila  |
    # | dibalik urutan hurufnya akan tetap  |
    # | terbaca sama.                       |
    # +-------------------------------------+

    # +--------------+-----------+
    # | KAMUS LOKAL  | TIPE DATA |
    # +--------------+-----------+
    # | kata         | string    |
    # | panjang_kata | integer   |
    # | kata_dibalik | string    |
    # +--------------+-----------+
    
    # +-------------------+-----------+------------------------------------------------+
    # | VARIABEL ITERASI  | TIPE DATA | KETERANGAN                                     |
    # +-------------------+-----------+------------------------------------------------+
    # | _                 | string    | variabel iterasi, terdapat pada 1x pengulangan |
    # | i                 | integer   | variabel iterasi, terdapat pada 1x pengulangan |
    # +-------------------+-----------+------------------------------------------------+

    """ ALGORITMA FUNGSI """
    # MENCARI PANJANG KATA YANG DIGUNAKAN UNTUK ITERASI
    # [NOTE] ALTERNATIF MENGGUNAKAN panjang_kata = len(kata) UNTUK MENCARI PANJANG STRING KATA
    panjang_kata = 0
    for _ in kata:
        panjang_kata += 1

    # MEMBALIK URUTAN KATA DENGAN ITERASI MUNDUR
    kata_dibalik = ""
    for i in range(panjang_kata - 1, -1, -1):
        kata_dibalik += kata[i]

    # KEMBALIKAN HASIL FUNGSI (HASIL COMPARE KATA DAN KATA YANG TELAH DIBALIK)
    return kata == kata_dibalik

def cetakKata(teks: str) -> None:
    """ Keterangan: `[PROSEDUR] cetakKata` """
    # +------------------------------------+
    # | PROSEDUR <Mencetak Kata Tertentu>  |
    # +------------------------------------+
    # | Mencetak kata dengan syarat kata   |
    # | tersebut paling banyak muncul atau |
    # | sebuah palindrom.                  |
    # +------------------------------------+

    # +-------------------+--------------+
    # | KAMUS LOKAL       | TIPE DATA    |
    # +-------------------+--------------+
    # | teks              | string       |
    # | teks_array        | list[string] |
    # | per_kata          | string       |
    # | max_frekuensi     | string       |
    # | informasi_penting | string       |
    # +-------------------+--------------+

    # +------------------+-----------+------------------------------------------------+
    # | VARIABEL ITERASI | TIPE DATA | KETERANGAN                                     |
    # +------------------+-----------+------------------------------------------------+
    # | huruf            | string    | variabel iterasi, terdapat pada 1x pengulangan |
    # | kata             | string    | variabel iterasi, terdapat pada 2x pengulangan |
    # +------------------+-----------+------------------------------------------------+

    """ ALGORITMA PROSEDUR """
    # MENGURAIKAN TEKS MENJADI ARRAY YANG BERISI MASING MASING KATA DALAM TEKS
    # [NOTE] ALTERNATIF GUNAKAN teks_array = teks.split(" ") UNTUK MENGURAI KATA MENJADI ARRAY
    teks_array = []
    per_kata = ""
    for huruf in (teks + " "):
        if huruf != " ":
            per_kata += huruf
        else:
            teks_array += [per_kata]
            per_kata = ""

    # MENCARI FREKUENSI KEMUNCULAN MAKSIMAL KATA DALAM TEKS
    max_frekuensi = 0
    for kata in teks_array:
        frekuensi = frekuensiKata(teks, kata)
        if (max_frekuensi < frekuensi):
            max_frekuensi = frekuensi

    # MENCARI INFORMASI PENTING DENGAN 2 SYARAT DALAM PROBLEM
    # 1. KATA ADALAH YANG PALING BANYAK FREKUENSI MUNCUL
    # 2. KATA ADALAH PALINDROM (KAKAK = KAKAK SAAT DIBALIK)
    informasi_penting = ""
    for kata in teks_array:
        if kata not in informasi_penting:
            if frekuensiKata(teks, kata) == max_frekuensi:
                informasi_penting += f"{kata} "
            elif isPalindrom(kata):
                informasi_penting += f"{kata} "

    # PRINT KELUARAN INFORMASI PENTING
    print(informasi_penting)

""" ALGORITMA PROGRAM """
# INPUT JUMLAH KATA DALAM TEKS BESERTA ISI TEKSNYA
jumlah_kata = int(input("Masukkan jumlah kata: ")) # [NOTE] GUA RASA INI GA PENTING, JADI MASUKIN NGASAL JUGA GAPAPA :)
teks = str(input("Masukkan teks: "))

# JALANKAN PROSEDUR UNTUK MENCETAK KATA
cetakKata(teks)

"""
[NOTE] CATATAN PENTING:
Sepertinya bagian input `Masukkan jumlah kata: ...` itu kurang penting,
karena tidak terpakai sama sekali di programnya. (Koreksi kalau salah)
"""