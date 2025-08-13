""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Recursive Pattern Generator>  |
# +----------------------------------------+
# | GENERATES A RECURSIVE PATTERN BASED ON |
# | TWO INPUT CHARACTERS AND A GIVEN       |
# | LEVEL 'N'.                             |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | char_one           | STRING    |
# | char_two           | STRING    |
# | level_n            | INTEGER   |
# | result_pattern     | STRING    |
# +--------------------+-----------+

def generatePattern(c1: str, c2: str, n: int) -> str:
    """ Description: `[FUNCTION] generatePattern` """
    # +----------------------------------------------------+
    # | FUNCTION <Generate Pattern>                        |
    # +----------------------------------------------------+
    # | RECURSIVELY GENERATES THE PATTERN.                 |
    # +----------------------------------------------------+

    # +------------------------+-----------+
    # | LOCAL DICTIONARY       | DATA TYPE |
    # +------------------------+-----------+
    # | c1                     | STRING    |
    # | c2                     | STRING    |
    # | n                      | INTEGER   |
    # | previous_pattern       | STRING    |
    # | complement_of_previous | STRING    |
    # | char                   | STRING    |
    # +------------------------+-----------+

    """ FUNCTION ALGORITHM """
    # BASE CASE: IF N IS 0, RETURN FIRST CHARACTER
    if n == 0: return c1
    
    # RECURSIVELY CALL TO GET THE PREVIOUS PATTERN
    # GET PATTERN FOR LEVEL (n-1) TO BUILD CURRENT LEVEL
    previous_pattern: str = generatePattern(c1, c2, n - 1)
    
    # CREATE THE COMPLEMENT OF THE PREVIOUS PATTERN
    # INITIALIZE EMPTY STRING FOR COMPLEMENT PATTERN
    complement_of_previous: str = ""
    # ITERATE THROUGH EACH CHARACTER IN PREVIOUS PATTERN
    for char in previous_pattern:
        # IF CHARACTER IS c1, REPLACE WITH c2 IN COMPLEMENT
        if char == c1:
            complement_of_previous += c2
        else:
            # IF CHARACTER IS c2, REPLACE WITH c1 IN COMPLEMENT
            complement_of_previous += c1
    
    # RETURN CONCATENATION OF PREVIOUS PATTERN AND ITS COMPLEMENT
    # CURRENT PATTERN = PREVIOUS + COMPLEMENT_OF_PREVIOUS
    return previous_pattern + complement_of_previous

""" PROGRAM ALGORITHM """
# INPUT THE TWO CHARACTERS AND THE LEVEL N FROM USER
# PROMPT USER TO ENTER THE FIRST CHARACTER FOR PATTERN
char_one: str = input("Masukkan karakter 1: ")
# PROMPT USER TO ENTER THE SECOND CHARACTER FOR PATTERN
char_two: str = input("Masukkan karakter 2: ")
# PROMPT USER TO ENTER THE RECURSION LEVEL N
level_n: int = int(input("Masukkan nilai n: "))

# GENERATE THE PATTERN USING RECURSIVE FUNCTION
# CALL "generatePattern" FUNCTION WITH USER INPUT PARAMETERS
result_pattern: str = generatePattern(char_one, char_two, level_n)

# PRINT THE RESULT IN FORMATTED OUTPUT
# DISPLAY THE GENERATED PATTERN TO USER
print(f"Pola yang didapat: {result_pattern}")
