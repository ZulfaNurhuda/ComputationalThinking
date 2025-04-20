""" KETERANGAN PROGRAM """
# +------------------------------------------+
# | PROGRAM <Menentukan Harga Diskon>        |
# +------------------------------------------+
# | Menentukan harga diskon beserta dengan   |
# | mata uang, berdasarkan input pengguna    |
# | dengan memanfaatkan Fungsi dan Prosedur. |
# +------------------------------------------+

# +-------------------+------------- +
# | KAMUS PROGRAM     | TIPE DATA    |
# +-------------------+------------- +
# | kata              | string       |
# | unsur_huruf       | list[string] |
# | alfabet           | string       |
# | huruf_hilang      | string       |
# | data_huruf_unik   | string       |
# | jumlah_huruf_unik | integer      |
# +-------------------+------------- +

# +--------------------+-----------+------------------------------------------------+
# | VARIABEL ITERASI   | TIPE DATA | KETERANGAN                                     |
# +--------------------+-----------+------------------------------------------------+
# | huruf              | string    | variabel iterasi, terdapat pada 2x pengulangan |
# | _                  | string    | variabel iterasi, terdapat pada 1x pengulangan |
# +--------------------+-----------+------------------------------------------------+

def cariHurufHilang(kata: str) -> None:
    """ Keterangan: `[PROSEDUR] cariHurufHilang` """
    # +------------------------------------+
    # | PROSEDUR <Mencari Huruf Hilang>    |
    # +------------------------------------+
    # | Mencari huruf apa saja yang hilang |
    # | berdasarkan kata yang didapat dari |
    # | input pengguna.                    |
    # +------------------------------------+

    # +--------------+-----------+
    # | KAMUS LOKAL  | TIPE DATA |
    # +--------------+-----------+
    # | kata         | string    |
    # | unsur_huruf  | string    |
    # | alfabet      | string    |
    # | huruf_hilang | string    |
    # +--------------+-----------+

    # +------------------+-----------+------------------------------------------------+
    # | VARIABEL ITERASI | TIPE DATA | KETERANGAN                                     |
    # +------------------+-----------+------------------------------------------------+
    # | huruf            | string    | variabel iterasi, terdapat pada 2x pengulangan |
    # +------------------+-----------+------------------------------------------------+

    """ ALGORITMA PROSEDUR """
    # MENCARI HURUF HURUF APA SAJA YANG ADA DALAM KATA TERSEBUT
    unsur_huruf = ""
    for huruf in kata:
        if huruf not in unsur_huruf:
            unsur_huruf += huruf

    # INISIALISASI SEMUA HURUF ALFABET
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    # MENCARI HURUF YANG HILANG DENGAN MEMBANDINGKAN KESELURUHAN DENGAN HURUF HURUF YANG ADA DALAM KATA
    huruf_hilang = ""
    for huruf in alfabet:
        if huruf not in unsur_huruf:
            huruf_hilang += huruf

    # PRINT KELUARAN INFORMASI HURUF APA SAJA YANG HILANG
    print(f"Huruf yang hilang: {huruf_hilang}")

def hitungHurufUnik(kata: str) -> None:
    """ Keterangan: `[PROSEDUR] hitungHurufUnik` """
    # +------------------------------------------+
    # | PROSEDUR <Menghitung Jumlah Huruf Unik>  |
    # +------------------------------------------+
    # | Menghitung jumlah huruf unik berdasarkan |
    # | kata yang didapat dari input pengguna.   |
    # +------------------------------------------+

    # +-------------------+-----------+
    # | KAMUS LOKAL       | TIPE DATA |
    # +-------------------+-----------+
    # | kata              | string    |
    # | data_huruf_unik   | string    |
    # | jumlah_huruf_unik | integer   |
    # +-------------------+-----------+

    # +------------------+-----------+------------------------------------------------+
    # | VARIABEL ITERASI | TIPE DATA | KETERANGAN                                     |
    # +------------------+-----------+------------------------------------------------+
    # | huruf            | string    | variabel iterasi, terdapat pada 1x pengulangan |
    # | _                | string    | variabel iterasi, terdapat pada 1x pengulangan |
    # +------------------+-----------+------------------------------------------------+

    """ ALGORITMA PROSEDUR """
    # MENCARI HURUF UNIK (AGAR TIDAK ADA HURUF YANG TERDUPLIKASI)
    data_huruf_unik = ""
    for huruf in kata:
        if huruf not in data_huruf_unik:
            data_huruf_unik += huruf

    # MENGHITUNG JUMLAH HURUF UNIK
    # [NOTE] ALTERNATIF GUNAKAN jumlah_huruf_unik = len(data_huruf_unik) UNTUK MENCARI PANJANG STRING DATA HURUF UNIK
    jumlah_huruf_unik = 0
    for _ in data_huruf_unik:
        jumlah_huruf_unik += 1

    # PRINT KELUARAN INFORMASI JUMLAH HURUF UNIK
    print(f"Jumlah huruf unik: {jumlah_huruf_unik}")

""" ALGORITMA PROGRAM """
# INPUT KATA
kata = str(input("Masukkan kata: "))

# EKSEKUSI PROSEDUR
cariHurufHilang(kata)
hitungHurufUnik(kata)

"""
[NOTE] CATATAN PENTING:
Sepertinya test case nomor 3 salah, seharusnya hasil test case nya seperti berikut:

(INPUT) Masukkan kata: pneumonoultramicroscopicsilicovolcanoconiosis
Huruf yang hilang: bdfghjkqwxyz
Jumlah huruf unik: 14

Pada test case tertulis jumlah huruf unik adalah 16.
"""