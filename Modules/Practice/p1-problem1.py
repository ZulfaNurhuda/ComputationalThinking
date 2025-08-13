""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Odd-Even Number Classifier>   |
# +----------------------------------------+
# | CLASSIFIES A GIVEN NUMBER AS POSITIVE, |
# | NEGATIVE, OR ZERO, AND IF POSITIVE,    |
# | WHETHER IT IS ODD OR EVEN.             |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | number_input       | INTEGER   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT THE NUMBER FROM USER
# PROMPT USER TO ENTER A NUMBER AND CONVERT STRING INPUT TO INTEGER
number_input: int = int(input("Masukkan nilai N: "))

# CLASSIFY THE NUMBER BASED ON ITS VALUE AND PARITY
# CHECK IF THE NUMBER IS POSITIVE (GREATER THAN ZERO)
if number_input > 0:
    # FOR POSITIVE NUMBERS, CHECK IF EVEN OR ODD USING MODULO OPERATION
    # IF REMAINDER WHEN DIVIDED BY 2 IS 0, THE NUMBER IS EVEN
    if number_input % 2 == 0:
        # PRINT RESULT FOR POSITIVE EVEN NUMBER
        print(f"{number_input} bilangan positif genap")
    else:
        # PRINT RESULT FOR POSITIVE ODD NUMBER
        print(f"{number_input} bilangan positif ganjil")
# CHECK IF THE NUMBER IS NEGATIVE (LESS THAN ZERO)
elif number_input < 0:
    # FOR NEGATIVE NUMBERS, ALSO CHECK IF EVEN OR ODD
    # MODULO OPERATION WORKS THE SAME FOR NEGATIVE NUMBERS
    if number_input % 2 == 0:
        # PRINT RESULT FOR NEGATIVE EVEN NUMBER
        print(f"{number_input} bilangan negatif genap")
    else:
        # PRINT RESULT FOR NEGATIVE ODD NUMBER
        print(f"{number_input} bilangan negatif ganjil")
# IF NUMBER IS NEITHER POSITIVE NOR NEGATIVE, IT MUST BE ZERO
else:
    # PRINT RESULT FOR ZERO (SPECIAL CASE)
    print(f"{number_input} adalah bilangan nol")
