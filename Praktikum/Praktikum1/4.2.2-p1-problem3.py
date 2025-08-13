""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Fixing Swapped Numbers>       |
# +----------------------------------------+
# | Fixes swapped numbers by inputting     |
# | the positions of the numbers to be     |
# | swapped, using typecasting.            |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | price_digits       | integer   |
# | price              | integer   |
# | swap_num_one_pos   | integer   |
# | swap_num_two_pos   | integer   |
# | price_string       | string    |
# | fixed_number       | integer   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT PRICE DIGITS
price_digits: int = int(input("Masukkan jumlah digit harga: "))

# INPUT ITEM PRICE
price: int = int(input("Masukkan harga: "))

# INPUT 2 NUMBERS TO BE SWAPPED
swap_num_one_pos: int = int(input("Masukkan posisi angka pertama yang akan ditukar: "))
swap_num_two_pos: int = int(input("Masukkan posisi angka kedua yang akan ditukar: "))

# VALIDATE IF PRICE MATCHES PRICE DIGITS
if (10 ** (price_digits - 1) <= price < 10 ** price_digits):
    # CONVERT INTEGER TO STRING TO USE TYPECASTING METHOD
    price_string: str = str(price)

    # SWAP THE INCORRECT NUMBER POSITIONS
    fixed_number: int = int(price_string[:swap_num_one_pos-1] + price_string[swap_num_two_pos-1] + price_string[swap_num_one_pos:swap_num_two_pos-1] + price_string[swap_num_one_pos-1] + price_string[swap_num_two_pos:])

    # PRINT THE OUTPUT OF THE FIXED NUMBER
    print("Harga setelah diperbaiki : " + str(fixed_number))

# IF PRICE DOES NOT MATCH DIGITS, INFORM
else:
    print("Masukan harga tidak valid")