""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Heart Shape Printer>          |
# +----------------------------------------+
# | PRINTS A HEART SHAPE USING '*'         |
# | CHARACTERS BASED ON A GIVEN            |
# | MATHEMATICAL INEQUALITY.               |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | y_coord            | INTEGER   |
# | x_coord            | INTEGER   |
# | value              | FLOAT     |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# ITERATE THROUGH Y-COORDINATES FROM TOP TO BOTTOM
# START FROM Y=15 AND GO DOWN TO Y=-15 (STEP -1)
for y_coord in range(15, -16, -1):
    # ITERATE THROUGH X-COORDINATES FROM LEFT TO RIGHT
    # START FROM X=-30 AND GO TO X=30 (STEP 1)
    for x_coord in range(-30, 31, 1):
        # CALCULATE VALUE BASED ON HEART INEQUALITY FORMULA
        # HEART EQUATION: ((x/2)^2) + ((5y/4) - (2*sqrt(|x|)))^2 <= 120
        value: float = ((x_coord / 2) ** 2) + ((5 * y_coord / 4) - (2 * (abs(x_coord) ** 0.5))) ** 2
        # DETERMINE CHARACTER TO PRINT BASED ON INEQUALITY RESULT
        # IF VALUE <= 120, POINT IS INSIDE HEART SHAPE
        if value <= 120:
            # PRINT ASTERISK FOR POINTS INSIDE HEART
            print("*", end="")
        else:
            # PRINT SPACE FOR POINTS OUTSIDE HEART
            print(" ", end="")
    # PRINT NEWLINE TO COMPLETE THE CURRENT ROW
    # MOVE TO NEXT LINE AFTER PROCESSING ALL X-COORDINATES
    print("")