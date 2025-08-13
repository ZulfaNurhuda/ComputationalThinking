""" PROGRAM DESCRIPTION """
# +-----------------------------------------+
# | PROGRAM <Harvest Festival Exhibition>   |
# +-----------------------------------------+
# | Shows whether the harvest can be        |
# | exhibited at the festival based on      |
# | input data of the day and grade of the  |
# | harvest.                                |
# +-----------------------------------------+

# +-----------------------+-----------+
# | PROGRAM DICTIONARY    | DATA TYPE |
# +-----------------------+-----------+
# | harvest_day           | integer   |
# | harvest_grade         | integer   |
# | min_tuesday           | integer   |
# | min_saturday          | integer   |
# | week_1                | string    |
# | week_2                | string    |
# | day_distance_tuesday  | integer   |
# | day_distance_saturday | integer   |
# | day_1                 | string    |
# | day_2                 | string    |
# +-----------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT HARVEST DAY WITH A NUMBER
harvest_day: int = int(input("Masukkan hari panen (dengan 1 menandakan hari Senin): "))

# INPUT GRADE WHEN HARVESTING
harvest_grade: int = int(input("Masukkan grade hasil panen: "))

# INITIALIZE MINIMUM GRADE FOR FESTIVAL EXHIBITION
min_tuesday: int = 5
min_saturday: int = 7

# INITIALIZE WEEK (THIS WEEK / NEXT WEEK)
week_1: str = ""
week_2: str = ""

# ANALYZE THE CONDITION OF DAY AND WEEK DISTANCE FOR TUESDAY
day_distance_tuesday: int = 2 - harvest_day
if (day_distance_tuesday < 0):
    day_distance_tuesday = 7 - (day_distance_tuesday * -1)
    week_1 = "minggu depan"
else:
    week_1 = "minggu ini"

# ANALYZE THE CONDITION OF DAY AND WEEK DISTANCE FOR SATURDAY
day_distance_saturday: int = 6 - harvest_day
if (day_distance_saturday < 0):
    day_distance_saturday = 7 - (day_distance_saturday * -1)
    week_2 = "minggu depan"
else:
    week_2 = "minggu ini"

# INITIALIZE DAY (SATURDAY/TUESDAY)
day_1: str = ""
day_2: str = ""

# ANALYZE WHETHER DAY 1 AND DAY 2 CAN BE EXHIBITED
if (harvest_grade - day_distance_tuesday >= min_tuesday):
    day_1 = "Selasa " + week_1
if (harvest_grade - day_distance_saturday >= min_saturday):
    day_2 = "Sabtu " + week_2

# INITIALIZE FINAL STATEMENT
final_statement: str = ""

# PRINT RESULTS BASED ON DAY CONDITIONS
if (day_1 != "" and day_2 != ""):
    final_statement = f"Hasil panen Nona Sal layak dipamerkan pada festifal di hari {day_1} dan {day_2}."
elif (day_1 != "" and day_2 == ""):
    final_statement = f"Hasil panen Nona Sal layak dipamerkan pada festifal di hari {day_1}."
elif (day_1 == "" and day_2 != ""):
    final_statement = f"Hasil panen Nona Sal layak dipamerkan pada festifal di hari {day_2}."
else:
    final_statement = "Hasil panen Nona Sal tidak layak untuk dipamerkan pada festival."

# PRINT FINAL STATEMENT OUTPUT
print(final_statement)
