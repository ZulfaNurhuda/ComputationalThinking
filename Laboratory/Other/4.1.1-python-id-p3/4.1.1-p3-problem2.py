""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Secret Message>               |
# +----------------------------------------+
# | Converts a message to a number and     |
# | determines the fate of Miss Deb.       |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | message            | string    |
# +--------------------+-----------+

def convertMessage(message: str) -> int:
    """ Description: `[FUNCTION] convertMessage` """
    # +------------------------------------------------+
    # | FUNCTION <Convert Message>                     |
    # +------------------------------------------------+
    # | Converts a message to a number and determines  |
    # | the fate of Miss Deb.                          |
    # +------------------------------------------------+

    # +--------------------+---------------------------------+
    # | LOCAL DICTIONARY   | DATA TYPE                       |
    # +--------------------+---------------------------------+
    # | message            | string                          |
    # | total              | integer                         |
    # | alphabet           | dictionary of string to integer |
    # | vowels             | list of string                  |
    # | letter             | string                          |
    # | value              | integer                         |
    # +--------------------+---------------------------------+

    """ FUNCTION ALGORITHM """
    # INITIALIZE TOTAL COUNTER TO ZERO
    total: int = 0

    # CREATE DICTIONARY TO MAP EACH LETTER TO ITS POSITION IN THE ALPHABET
    alphabet: dict[str, int] = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 
        'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 
        'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 
        'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
        'X': 23, 'Y': 24, 'Z': 25
    }

    # CREATE LIST OF VOWELS (A, I, U, E, O)
    vowels: list[str] = ["A", "I", "U", "E", "O"]
    
    # ITERATE THROUGH EACH CHARACTER IN MESSAGE
    for letter in message:
        # CALCULATE LETTER VALUE (A=0, B=1, C=2, etc.)
        value: int = alphabet[letter]
        
        # DOUBLE THE VALUE FOR VOWELS (A, I, U, E, O)
        if letter in vowels:
            total += value * 2  # VOWEL BONUS: MULTIPLY BY 2
        else:
            total += value      # CONSONANT: ADD NORMAL VALUE
    
    # RETURN FINAL CALCULATED TOTAL
    return total

def checkFate(total: int) -> None:
    """ Description: `[PROCEDURE] checkFate` """
    # +------------------------------------------------+
    # | PROCEDURE <Check Fate>                         |
    # +------------------------------------------------+
    # | Determines the fate of Miss Deb based on the   |
    # | total number.                                  |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | total              | integer   |
    # +--------------------+-----------+

    """ PROCEDURE ALGORITHM """
    # CHECK IF TOTAL IS EVEN OR ODD TO DETERMINE FATE
    if total % 2 == 0:
        # EVEN NUMBER: MISS DEB IS SAFE
        print("Nona Deb selamat dari bahaya.")
    else:
        # ODD NUMBER: MISS DEB IS IN DANGER
        print("Nona Deb tidak selamat dari bahaya.")

""" PROGRAM ALGORITHM """
# INPUT SECTION: GET SECRET MESSAGE FROM USER
message: str = input("Masukkan pesan misteri: ")

# PROCESSING SECTION: CONVERT MESSAGE TO NUMERICAL VALUE
total: int = convertMessage(message)

# OUTPUT SECTION: DETERMINE AND DISPLAY MISS DEB'S FATE
checkFate(total)
