""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Smallest Power of 10>         |
# +----------------------------------------+
# | FINDS THE SMALLEST POWER OF 10 THAT IS |
# | GREATER THAN A GIVEN INTEGER N.        |
# +----------------------------------------+

# +------------------------+-----------+
# | PROGRAM DICTIONARY     | DATA TYPE |
# +------------------------+-----------+
# | number_input           | INTEGER   |
# | smallest_power_of_10   | INTEGER   |
# +------------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT THE NUMBER N FROM USER
# PROMPT USER TO ENTER A NUMBER AND CONVERT STRING INPUT TO INTEGER
number_input: int = int(input("Masukkan N: "))

# FIND THE SMALLEST POWER OF 10 GREATER THAN N USING ITERATIVE APPROACH
# INITIALIZE POWER OF 10 STARTING FROM 1 (10^0)
smallest_power_of_10: int = 1
# KEEP MULTIPLYING BY 10 UNTIL WE FIND A POWER GREATER THAN INPUT
# LOOP CONTINUES WHILE CURRENT POWER IS LESS THAN OR EQUAL TO INPUT
while smallest_power_of_10 <= number_input:
    # MULTIPLY BY 10 TO GET NEXT POWER (1 -> 10 -> 100 -> 1000 -> ...)
    smallest_power_of_10 *= 10

# PRINT THE RESULT - THE SMALLEST POWER OF 10 GREATER THAN INPUT
# OUTPUT THE POWER OF 10 THAT IS JUST LARGER THAN THE INPUT NUMBER
print(smallest_power_of_10)
