""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Quadratic Equation>           |
# +----------------------------------------+
# | CALCULATES THE DISCRIMINANT AND        |
# | DETERMINES THE NATURE OF THE ROOTS OF  |
# | A QUADRATIC EQUATION.                  |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | a                  | float     |
# | b                  | float     |
# | c                  | float     |
# | d                  | float     |
# +--------------------+-----------+

def calculateDiscriminant(a: float, b: float, c: float) -> float:
    """ Description: `[FUNCTION] calculateDiscriminant` """
    # +-------------------------------------------------+
    # | FUNCTION <Calculate Discriminant>               |
    # +-------------------------------------------------+
    # | ACCEPTS 3 REAL NUMBERS A, B, AND C WHICH ARE    |
    # | THE COEFFICIENTS OF A QUADRATIC EQUATION, THEN  |
    # | RETURNS THE DISCRIMINANT VALUE OF THE QUADRATIC |
    # | EQUATION.                                       |
    # +-------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | a                  | float     |
    # | b                  | float     |
    # | c                  | float     |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # CALCULATE THE DISCRIMINANT USING THE FORMULA B^2 - 4AC.
    return b ** 2 - 4 * a * c

def checkRoots(d: float) -> None:
    """ Description: `[PROCEDURE] checkRoots` """
    # +------------------------------------------------+
    # | PROCEDURE <Check Root Type>                    |
    # +------------------------------------------------+
    # | ACCEPTS A REAL NUMBER D WHICH IS THE           |
    # | DISCRIMINANT VALUE OF A QUADRATIC EQUATION,    |
    # | THEN OUTPUTS INFORMATION ON WHETHER THE        |
    # | QUADRATIC EQUATION HAS DISTINCT REAL ROOTS,    |
    # | TWIN REAL ROOTS, OR NO REAL ROOTS.             |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | d                  | float     |
    # +--------------------+-----------+

    """ PROCEDURE ALGORITHM """
    # CHECK THE VALUE OF THE DISCRIMINANT TO DETERMINE THE NATURE OF THE ROOTS.
    if d > 0:
        # IF D > 0, THE EQUATION HAS TWO DISTINCT REAL ROOTS.
        print("Persamaan kuadrat memiliki akar real berbeda.")
    elif d == 0:
        # IF D = 0, THE EQUATION HAS TWO EQUAL REAL ROOTS (TWIN ROOTS).
        print("Persamaan kuadrat memiliki akar kembar.")
    else:
        # IF D < 0, THE EQUATION HAS NO REAL ROOTS (COMPLEX ROOTS).
        print("Persamaan kuadrat tidak memiliki akar real.")

""" PROGRAM ALGORITHM """
# GET THE COEFFICIENTS OF THE QUADRATIC EQUATION FROM THE USER.
a: float = float(input("Masukkan nilai a: "))
b: float = float(input("Masukkan nilai b: "))
c: float = float(input("Masukkan nilai c: "))

# CALCULATE THE DISCRIMINANT.
d: float = calculateDiscriminant(a, b, c)

# PRINT THE DISCRIMINANT VALUE.
print(f"Nilai diskriminan: {d:.2f}")
# CHECK AND PRINT THE NATURE OF THE ROOTS.
checkRoots(d)