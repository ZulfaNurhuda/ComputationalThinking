""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Number Classification>        |
# +----------------------------------------+
# | CLASSIFIES A FOUR-DIGIT NUMBER INTO    |
# | FOUR CATEGORIES: SKIBIDI, SIGMA, OHIO, |
# | AND RIZZ.                              |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | number             | integer   |
# +--------------------+-----------+

def countCircles(n: int) -> int:
    """ Description: `[FUNCTION] countCircles` """
    # +------------------------------------------------+
    # | FUNCTION <Count Circles in a Digit>            |
    # +------------------------------------------------+
    # | COUNTS THE NUMBER OF "CIRCLES" IN A SINGLE     |
    # | DIGIT (E.G., 0, 6, 9 HAVE 1 CIRCLE; 8 HAS 2).  |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | n                  | integer   |
    # | circles            | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # INITIALIZE CIRCLES COUNT TO 0.
    circles: int = 0
    # CHECK FOR DIGITS WITH ONE CIRCLE.
    if n == 0 or n == 6 or n == 9:
        circles = 1
    # CHECK FOR DIGITS WITH TWO CIRCLES.
    elif n == 8:
        circles = 2
    # RETURN THE COUNT OF CIRCLES.
    return circles

def classifyNumber(number: int) -> str:
    """ Description: `[FUNCTION] classifyNumber` """
    # +------------------------------------------------+
    # | FUNCTION <Classify Number>                     |
    # +------------------------------------------------+
    # | CLASSIFIES A FOUR-DIGIT NUMBER INTO CATEGORIES |
    # | BASED ON THE SUM OF CIRCLES IN ITS DIGITS AND  |
    # | THE SUM OF CIRCLES IN THE DIGITS OF ITS SUM.   |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | number             | integer   |
    # | d1                 | integer   |
    # | d2                 | integer   |
    # | d3                 | integer   |
    # | d4                 | integer   |
    # | number_circle_sum  | integer   |
    # | digit_sum          | integer   |
    # | d1_sum             | integer   |
    # | d2_sum             | integer   |
    # | sum_circle_sum     | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # EXTRACT EACH DIGIT OF THE FOUR-DIGIT NUMBER.
    d1: int = number // 1000
    d2: int = (number // 100) % 10
    d3: int = (number // 10) % 10
    d4: int = number % 10

    # CALCULATE THE SUM OF CIRCLES IN THE ORIGINAL NUMBER'S DIGITS.
    number_circle_sum: int = countCircles(d1) + countCircles(d2) + countCircles(d3) + countCircles(d4)
    # CALCULATE THE SUM OF THE ORIGINAL NUMBER'S DIGITS.
    digit_sum: int = d1 + d2 + d3 + d4

    # EXTRACT EACH DIGIT OF THE SUM OF DIGITS.
    d1_sum: int = digit_sum // 10
    d2_sum: int = digit_sum % 10
    
    # CALCULATE THE SUM OF CIRCLES IN THE DIGITS OF THE SUM OF DIGITS.
    sum_circle_sum: int = countCircles(d1_sum) + countCircles(d2_sum)

    # CLASSIFY THE NUMBER BASED ON THE CALCULATED SUMS OF CIRCLES.
    if number_circle_sum == 0:
        if sum_circle_sum > 0:
            return "Ohio"
        else:
            return "Skibidi"
    else:
        if sum_circle_sum > 0:
            return "Rizz"
        else:
            return "Sigma"

""" PROGRAM ALGORITHM """
# GET A FOUR-DIGIT NUMBER FROM THE USER.
number: int = int(input("Masukkan sebuah bilangan: "))
# CLASSIFY THE NUMBER.
result: str = classifyNumber(number)
# PRINT THE CLASSIFICATION RESULT.
print(f"Bilangan tersebut adalah bilangan {result}.")
