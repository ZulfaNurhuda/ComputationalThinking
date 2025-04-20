import os
from pathlib import Path
from dotenv import load_dotenv

# ╒====================================╕
# |     INISIALISASI ENV VARIABLE      |
# ╘====================================╛
# Menggunakan file .env untuk menyimpan kredensial private dan pengaturan lainnya.
# File .env harus ada di direktori yang sama dengan file ini.
#
# File .env berisi variabel-variabel berikut:
# - FILE_AKUN_LAYANAN: Nama file kredensial akun layanan Google (misalnya: 'credentials.json')
# - ID_SHEET: ID Google Sheets yang digunakan untuk menyimpan data transaksi
#
# Hal ini dilakukan untuk menjaga keamanan dan privasi informasi sensitif.
# Penggunaan file .env juga memudahkan pengaturan dan perubahan konfigurasi tanpa harus mengubah kode sumber.

FILE_ENV = Path(
    os.path.join(
        os.getcwd(),
        "credentials",
        ".env",
    )
)

if FILE_ENV.exists():
    load_dotenv(dotenv_path=FILE_ENV)
else:
    print(f"File {FILE_ENV.name} tidak ditemukan. Pastikan file .env ada di direktori yang benar.")
    import sys
    sys.exit(1)

# =============================================================================================================

class Konfigurasi:
    """Konfigurasi global untuk aplikasi mesin kopi."""

    # File kredensial akun layanan Google
    FILE_AKUN_LAYANAN = os.path.join(
        os.getcwd(),
        "credentials",
        os.getenv("FILE_AKUN_LAYANAN", "credentials.json"),
    )

    # ID Google Sheets
    ID_SHEET = os.getenv("ID_SHEET", "123abc456def789ghi012jkl345mno678pqrs")

    # Kode admin default (jika admin_code.txt belum ada)
    KODE_ADMIN_DEFAULT = 1234567890

    # Host untuk webservice
    HOST = "0.0.0.0"

    # Port untuk webservice Flask
    PORT = 5000

    # Host untuk pengecekan koneksi (untuk indikasi webserver sudah berjalan)
    CHECK_HOST = "127.0.0.1" # JANGAN DIUBAH-UBAH

    # Durasi timeout untuk input (dalam detik)
    DURASI_TIMEOUT = 60

    # Interval sinkronisasi periodik ke Google Sheets (dalam detik)
    INTERVAL_SINKRONISASI = 300  # 5 menit

    # Batas waktu pembayaran QRIS (dalam detik)
    QRIS_TIMEOUT = 300  # 5 menit
