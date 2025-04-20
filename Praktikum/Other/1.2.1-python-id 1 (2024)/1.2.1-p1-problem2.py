""" KETERANGAN PROGRAM """
# +-----------------------------------------+
# | PROGRAM <Pameran Festival Hasil Panen>  |
# +-----------------------------------------+
# | Menunjukkan apakah hasil panen dapat    |
# | dipamerkan pada festival berdasarkan    |
# | masukan data hari dan grade hasil panen |
# +-----------------------------------------+

# +-------------------+-----------+
# | KAMUS PROGRAM     | TIPE DATA |
# +-------------------+-----------+
# | hari_panen        | integer   |
# | grade_panen       | integer   |
# | min_selasa        | integer   |
# | min_sabtu         | integer   |
# | minggu_1          | string    |
# | minggu_2          | string    |
# | jarak_hari_selasa | integer   |
# | jarak_hari_sabtu  | integer   |
# | hari_1            | string    |
# | hari_2            | string    |
# +-------------------+-----------+

""" ALGORITMA PROGRAM """
# INPUT HARI PANEN DENGAN ANGKA
hari_panen = int(input("Masukkan hari panen (dengan 1 menandakan hari Senin): "))

# INPUT GRADE KETIKA PANEN
grade_panen = int(input("Masukkan grade hasil panen: "))

# INISIASI GRADE MINIMAL PAMERAN FESTIVAL
min_selasa = 5
min_sabtu = 7

# INISIASI MINGGU (MINGGU INI / MINGGU DEPAN)
minggu_1 = ""
minggu_2 = ""

# MENGANALISIS KONDISI JARAK HARI DAN MINGGU UNTUK HARI SELASA
jarak_hari_selasa = 2 - hari_panen
if (jarak_hari_selasa < 0):
    jarak_hari_selasa = 7 - (jarak_hari_selasa * -1)
    minggu_1 = "minggu depan"
else:
    minggu_1 = "minggu ini"

# MENGANALISIS KONDISI JARAK HARI DAN MINGGU UNTUK HARI SABTU
jarak_hari_sabtu = 6 - hari_panen
if (jarak_hari_sabtu < 0):
    jarak_hari_sabtu = 7 - (jarak_hari_sabtu * -1)
    minggu_2 = "minggu depan"
else:
    minggu_2 = "minggu ini"

# INISIASI HARI (SABTU/SELASA)
hari_1 = ""
hari_2 = ""

# MENGANALIS APAKAH HARI 1 DAN HARI 2 BISA DILAKUKAN PAMERAN
if (grade_panen - jarak_hari_selasa >= min_selasa):
    hari_1 = "Selasa " + minggu_1
if (grade_panen - jarak_hari_sabtu >= min_sabtu):
    hari_2 = "Sabtu " + minggu_2

# INISIASI FINAL STATEMENT
final_statement = ""

# PRINT HASIL BERDASARKAN KONDISI HARI
if (hari_1 != "" and hari_2 != ""):
    final_statement = f"Hasil panen Nona Sal layak dipamerkan pada festifal di hari {hari_1} dan {hari_2}."
elif (hari_1 != "" and hari_2 == ""):
    final_statement = f"Hasil panen Nona Sal layak dipamerkan pada festifal di hari {hari_1}."
elif (hari_1 == "" and hari_2 != ""):
    final_statement = f"Hasil panen Nona Sal layak dipamerkan pada festifal di hari {hari_2}."
else:
    final_statement = "Hasil panen Nona Sal tidak layak untuk dipamerkan pada festival."

# PRINT KELUARAN FINAL STATEMENT
print(final_statement)