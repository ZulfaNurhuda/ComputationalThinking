""" PROGRAM DESCRIPTION """
# +--------------------------------------- +
# | PROGRAM <Runner's Points>              |
# +--------------------------------------- +
# | Determines the runner's total points   |
# | and time in 3 attempts                 |
# +--------------------------------------- +

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | stage_one_time     | integer   |
# | stage_two_time     | integer   |
# | stage_three_time   | integer   |
# | total_time         | integer   |
# | limit_one          | integer   |
# | limit_two          | integer   |
# | limit_three        | integer   |
# | total_points       | integer   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT TIME FOR EACH STAGE
stage_one_time: int = int(input("Masukkan waktu tahap 1 (menit): "))
stage_two_time: int = int(input("Masukkan waktu tahap 2 (menit): "))
stage_three_time: int = int(input("Masukkan waktu tahap 3 (menit): "))

# CALCULATE TOTAL TIME
total_time: int = stage_one_time + stage_two_time + stage_three_time

# INITIALIZE LIMITS
limit_one: int = 15
limit_two: int = 15
limit_three: int = 15

# CALCULATE TOTAL POINTS
total_points: int = 45 - stage_one_time - stage_two_time - stage_three_time

# IF STAGE 1 IS LESS THAN 5 MINUTES, STAGE 2 LIMIT INCREASES BY 2 MINUTES
if (stage_one_time < 5):
    limit_two += 2

# IF STAGE 2 IS LESS THAN 5 MINUTES, STAGE 3 LIMIT INCREASES BY 2 MINUTES
if (stage_two_time < 5):
    limit_three += 2

# IF TOTAL TIME IS UNDER 30 MINUTES, POINTS INCREASE BY 10
if (total_time < 30):
    total_points += 10

# IF ONE OF THE STAGES EXCEEDS THE TIME LIMIT, THE RUNNER IS DISQUALIFIED WITH 0 POINTS
if (stage_one_time > limit_one):
    total_time = stage_one_time
    total_points = 0
elif (stage_two_time > limit_two):
    total_time = stage_one_time + stage_two_time
    total_points = 0
elif (stage_three_time > limit_three):
    total_points = 0

# PRINT THE TOTAL TIME AND TOTAL POINTS OUTPUT
print(f"Total waktu yang dihabiskan adalah {total_time} menit Poin yang didapatkan adalah {total_points}.")
