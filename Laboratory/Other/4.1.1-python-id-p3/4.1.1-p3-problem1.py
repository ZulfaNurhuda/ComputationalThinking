""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Practical Assignment Grading> |
# +----------------------------------------+
# | Automates the practical assignment     |
# | grading process.                       |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | a                  | float     |
# | b                  | float     |
# | c                  | float     |
# | problem1           | float     |
# | problem2           | float     |
# | problem3           | float     |
# +--------------------+-----------+

def checkValid(a: float, b: float, c: float) -> bool:
    """ Description: `[FUNCTION] checkValid` """
    # +-------------------------------------------------+
    # | FUNCTION <Weight Validation>                    |
    # +-------------------------------------------------+
    # | Accepts 3 real numbers (a, b, and c) and checks |
    # | whether the weights are valid or not (their sum |
    # | must be 1 and they must be within the range     |
    # | 0 to 1).                                        |
    # +-------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | a                  | float     |
    # | b                  | float     |
    # | c                  | float     |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # CHECK IF ALL WEIGHTS ARE WITHIN VALID RANGE [0, 1]
    # AND VERIFY THAT THE SUM OF ALL WEIGHTS EQUALS 1
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1 and a + b + c == 1

def calculate(a: float, b: float, c: float, problem1: float, problem2: float, problem3: float) -> None:
    """ Description: `[PROCEDURE] calculate` """
    # +------------------------------------------------+
    # | PROCEDURE <Calculate Grade>                    |
    # +------------------------------------------------+
    # | Accepts 6 real numbers, where 3 are weights    |
    # | (a, b, and c) and the other 3 are the scores   |
    # | for each problem. This subprogram will         |
    # | calculate the practical assignment grade if the|
    # | weights are valid, and output "invalid weights"|
    # | if the weights are not valid.                  |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | a                  | float     |
    # | b                  | float     |
    # | c                  | float     |
    # | problem1           | float     |
    # | problem2           | float     |
    # | problem3           | float     |
    # | grade              | float     |
    # +--------------------+-----------+

    """ PROCEDURE ALGORITHM """
    # VALIDATE WEIGHTS USING "checkValid" FUNCTION
    if checkValid(a, b, c):
        # CALCULATE WEIGHTED AVERAGE OF THREE PROBLEM SCORES
        grade: float = a * problem1 + b * problem2 + c * problem3
        # DISPLAY FINAL GRADE WITH 2 DECIMAL PLACES
        print(f"Nilai tugas praktikum adalah {grade:.2f}")
    else:
        # DISPLAY ERROR MESSAGE FOR INVALID WEIGHTS
        print("bobot tidak valid")

""" PROGRAM ALGORITHM """
# INPUT SECTION: GET WEIGHT VALUES FROM USER
a: float = float(input("Masukkan nilai a: "))  # WEIGHT FOR PROBLEM 1
b: float = float(input("Masukkan nilai b: "))  # WEIGHT FOR PROBLEM 2
c: float = float(input("Masukkan nilai c: "))  # WEIGHT FOR PROBLEM 3

# INPUT SECTION: GET PROBLEM SCORES FROM USER
problem1: float = float(input("Masukkan nilai soal 1: "))  # SCORE FOR PROBLEM 1
problem2: float = float(input("Masukkan nilai soal 2: "))  # SCORE FOR PROBLEM 2
problem3: float = float(input("Masukkan nilai soal 3: "))  # SCORE FOR PROBLEM 3

# PROCESSING SECTION: CALCULATE AND DISPLAY FINAL GRADE
calculate(a, b, c, problem1, problem2, problem3)
