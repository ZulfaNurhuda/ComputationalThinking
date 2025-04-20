""" KETERANGAN PROGRAM """
# +-------------------------------------------------------------+
# | PROGRAM <Mengatur Susunan Buku>                             |
# +-------------------------------------------------------------+
# | Program ini bertujuan untuk mencari susunan buku yang valid |
# | berdasarkan jumlah rak, jumlah buku, dan arah susunan yang  |
# | diinginkan (menaik atau menurun).                           |
# +-------------------------------------------------------------+

# +--------------------+---------------------+
# | KAMUS              | TIPE DATA           |
# +--------------------+---------------------+
# | jumlah_rak         | integer             |
# | jumlah_buku        | list[integer]       |
# | arah_susunan       | string              |
# | total_buku         | integer             |
# | susunan_valid      | list[list[integer]] |
# | susunan_baru       | list[integer]       |
# | banyak_rak         | integer             |
# | total_buku_susunan | integer             |
# | minimal            | integer             |
# | jarak_antar_rak    | integer             |
# | jarak_terbesar     | integer             |
# +--------------------+---------------------+

# +------------------+-----------+------------------------------------------------+
# | VARIABEL ITERASI | TIPE DATA | KETERANGAN                                     |
# +------------------+-----------+------------------------------------------------+
# | index            | integer   | variabel iterasi, terdapat pada 1x pengulangan |
# | i                | integer   | variabel iterasi, terdapat pada 5x pengulangan |
# | _                | integer   | variabel iterasi, terdapat pada 2x pengulangan |
# | angka            | integer   | variabel iterasi, terdapat pada 2x pengulangan |
# | susunan          | list[int] | variabel iterasi, terdapat pada 1x pengulangan |
# +------------------+-----------+------------------------------------------------+


""" ALGORITMA PROGRAM """
# MEMINTA PENGGUNA UNTUK MEMASUKKAN JUMLAH RAK
jumlah_rak = int(input("Jumlah rak yang dimiliki: "))

# MEMINTA JUMLAH BUKU DI SETIAP RAK DAN MENYIMPANNYA
jumlah_buku = [
    int(input(f"Jumlah buku di rak ke-{i + 1}: ")) for i in range(jumlah_rak)
]

# MEMINTA PENGGUNA UNTUK MEMASUKKAN ARAH SUSUNAN BUKU (MENAIK ATAU MENURUN)
arah_susunan = input("Urutan buku diurutkan: Menaik/Menurun? ")

# MENGHITUNG TOTAL BUKU DARI SEMUA RAK
total_buku = 0
for i in jumlah_buku:
    total_buku += i

# MENYIAPKAN DAFTAR UNTUK MENYIMPAN SUSUNAN YANG VALID
susunan_valid = []

# PERULANGAN UNTUK MENCARI SUSUNAN YANG MEMENUHI KONDISI
for index in range(1, total_buku // (jumlah_rak - 1) + 2):
    susunan = []
    sekarang = index
    tersisa = total_buku

    # MEMBANGUN SUSUNAN BUKU BERDASARKAN LOGIKA TERTENTU
    for i in range(jumlah_rak):
        if tersisa >= sekarang and sekarang >= 1:
            susunan += [sekarang]
            tersisa -= sekarang
            if i < jumlah_rak - 1:
                if sekarang + 1 < tersisa // (jumlah_rak - i - 1):
                    sekarang = sekarang + 1
                else:
                    sekarang = tersisa // (jumlah_rak - i - 1)

    # MEMBALIK SUSUNAN JIKA ARAH YANG DIPILIH ADALAH "MENURUN"
    if arah_susunan == "Menurun":
        susunan = susunan[::-1]

    # MENGHITUNG JUMLAH RAK DALAM SUSUNAN
    banyak_rak = 0
    for _ in susunan:
        banyak_rak += 1

    # MENGHITUNG TOTAL BUKU DALAM SUSUNAN
    total_buku_susunan = 0
    for angka in susunan:
        total_buku_susunan += angka

    # MENCARI NILAI TERKECIL DALAM SUSUNAN
    minimal = 0
    for angka in susunan:
        if minimal == 0:
            minimal = angka
        elif minimal > angka:
            minimal = angka

    # MENGHITUNG JARAK TERBESAR ANTARA RAK DALAM SUSUNAN
    jarak_antar_rak = 0
    for i in range(banyak_rak - 1):
        jarak = susunan[i] - susunan[i + 1]
        if jarak < 0:
            jarak *= -1
        if jarak_antar_rak < jarak:
            jarak_antar_rak = jarak

    # MENAMBAHKAN SUSUNAN KE DAFTAR JIKA MEMENUHI SEMUA KONDISI
    if (
        banyak_rak == jumlah_rak
        and total_buku_susunan == total_buku
        and minimal >= 1
        and 0 <= jarak_antar_rak <= 1
    ):
        susunan_valid += [susunan]

# MENCARI SUSUNAN DENGAN JARAK TERBESAR ANTARA RAK PERTAMA DAN TERAKHIR
susunan_baru = []
for susunan in susunan_valid:
    jarak_terbesar = 0
    for i in susunan_valid:
        jarak = i[0] - i[-1]
        if jarak < 0:
            jarak *= -1
        if jarak_terbesar < jarak:
            jarak_terbesar = jarak
    jarak = susunan[0] - susunan[-1]
    if jarak < 0:
        jarak *= -1
    if jarak == jarak_terbesar:
        susunan_baru = susunan

# MENGHITUNG JUMLAH RAK DALAM SUSUNAN BARU
banyak_rak_baru = 0
for _ in susunan_baru:
    banyak_rak_baru += 1

# MENAMPILKAN SUSUNAN BARU ATAU PESAN JIKA TIDAK ADA SUSUNAN YANG VALID
if banyak_rak_baru > 0:
    print(f"Urutan buku yang baru adalah {susunan_baru}.")
else:
    print("Tidak ada susunan yang valid untuk kondisi tersebut.")