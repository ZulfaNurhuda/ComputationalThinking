""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Qualified Participants>       |
# +----------------------------------------+
# | Determines the number of qualified     |
# | participants and the compensation      |
# | dollar they will receive.              |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | dollar             | integer   |
# | min_time           | integer   |
# | leo_time           | integer   |
# | deb_time           | integer   |
# | sal_time           | integer   |
# | qualified_count    | integer   |
# | prize_per_person   | integer   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT THE AMOUNT OF DOLLARS AVAILABLE AS PRIZE
dollar: int = int(input("Masukkan nilai N: "))

# INPUT MINIMUM TIME TO QUALIFY
min_time: int = int(input("Masukkan nilai T: "))

# INPUT RUNNING TIME OF MR. LEO, MISS DEB, AND MISS SAL
leo_time: int = int(input("Masukkan waktu lari Tuan Leo: "))
deb_time: int = int(input("Masukkan waktu lari Nona Deb: "))
sal_time: int = int(input("Masukkan waktu lari Nona Sal: "))

# INITIALIZE QUALIFIED COUNT
qualified_count: int = 0

# ANALYZE WHO QUALIFIES
if (leo_time <= min_time):
    qualified_count += 1
if (deb_time <= min_time):
    qualified_count += 1
if (sal_time <= min_time):
    qualified_count += 1

# IF ANYONE QUALIFIES
if (qualified_count > 0):
    # DETERMINE PRIZE PER PERSON
    prize_per_person: int = int(dollar / qualified_count)

    # PRINT OUTPUT INFORMATION ABOUT THE NUMBER OF QUALIFIED PARTICIPANTS AND PRIZE PER PERSON
    print(f"Terdapat {qualified_count} peserta yang terkualifikasi dan masing-masing akan mendapatkan {prize_per_person} dollar kompeng.")

# IF NO ONE QUALIFIES
else:
    print("Tidak ada peserta yang terkualifikasi")