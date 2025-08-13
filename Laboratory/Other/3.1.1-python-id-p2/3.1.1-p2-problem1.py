""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Find Car>                     |
# +----------------------------------------+
# | Find a car in a parking building       |
# | using license plate analysis,          |
# | number of digits, and sum of digits on |
# | the license plate.                     |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | license_plate      | string    |
# | digit_sum          | integer   |
# | digit_count        | integer   |
# | car_digit_sum      | integer   |
# | car_digit_count    | integer   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT LICENSE PLATE, SUM OF DIGITS, AND NUMBER OF DIGITS
license_plate: str = input("Masukkan nomor plat mobil: ")
digit_sum: int = int(input("Masukkan jumlah digit: "))
digit_count: int = int(input("Masukkan banyak digit: "))

# INITIALIZE THE ACTUAL SUM AND COUNT OF DIGITS ON THE LICENSE PLATE
car_digit_sum: int = 0
car_digit_count: int = 0

# LOOP TO DETERMINE THE SUM AND COUNT OF DIGITS FROM THE INPUT
for i in license_plate:
    # IF IT IS A NUMBER -> PREVENTS INTEGER ERROR
    if ('0' <= i <= '9'):
        car_digit_sum += int(i)
        car_digit_count += 1

# CONDITIONAL, IF IT DOES NOT START WITH D, IT IS NOT THE CAR
if (license_plate[0] == "D"):
    # CONDITIONAL, IF THE SUM AND COUNT OF DIGITS FROM INPUT MATCH THE ACTUAL SUM AND COUNT OF DIGITS ON THE LICENSE PLATE
    if (digit_sum == car_digit_sum and digit_count == car_digit_count):
        print("Mobil Tuan Leo ditemukan!")
    else:
        print("Bukan mobil Tuan Leo!")
else:
    print("Bukan mobil Tuan Leo!")
