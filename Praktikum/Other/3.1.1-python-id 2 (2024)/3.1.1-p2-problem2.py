""" KETERANGAN PROGRAM """
# +-------------------------------------------------+
# | PROGRAM <Merapikan Invoice>                     |
# +-------------------------------------------------+
# | Mengidentifikasi data pada invoice (nomor       |
# | department pengirim, penerima, dan nomor urut   |
# | invoice) dan menyusunnya pada format yang benar |
# +-------------------------------------------------+

# +----------------------------+----------------------+
# | KAMUS                      | TIPE DATA            |
# +----------------------------+----------------------+
# | department_kirim           | list[string]         |
# | data_department_kirim      | dict[string, string] |
# | nomor_invoice              | string               |
# | invoice_data               | list[string]         |
# | indeks                     | integer              |
# | pembatas                   | boolean              |
# | department_kirim_invoice   | string               |
# | department_terima_invoice  | string               |
# | nomor_urut_invoice         | string               |
# +----------------------------+----------------------+

# +------------------+-----------+------------------------------------------------+
# | VARIABEL ITERASI | TIPE DATA | KETERANGAN                                     |
# +------------------+-----------+------------------------------------------------+
# | nomor_department | string    | variabel iterasi, terdapat pada 1x pengulangan |
# | i                | integer   | variabel iterasi, terdapat pada 2x pengulangan |
# | _                | string    | variabel iterasi, terdapat pada 1x pengulangan |
# +------------------+-----------+------------------------------------------------+


""" ALGORITMA PROGRAM """
# INISIALISASI NOMOR DEPARTMENT YANG BISA MENGIRIM
department_kirim = ["1", "9", "14"]

# INPUT DATA INVOICE YANG SUDAH DIHASILKAN DARI MASING MASING DEPARTMENT PENGIRIM
data_department_kirim = {
    nomor_department: str(input(f"Masukkan jumalah invoice yang telah dikeluarkan oleh departemen {nomor_department}: "))
    for nomor_department in department_kirim
}

# INPUT NOMOR INVOICE YANG AKAN DI CEK
nomor_invoice = str(input("Masukkan nomor invoice yang akan dicek: "))

# INISIALISASI INVOICE DATA UNTUK MENAMPUNG ANGKA ANGKA YANG SUDAH TERPISAH OLEH SEPARATOR (/)
invoice_data = ["" for _ in range(3)]

# BUAT INDEKS DAN PEMBATAS UNTUK MENDUKUNG PENGULANGAN
indeks = 0
pembatas = False

# PENGULANGAN UNTUK MENCARI ANGKA ANGKA YANG TERPISAH OLEH SEPARATOR (/)
for i in nomor_invoice:
    if ('0' <= i <= '9'):
        if (not pembatas):
            invoice_data[indeks] += i
        else:
            invoice_data[indeks] = i
            pembatas = False
    else:
        indeks += 1
        pembatas = True

# INISIALISASI NOMOR DEPARTMENT PENGIRIM, PENERIMA, DAN NOMOR URUT INVOICE
department_kirim_invoice = None
department_terima_invoice = None
nomor_urut_invoice = None

# MENYELEKSI ANGKA YANG ADA PADA INVOICE DATA, UNTUK DIKELOLA ANGKA TERSEBUT BERMAKSUD SEBAGAI APA
for i in invoice_data:
    digit = 0
    for _ in i:
        digit += 1

    if digit == 3:
        nomor_urut_invoice = i
    else:
        if i in department_kirim:
            department_kirim_invoice = i
        else:
            department_terima_invoice = i

# KONDISIONAL SEBAGAI FILTER KONDISI YANG TERJADI
if (department_kirim_invoice and department_terima_invoice and nomor_urut_invoice):
    if (nomor_urut_invoice <= data_department_kirim[department_kirim_invoice]):
        print(f"Nomor invoice yang valid: {department_kirim_invoice}/{nomor_urut_invoice}/{department_terima_invoice}")
    else:
        print("Nomor invoice tersebut tidak valid.")
else:
    print("Nomor invoice tersebut tidak valid.")