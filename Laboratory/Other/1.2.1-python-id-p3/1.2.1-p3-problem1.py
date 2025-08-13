""" PROGRAM DESCRIPTION """
# +------------------------------------------+
# | PROGRAM <Determine Discounted Price>     |
# +------------------------------------------+
# | Determines the discounted price along    |
# | with the currency, based on user input   |
# | utilizing Functions and Procedures.      |
# +------------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | initial_price      | integer   |
# | discount           | integer   |
# | currency           | string    |
# +--------------------+-----------+

def calculatePrice(initial_price: int, discount: int) -> int:
    """ Description: `[FUNCTION] calculatePrice` """
    # +-------------------------------------------------+
    # | FUNCTION <Determine Final Price After Discount> |
    # +-------------------------------------------------+
    # | Determines the discounted price, based on       |
    # | user input.                                     |
    # +-------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | initial_price      | integer   |
    # | discount           | integer   |
    # | discounted_price   | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # CALCULATE DISCOUNTED PRICE
    discounted_price: int = initial_price - (initial_price * (discount / 100))

    # RETURN FUNCTION RESULT
    return int(discounted_price)

def printPrice(initial_price: int, discount: int, currency: str) -> None:
    """ Description: `[PROCEDURE] printPrice` """
    # +--------------------------------------------------------+
    # | PROCEDURE <Print Discounted Price and Currency>        |
    # +--------------------------------------------------------+
    # | Prints the output information in the form of the       |
    # | price after the discount along with its currency type. |
    # +------------------------------------------------------ -+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | initial_price      | integer   |
    # | discount           | integer   |
    # | currency           | string    |
    # | discounted_price   | integer   |
    # +--------------------+-----------+

    """ PROCEDURE ALGORITHM """
    # FIND THE DISCOUNTED PRICE USING THE PREVIOUS FUNCTION
    discounted_price: int = calculatePrice(initial_price, discount)

    # PRINT DISCOUNTED PRICE AND CURRENCY TYPE INFORMATION OUTPUT
    print(f"Harga yang harus dibayar adalah {discounted_price} {currency}")

""" PROGRAM ALGORITHM """
# INPUT INITIAL PRICE, DISCOUNT, AND CURRENCY TYPE
initial_price: int = int(input("Masukkan harga dasar barang: "))
discount: int = int(input("Masukkan diskon barang: "))
currency: str = str(input("Masukkan satuan mata uang: "))

# EXECUTE PROCEDURE
printPrice(initial_price, discount, currency)
