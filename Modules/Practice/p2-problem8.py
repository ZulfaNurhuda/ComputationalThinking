""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Prime Factor Finder>          |
# +----------------------------------------+
# | FINDS AND PRINTS THE PRIME FACTORS OF  |
# | A GIVEN INTEGER N IN ASCENDING ORDER.  |
# +----------------------------------------+

# +------------------------+-----------+
# | PROGRAM DICTIONARY     | DATA TYPE |
# +------------------------+-----------+
# | number_input           | INTEGER   |
# | divisor                | INTEGER   |
# | prime_factors          | LIST      |
# +------------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT THE NUMBER N FROM USER
# PROMPT USER TO ENTER THE NUMBER TO FIND PRIME FACTORS
number_input: int = int(input("Masukkan N: "))

# INITIALIZE LIST TO STORE UNIQUE PRIME FACTORS
# CREATE EMPTY LIST TO COLLECT PRIME FACTORS WITHOUT DUPLICATES
prime_factors: list[int] = []
# START WITH SMALLEST PRIME NUMBER AS DIVISOR
divisor: int = 2

# FIND PRIME FACTORS AND STORE IN LIST
# ITERATE THROUGH POTENTIAL DIVISORS UP TO SQRT(number_input)
while divisor * divisor <= number_input:
    # CHECK IF CURRENT DIVISOR IS A FACTOR
    if number_input % divisor == 0:
        # DIVIDE OUT ALL OCCURRENCES OF THIS PRIME FACTOR
        while number_input % divisor == 0:
            # ADD PRIME FACTOR TO LIST IF NOT ALREADY PRESENT
            if divisor not in prime_factors: prime_factors += [divisor] # ADD PRIME FACTOR IF NOT YET ADDED
            # DIVIDE number_input BY THE PRIME FACTOR
            number_input //= divisor
    # MOVE TO NEXT POTENTIAL DIVISOR
    divisor += 1

# HANDLE REMAINING PRIME FACTOR (IF ANY)
# IF number_input > 1, IT'S A PRIME FACTOR LARGER THAN SQRT(ORIGINAL NUMBER)
if number_input > 1 and (number_input not in prime_factors): # REMAINING number_input IS A PRIME FACTOR AND NOT YET ADDED
    # ADD THE REMAINING PRIME FACTOR TO THE LIST
    prime_factors += [number_input]

# PRINT THE RESULT IN FORMATTED OUTPUT
# DISPLAY HEADER MESSAGE FOR PRIME FACTORS
print("Faktor primanya adalah: ", end="")
# ITERATE THROUGH ALL PRIME FACTORS IN THE LIST
for i in range(len(prime_factors)):
    # PRINT CURRENT PRIME FACTOR
    print(prime_factors[i], end="")
    # ADD COMMA AND SPACE BETWEEN FACTORS (EXCEPT FOR LAST ONE)
    if i < len(prime_factors) - 1:
        print(", ", end="")
# PRINT PERIOD TO END THE OUTPUT
print(".")
