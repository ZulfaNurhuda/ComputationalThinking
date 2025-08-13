""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Quadratic Function Calculator>|
# +----------------------------------------+
# | CALCULATES AND PRINTS THE VALUES OF A  |
# | QUADRATIC FUNCTION F(X) = X^2 - 2X + 5 |
# | FOR A GIVEN RANGE [A, B].              |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | A                  | INTEGER   |
# | B                  | INTEGER   |
# +--------------------+-----------+

def calculateQuadratic(x: int) -> int:
    """ Description: `[FUNCTION] calculateQuadratic` """
    # +----------------------------------------------------+
    # | FUNCTION <Calculate Quadratic>                     |
    # +----------------------------------------------------+
    # | CALCULATES THE VALUE OF THE QUADRATIC FUNCTION     |
    # | F(X) = X^2 - 2X + 5.                               |
    # +----------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | x                  | INTEGER   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # CALCULATE QUADRATIC FUNCTION: F(X) = X^2 - 2X + 5
    # RETURN THE RESULT OF THE QUADRATIC FORMULA
    return x ** 2 - 2 * x + 5

""" PROGRAM ALGORITHM """
# INPUT THE RANGE START (A) AND END (B) FROM USER
# PROMPT USER TO ENTER THE STARTING VALUE OF THE RANGE
A: int = int(input("Masukkan A: "))
# PROMPT USER TO ENTER THE ENDING VALUE OF THE RANGE
B: int = int(input("Masukkan B: "))

# CALCULATE AND PRINT FUNCTION VALUES FOR THE GIVEN RANGE
# ITERATE THROUGH ALL INTEGER VALUES FROM A TO B (INCLUSIVE)
for i in range(A, B + 1):
    # CALL "calculateQuadratic" FUNCTION AND PRINT RESULT
    # FORMAT OUTPUT AS f(x) = result
    print(f"f({i}) = {calculateQuadratic(i)}")
