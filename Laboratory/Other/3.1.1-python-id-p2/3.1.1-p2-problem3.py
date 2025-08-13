""" PROGRAM DESCRIPTION """
# +-------------------------------------------------------------+
# | PROGRAM <Arranging Books>                                   |
# +-------------------------------------------------------------+
# | This program aims to find a valid book arrangement          |
# | based on the number of shelves, the number of books, and    |
# | the desired arrangement direction (ascending or descending).|
# +-------------------------------------------------------------+

# +--------------------+---------------------+
# | DICTIONARY         | DATA TYPE           |
# +--------------------+---------------------+
# | shelf_count        | integer             |
# | book_count         | list[integer]       |
# | sort_direction     | string              |
# | total_books        | integer             |
# | valid_arrangement  | list[list[integer]] |
# | new_arrangement    | list[integer]       |
# | shelf_amount       | integer             |
# | total_books_in_arrangement | integer     |
# | minimum            | integer             |
# | shelf_distance     | integer             |
# | max_distance       | integer             |
# +--------------------+---------------------+

""" PROGRAM ALGORITHM """
# ASK THE USER TO INPUT THE NUMBER OF SHELVES
shelf_count: int = int(input("Jumlah rak yang dimiliki: "))

# ASK FOR THE NUMBER OF BOOKS ON EACH SHELF AND STORE IT
book_count: list[int] = [
    int(input(f"Jumlah buku di rak ke-{i + 1}: ")) for i in range(shelf_count)
]

# ASK THE USER TO INPUT THE BOOK ARRANGEMENT DIRECTION (ASCENDING OR DESCENDING)
sort_direction: str = input("Urutan buku diurutkan: Menaik/Menurun? ")

# CALCULATE THE TOTAL BOOKS FROM ALL SHELVES
total_books: int = 0
for i in book_count:
    total_books += i

# PREPARE A LIST TO STORE VALID ARRANGEMENTS
valid_arrangement: list[list[int]] = []

# LOOP TO FIND ARRANGEMENTS THAT MEET THE CONDITIONS
for index in range(1, total_books // (shelf_count - 1) + 2):
    arrangement: list[int] = []
    current: int = index
    remaining: int = total_books

    # BUILD THE BOOK ARRANGEMENT BASED ON A CERTAIN LOGIC
    for i in range(shelf_count):
        if remaining >= current and current >= 1:
            arrangement += [current]
            remaining -= current
            if i < shelf_count - 1:
                if current + 1 < remaining // (shelf_count - i - 1):
                    current = current + 1
                else:
                    current = remaining // (shelf_count - i - 1)

    # REVERSE THE ARRANGEMENT IF THE CHOSEN DIRECTION IS "DESCENDING"
    if sort_direction == "Menurun":
        arrangement = arrangement[::-1]

    # COUNT THE NUMBER OF SHELVES IN THE ARRANGEMENT
    shelf_amount: int = 0
    for _ in arrangement:
        shelf_amount += 1

    # COUNT THE TOTAL BOOKS IN THE ARRANGEMENT
    total_books_in_arrangement: int = 0
    for num in arrangement:
        total_books_in_arrangement += num

    # FIND THE SMALLEST VALUE IN THE ARRANGEMENT
    minimum: int = 0
    for num in arrangement:
        if minimum == 0:
            minimum = num
        elif minimum > num:
            minimum = num

    # CALCULATE THE LARGEST DISTANCE BETWEEN SHELVES IN THE ARRANGEMENT
    shelf_distance: int = 0
    for i in range(shelf_amount - 1):
        distance: int = arrangement[i] - arrangement[i + 1]
        if distance < 0:
            distance *= -1
        if shelf_distance < distance:
            shelf_distance = distance

    # ADD THE ARRANGEMENT TO THE LIST IF IT MEETS ALL CONDITIONS
    if (
        shelf_amount == shelf_count
        and total_books_in_arrangement == total_books
        and minimum >= 1
        and 0 <= shelf_distance <= 1
    ):
        valid_arrangement += [arrangement]

# FIND THE ARRANGEMENT WITH THE LARGEST DISTANCE BETWEEN THE FIRST AND LAST SHELF
new_arrangement: list[int] = []
for arrangement in valid_arrangement:
    max_distance: int = 0
    for i in valid_arrangement:
        distance = i[0] - i[-1]
        if distance < 0:
            distance *= -1
        if max_distance < distance:
            max_distance = distance
    distance = arrangement[0] - arrangement[-1]
    if distance < 0:
        distance *= -1
    if distance == max_distance:
        new_arrangement = arrangement

# COUNT THE NUMBER OF SHELVES IN THE NEW ARRANGEMENT
new_shelf_amount: int = 0
for _ in new_arrangement:
    new_shelf_amount += 1

# DISPLAY THE NEW ARRANGEMENT OR A MESSAGE IF NO VALID ARRANGEMENT EXISTS
if new_shelf_amount > 0:
    print(f"Urutan buku yang baru adalah {new_arrangement}.")
else:
    print("Tidak ada susunan yang valid untuk kondisi tersebut.")
