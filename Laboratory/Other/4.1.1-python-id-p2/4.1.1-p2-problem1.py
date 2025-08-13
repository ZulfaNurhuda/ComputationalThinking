""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Building Assignment>          |
# +----------------------------------------+
# | Assigns participants to buildings A    |
# | and B based on participant numbers    |
# | and building capacity constraints.    |
# +----------------------------------------+

# +-----------------------+-----------------+
# | PROGRAM DICTIONARY    | DATA TYPE       |
# +-----------------------+-----------------+
# | participant_limit     | integer         |
# | participants_a        | array of int    |
# | participants_b        | array of int    |
# | index_a               | integer         |
# | index_b               | integer         |
# | stop                  | boolean         |
# | participant           | integer         |
# | activity_count_a      | integer         |
# | activity_count_b      | integer         |
# +-----------------------+-----------------+

""" PROGRAM ALGORITHM """
# INITIALIZE PARTICIPANT LIMIT INPUT
participant_limit: int = int(input("Masukkan Nilai N: "))

# INITIALIZE PARTICIPANT ARRAYS FOR BUILDING A (CAPACITY 5) AND BUILDING B (CAPACITY 3)
participants_a: list[int] = [0 for _ in range(5)]
participants_b: list[int] = [0 for _ in range(3)]

# INITIALIZE COUNTERS FOR BUILDING A AND BUILDING B
index_a: int = 0
index_b: int = 0

# INITIALIZE STOP CONDITION FOR LOOP
stop: bool = False
# LOOP TO INPUT PARTICIPANTS FOR ACTIVITIES
while not stop:
    # INPUT PARTICIPANT NUMBER
    participant: int = int(input(f"Masukkan peserta kegiatan ke-{index_a + index_b + 1}: "))
    # IF PARTICIPANT NUMBER IS LESS THAN THE LIMIT
    if (participant < participant_limit):
        # IF THERE IS STILL SPACE IN BUILDING A
        if (index_a + 1 <= 5):
            # ADD PARTICIPANT TO BUILDING A
            participants_a[index_a] = participant
            # INCREMENT COUNTER FOR BUILDING A
            index_a += 1
        else:
            # ADD PARTICIPANT TO BUILDING B
            participants_b[index_b] = participant
            # INCREMENT COUNTER FOR BUILDING B
            index_b += 1
    else:
        # ADD PARTICIPANT TO BUILDING B
        participants_b[index_b] = participant
        # INCREMENT COUNTER FOR BUILDING B
        index_b += 1

    # IF BUILDING B IS FULL
    if (index_b >= 3):
        # STOP INPUT LOOP
        stop = True

# CALCULATE NUMBER OF ACTIVITIES IN BUILDING A
activity_count_a: int = 0
for i in participants_a:
    # IF SLOT IS FILLED BY PARTICIPANT
    if i > 0:
        # ADD ONE TO ACTIVITY COUNT IN BUILDING A
        activity_count_a += 1

# CALCULATE NUMBER OF ACTIVITIES IN BUILDING B
activity_count_b: int = 0
for i in participants_b:
    # IF SLOT IS FILLED BY PARTICIPANT
    if i > 0:
        # ADD ONE TO ACTIVITY COUNT IN BUILDING B
        activity_count_b += 1

# DISPLAY ACTIVITY COUNT IN BUILDING A AND BUILDING B TO USER
print(f"Terdapat {activity_count_a} kegiatan di gedung A dan {activity_count_b} kegiatan di gedung B.")