""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Number Triangle Pattern>      |
# +----------------------------------------+
# | GENERATES A NUMBER TRIANGLE PATTERN    |
# | BASED ON A GIVEN INTEGER N.            |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | number_input       | INTEGER   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT THE NUMBER N FROM USER
# PROMPT USER TO ENTER A NUMBER AND CONVERT STRING INPUT TO INTEGER
number_input: int = int(input("Masukkan N: "))

# GENERATE AND PRINT THE NUMBER TRIANGLE PATTERN
# OUTER LOOP: ITERATE FROM 1 TO N (INCLUSIVE) FOR EACH ROW
for i in range(1, number_input + 1):
    # INNER LOOP: PRINT NUMBERS FROM 1 TO CURRENT ROW NUMBER
    # FOR ROW i, PRINT NUMBERS 1, 2, 3, ..., i
    for j in range(1, i + 1):
        # PRINT CURRENT NUMBER FOLLOWED BY A SPACE (NO NEWLINE)
        print(j, end=" ")
    # PRINT NEWLINE AFTER EACH ROW TO MOVE TO NEXT LINE
    print("") # NEWLINE
