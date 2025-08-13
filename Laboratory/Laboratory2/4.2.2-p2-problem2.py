""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Consumption Check>            |
# +----------------------------------------+
# | Determines which visitors can and      |
# | cannot receive consumption, and records|
# | how many visitors received consumption |
# | and how many tried more than once.     |
# +----------------------------------------+

# +-----------------------+-----------------+
# | PROGRAM DICTIONARY    | DATA TYPE       |
# +-----------------------+-----------------+
# | stop                  | boolean         |
# | ticket_data           | array of string |
# | more_than_one         | array of string |
# | ticket_number         | string          |
# | total_consumption     | integer         |
# | total_more_than_one   | integer         |
# +-----------------------+-----------------+

""" PROGRAM ALGORITHM """
# INITIALIZE TICKET DATA ARRAY AND MORE THAN ONE DATA (AND EACH LENGTH)
ticket_data: list[str] = []
more_than_one: list[str] = []

# INITIALIZE STOP, TO DETERMINE IF ITERATION SHOULD STOP OR NOT (BECAUSE BREAK IS NOT ALLOWED)
stop: bool = False

# LOOP TO ENSURE TICKET NUMBER HAS RECEIVED CONSUMPTION OR NOT
while not stop:
    ticket_number: str = str(input("Masukkan nomor tiket pengunjung: "))

    # CONDITIONAL, XXX TO EXIT LOOP
    if (ticket_number == "XXX"):
        stop = True

    # IF NOT XXX, PROCESS TICKET NUMBER
    else:
        if (ticket_number not in ticket_data):
            print("Pengunjung tersebut bisa mendapat konsumsi.")
            ticket_data += [ticket_number]
        elif (ticket_number in ticket_data):
            print("Pengunjung tersebut tidak bisa mendapat konsumsi lagi.")
            if (ticket_number not in more_than_one):
                more_than_one += [ticket_number]

# INITIALIZE TOTAL VISITORS WHO RECEIVED CONSUMPTION
total_consumption: int = 0

# LOOP TO DETERMINE VISITORS WHO RECEIVED CONSUMPTION
for _ in ticket_data:
    total_consumption += 1

# INITIALIZE TOTAL VISITORS WHO TRIED MORE THAN ONCE
total_more_than_one: int = 0

# LOOP TO DETERMINE VISITORS WHO TRIED MORE THAN ONCE
for _ in more_than_one:
    total_more_than_one += 1

# PROVIDE OUTPUT DATA OF TOTAL VISITORS WHO RECEIVED CONSUMPTION
print(f"Total pengunjung yang mendapat konsumsi: {total_consumption}")

# IF ANYONE TRIED MORE THAN ONCE, PROVIDE THEIR DATA
if (total_more_than_one > 0):
    print(f"Total pengunjung yang mencoba mendapat konsumsi lebih dari satu kali: {total_more_than_one}")
