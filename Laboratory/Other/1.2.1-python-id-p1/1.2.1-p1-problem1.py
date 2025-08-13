""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Runner's Time>                |
# +----------------------------------------+
# | Calculates the maximum time for a      |
# | runner from 3 running attempts         |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | time_1             | integer   |
# | time_2             | integer   |
# | time_3             | integer   |
# | final_time         | integer   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT TIME FOR EACH RUN
time_1: int = int(input("Masukkan waktu lari pertama: "))
time_2: int = int(input("Masukkan waktu lari kedua: "))
time_3: int = int(input("Masukkan waktu lari ketiga: "))

# INITIALIZE FINAL TIME
final_time: float = 0.0

# BRANCHING TO ANALYZE THE MAXIMUM TIME
if (time_1 >= time_2 >= time_3):
    final_time = (time_1 + time_2) / 2
elif (time_1 >= time_3 >= time_2):
    final_time = (time_1 + time_3) / 2
elif (time_2 >= time_1 >= time_3):
    final_time = (time_2 + time_1) / 2
elif (time_2 >= time_3 >= time_1):
    final_time = (time_2 + time_3) / 2
elif (time_3 >= time_1 >= time_2 ):
    final_time = (time_3 + time_1) / 2
else:
    final_time = (time_3 + time_2) / 2

# PRINT THE FINAL TIME OUTPUT FOR THE PARTICIPANT
print(f"Waktu akhir peserta adalah {final_time} detik.")
