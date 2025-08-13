""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <User ID Possibilities>        |
# +----------------------------------------+
# | Determines possible user IDs based on  |
# | the prime factors of the serial number |
# | and limited by [upper_bound,           |
# | lower_bound]                           |
# +----------------------------------------+

# +-----------------------+------------------+
# | PROGRAM DICTIONARY    | TIPE DATA        |
# +-----------------------+------------------+
# | serial_number         | integer          |
# | lower_bound           | integer          |
# | upper_bound           | integer          |
# | prime_factors         | array of integer |
# | user_ids              | array of integer |
# | num_possible_ids      | integer          |
# +-----------------------+------------------+

""" PROGRAM ALGORITHM """
# INPUT SERIAL NUMBER, LOWER BOUND, AND UPPER BOUND
serial_number: int = int(input("Masukkan Nomor Urut: "))
lower_bound: int = int(input("Masukkan batas bawah (x): "))
upper_bound: int = int(input("Masukkan batas atas (y): "))

# INITIALIZE PRIME FACTORS ARRAY
prime_factors: list[int] = []

# CHECK PRIME FACTOR 2
if serial_number % 2 == 0:
    prime_factors += [2]
    while serial_number % 2 == 0:
        serial_number //= 2

# CHECK ODD PRIME FACTORS STARTING FROM 3, 5, 7 ... ETC
for i in range(3, int(serial_number ** 0.5) + 1, 2):
    if serial_number % i == 0:
        prime_factors += [i]
        while serial_number % i == 0:
            serial_number //= i

# IF THE REMAINDER IS GREATER THAN 2, IT IS COUNTED AS A PRIME FACTOR
if (serial_number > 2):
    prime_factors += [serial_number]

# INITIALIZE USER ID ARRAY
user_ids: list[int] = []

# LOOP TO ENSURE USER ID VALIDATION FROM AVAILABLE PRIME FACTORS
for i in range(lower_bound + 1, upper_bound + 1):
    for factor in prime_factors:
        if (i % factor == 0):
            if i not in user_ids:
                user_ids += [i]

# INITIALIZE POSSIBLE USER IDS
num_possible_ids: int = 0

# LOOP TO FIND THE TOTAL NUMBER OF POSSIBLE USER IDS
for _ in user_ids:
    num_possible_ids += 1

# CONDITIONAL, IF THE NUMBER OF POSSIBLE IDS IS GREATER THAN 0, THEN PRINT POSSIBLE USER IDS
if (num_possible_ids > 0):
    print(f"Id Pengguna yang valid = {user_ids}")
else:
    print("Tidak ada Id Pengguna yang valid.")
