""" PROGRAM DESCRIPTION """
# +-----------------------------------------+
# | PROGRAM <Bravo Number Identifier>       |
# +-----------------------------------------+
# | DETERMINES IF A 4-DIGIT NUMBER IS A     |
# | "BRAVO" NUMBER (SUM OF DIGITS DIVISIBLE |
# | BY EACH NON-ZERO DIGIT) OR A "BIASA"    |
# | NUMBER.                                 |
# +-----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | number_int         | INTEGER   |
# | digit1             | INTEGER   |
# | digit2             | INTEGER   |
# | digit3             | INTEGER   |
# | digit4             | INTEGER   |
# | sum_of_digits      | INTEGER   |
# | is_bravo           | BOOLEAN   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT THE NUMBER AS INTEGER FROM USER
# PROMPT USER TO ENTER A NUMBER AND CONVERT STRING INPUT TO INTEGER
number_int: int = int(input("Masukkan sebuah bilangan: "))

# CHECK IF THE NUMBER IS EXACTLY 4 DIGITS (BETWEEN 1000 AND 9999)
# VALIDATE INPUT TO ENSURE IT'S A 4-DIGIT NUMBER AS REQUIRED
if number_int < 1000 or number_int > 9999:
    # PRINT ERROR MESSAGE IF NUMBER IS NOT 4 DIGITS
    print("Mohon masukkan bilangan 4 digit.")
else:
    # EXTRACT EACH DIGIT USING INTEGER DIVISION AND MODULO OPERATIONS
    # GET THOUSANDS DIGIT BY DIVIDING BY 1000 (INTEGER DIVISION)
    digit1: int = number_int // 1000
    # GET HUNDREDS DIGIT BY DIVIDING BY 100 AND TAKING REMAINDER WHEN DIVIDED BY 10
    digit2: int = (number_int // 100) % 10
    # GET TENS DIGIT BY DIVIDING BY 10 AND TAKING REMAINDER WHEN DIVIDED BY 10
    digit3: int = (number_int // 10) % 10
    # GET UNITS DIGIT BY TAKING REMAINDER WHEN DIVIDED BY 10
    digit4: int = number_int % 10
    
    # CALCULATE THE SUM OF ALL FOUR DIGITS
    # ADD ALL INDIVIDUAL DIGITS TO GET TOTAL SUM
    sum_of_digits: int = digit1 + digit2 + digit3 + digit4
    # INITIALIZE BOOLEAN FLAG TO TRACK IF NUMBER IS BRAVO (ASSUME TRUE INITIALLY)
    is_bravo: bool = True
    
    # CHECK BRAVO NUMBER CONDITIONS FOR EACH NON-ZERO DIGIT
    # A BRAVO NUMBER REQUIRES SUM OF DIGITS TO BE DIVISIBLE BY EACH NON-ZERO DIGIT
    # CHECK FIRST DIGIT: IF NOT ZERO AND SUM NOT DIVISIBLE BY IT, NOT BRAVO
    if digit1 != 0 and sum_of_digits % digit1 != 0:
        is_bravo = False
    # CHECK SECOND DIGIT: IF NOT ZERO AND SUM NOT DIVISIBLE BY IT, NOT BRAVO
    if digit2 != 0 and sum_of_digits % digit2 != 0:
        is_bravo = False
    # CHECK THIRD DIGIT: IF NOT ZERO AND SUM NOT DIVISIBLE BY IT, NOT BRAVO
    if digit3 != 0 and sum_of_digits % digit3 != 0:
        is_bravo = False
    # CHECK FOURTH DIGIT: IF NOT ZERO AND SUM NOT DIVISIBLE BY IT, NOT BRAVO
    if digit4 != 0 and sum_of_digits % digit4 != 0:
        is_bravo = False
    
    # PRINT THE RESULT BASED ON BRAVO NUMBER CLASSIFICATION
    # IF ALL CONDITIONS ARE MET, NUMBER IS BRAVO
    if is_bravo:
        # PRINT BRAVO NUMBER MESSAGE
        print(f"Bilangan tersebut adalah bilangan Bravo.")
    else:
        # PRINT REGULAR NUMBER MESSAGE
        print(f"Bilangan tersebut adalah bilangan biasa.")
