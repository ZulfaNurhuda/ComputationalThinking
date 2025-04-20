""" IDENTITAS """
# Nama: Muhammad Zulfa Fauzan Nurhuda
# NIM: 19624258
# Tanggal: 07 Desember 2024

""" KETERANGAN PROGRAM """
# PROGRAM <Memecahkan kode enkripsi>
# Melakukan dekripsi pesan berdasarkan aturan yang sudah ditentukan

# KAMUS | DICTIONARY
# kata_terenkripsi: string
# kata_terdekripsi: string
# (Variabel fungsi/prosedur dapat dilihat di masing masing variabel lokal fungsi/prosedur)

""" ALGORITMA PROGRAM """
def cariAngkaAsliAngkaTerenkripsi(angka):
    """ Keterangan: [FUNGSI] cariAngkaAsliAngkaTerenkripsi """
    # FUNGSI <Mencari angka sebenarnya>
    # Mencari angka sebenarnya dari pesan terenkripsi
    # Alasan menggunakan fungsi: ada data keluaran yang masih bisa dimanipulasi di luar fungsi yang dijalankan

    # KAMUS LOKAL | LOCAL DICTIONARY
    # (parameter) angka: string
    # angka_terenkripsi: integer

    """ ALGORITMA FUNGSI """
    # Buat angka terenkripsi menjadi integer
    angka_terenkripsi = int(angka)

    # Proses dengan syarat yang sudah ditentukan
    if angka_terenkripsi % 2 == 0:
        return angka_terenkripsi // 2
    else:
        return angka_terenkripsi // 3

def konversiHurufAngkaTerenkripsi(kata_terenkripsi):
    """ Keterangan: [FUNGSI] konversiHurufAngkaTerenkripsi """
    # FUNGSI <Mencari angka sebenarnya>
    # Mencari pesan berupa huruf sebenarnya dari pesan terenkripsi
    # Alasan menggunakan fungsi: ada data keluaran yang masih bisa dimanipulasi di luar fungsi yang dijalankan

    # KAMUS LOKAL | LOCAL DICTIONARY
    # (parameter) kata_terenkripsi: string
    # panjang_kata: integer
    # kata_terdekripsi: string
    # huruf_latin: Array[string]
    # angka_asli_terenkripsi: integer

    """ ALGORITMA FUNGSI """
    # Mencari panjang kata
    panjang_kata = 0
    for i in kata_terenkripsi:
        panjang_kata += 1

    # Inisialisasi kata_terdekripsi untuk menampung hasil dekripsi pesan
    kata_terdekripsi = ""

    # Lakukan iterasi untuk setiap 2 karakter pada kata_terenkripsi untuk melakukan dekripsi
    for i in range(0, panjang_kata, 2):
        huruf_latin = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # Gunakan fungsi cariAngkaAsliAngkaTerenkripsi untuk mencari angka asli
        angka_asli_terenkripsi = cariAngkaAsliAngkaTerenkripsi(
            kata_terenkripsi[i] + kata_terenkripsi[i + 1]
        )

        kata_terdekripsi += huruf_latin[angka_asli_terenkripsi - 1]

    # Lakukan kembalian data berupa pesan yang sudah terdekripsi
    return kata_terdekripsi

# Input pesan rahasia terenkripsi
kata_terenkripsi = str(input("Pesan rahasia: "))

# Gunakan fungsi konversiHurufAngkaTerenkripsi untuk mendekripsi pesan
kata_terdekripsi = konversiHurufAngkaTerenkripsi(kata_terenkripsi)

# Print informasi dari pesan yang sudah terdekripsi
print(f"Pesan rahasia dari Tuan Leo adalah {kata_terdekripsi}")
