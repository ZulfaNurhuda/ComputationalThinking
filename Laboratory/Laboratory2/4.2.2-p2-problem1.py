""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Determine Land Area>          |
# +----------------------------------------+
# | Determines the minimum land area for   |
# | building a house based on the value of |
# | n from the input data.                 |
# +----------------------------------------+

# +--------------------+-------------------+
# | PROGRAM DICTIONARY | DATA TYPE         |
# +--------------------+-------------------+
# | num_data           | integer           |
# | data               | array of integer  |
# | minimum            | integer           |
# | selected           | integer           |
# +--------------------+-------------------+

""" PROGRAM ALGORITHM """
# INPUT THE NUMBER OF LAND DATA TO BE ENTERED
num_data: int = int(input("Masukkan banyak data: "))

# INPUT LAND AREA DATA BASED ON THE NUMBER OF LANDS AVAILABLE
data: list[int] = [int(input(f"Masukkan luas tanah ke-{i + 1}: ")) for i in range(num_data)]

# INPUT MINIMUM LAND AREA FOR BUILDING A HOUSE
minimum: int = int(input("Tentukan luas tanah minimum: "))

# SORT ARRAY, SO IT IS SORTED FROM SMALLEST TO LARGEST
for i in range(1, num_data):
    for j in range(0, num_data - 1):
        if (data[j] > data[j + 1]):
            data[j], data[j + 1] = data[j + 1], data[j]

# INITIALIZE SELECTED LAND
selected: int = 0

# PERFORM LOOP TO DETERMINE THE SMALLEST LAND THAT IS GREATER THAN OR EQUAL TO THE MINIMUM
for i in data:
    if (selected == 0):
        if (i >= minimum):
            selected += i

# CONDITIONAL, DETERMINE IF THERE IS A SELECTED LAND, IF NOT (0), THEN NO
if (selected > 0):
    print(f"Luas tanah terkecil yang dapat dipilih adalah {selected}.")
else:
    print("Tuan Leo tidak dapat membangun rumah.")
