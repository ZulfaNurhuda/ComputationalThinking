""" KETERANGAN PROGRAM """
# +------------------------------------------+
# | PROGRAM <Menentukan Harga Diskon>        |
# +------------------------------------------+
# | Menentukan harga diskon beserta dengan   |
# | mata uang, berdasarkan input pengguna    |
# | dengan memanfaatkan Fungsi dan Prosedur. |
# +------------------------------------------+

# +---------------+-----------+
# | KAMUS PROGRAM | TIPE DATA |
# +---------------+-----------+
# | harga_awal    | integer   |
# | diskon        | integer   |
# | mata_uang     | string    |
# | harga_diskon  | integer   |
# +---------------+-----------+

def hitungHarga(harga_awal: int, diskon: int) -> int:
    """ Keterangan: `[FUNGSI] hitungHarga` """
    # +------------------------------------------------+
    # | FUNGSI <Menentukan Harga Akhir Setelah Diskon> |
    # +------------------------------------------------+
    # | Menentukan harga diskon, berdasarkan           |
    # | input pengguna.                                |
    # +------------------------------------------------+

    # +--------------+-----------+
    # | KAMUS LOKAL  | TIPE DATA |
    # +--------------+-----------+
    # | harga_awal   | integer   |
    # | diskon       | integer   |
    # | harga_diskon | integer   |
    # +--------------+-----------+

    """ ALGORITMA FUNGSI """
    # MENGHITHUNG HARGA DISKON
    harga_diskon = harga_awal - (harga_awal * (diskon / 100))

    # KEMBALIKAN HASIL FUNGSI
    return int(harga_diskon)

def cetakHarga(harga_awal: int, diskon: int, mata_uang: str) -> None:
    """ Keterangan: `[PROSEDUR] cetakHarga` """
    # +------------------------------------------------------+
    # | PROSEDUR <Cetak Hasil Harga Diskon Dan Mata Uangnya> |
    # +------------------------------------------------------+
    # | Mencetak keluaran informasi berupa harga setelah     |
    # | diskon disertai dengan jenis mata uangnya.           |
    # +------------------------------------------------------+

    # +--------------+-----------+
    # | KAMUS LOKAL  | TIPE DATA |
    # +--------------+-----------+
    # | harga_awal   | integer   |
    # | diskon       | integer   |
    # | mata_uang    | string    |
    # | harga_diskon | integer   |
    # +--------------+-----------+

    """ ALGORITMA PROSEDUR """
    # MENCARI HARGA DISKON DENGAN MEMANFAATKAN FUNGSI SEBELUMNYA
    harga_diskon = hitungHarga(harga_awal, diskon)

    # PRINT KELUARAN INFORMASI HARGA DISKON DAN JENIS MATA UANG
    print(f"Harga yang harus dibayar adalah {harga_diskon} {mata_uang}")

""" ALGORITMA PROGRAM """
# INPUT HARGA AWAL, DISKON, DAN JENIS MATA UANG
harga_awal = int(input("Masukkan harga dasar barang: "))
diskon = int(input("Masukkan diskon barang: "))
mata_uang = str(input("Masukkan satuan mata uang: "))

# EKSEKUSI PROSEDUR
cetakHarga(harga_awal, diskon, mata_uang)