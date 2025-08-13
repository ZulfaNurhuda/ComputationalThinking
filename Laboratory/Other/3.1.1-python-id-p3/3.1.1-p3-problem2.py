""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Secret Message>               |
# +----------------------------------------+
# | CONVERTS A MESSAGE TO A NUMBER AND     |
# | DETERMINES THE FATE OF MISS DEB.       |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | message            | string    |
# +--------------------+-----------+

def convertMessage(message: str) -> int:
    """ Description: `[FUNCTION] convertMessage` """
    # +-------------------------------------------------+
    # | FUNCTION <Convert Message>                      |
    # +-------------------------------------------------+
    # | ACCEPTS A STRING MESSAGE AND RETURNS AN INTEGER |
    # | REPRESENTING THE CONVERTED NUMERICAL VALUE.     |
    # +-------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | message            | string    |
    # | total              | integer   |
    # | letter             | string    |
    # | value              | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # INITIALIZE TOTAL TO 0.
    total: int = 0
    # ITERATE THROUGH EACH LETTER IN THE MESSAGE (CONVERTED TO LOWERCASE).
    for letter in message.lower():
        # CHECK IF THE CHARACTER IS A LETTER.
        if 'a' <= letter <= 'z':
            # GET THE NUMERICAL VALUE OF THE LETTER (A=0, B=1, ...).
            value: int = ord(letter) - ord('a')
            # IF THE LETTER IS A VOWEL, MULTIPLY ITS VALUE BY 2.
            if letter in "aiueo":
                total += value * 2
            # OTHERWISE, ADD ITS VALUE.
            else:
                total += value
    # RETURN THE TOTAL SUM.
    return total

def checkFate(total: int) -> None:
    """ Description: `[PROCEDURE] checkFate` """
    # +------------------------------------------------+
    # | PROCEDURE <Check Fate>                         |
    # +------------------------------------------------+
    # | ACCEPTS AN INTEGER TOTAL AND PRINTS THE FATE   |
    # | OF MISS DEB BASED ON WHETHER THE TOTAL IS EVEN |
    # | OR ODD.                                        |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | total              | integer   |
    # +--------------------+-----------+

    """ PROCEDURE ALGORITHM """
    # IF THE TOTAL IS EVEN, MISS DEB IS SAFE.
    if total % 2 == 0:
        print("Nona Deb selamat dari bahaya.")
    # IF THE TOTAL IS ODD, MISS DEB IS NOT SAFE.
    else:
        print("Nona Deb tidak selamat dari bahaya.")

""" PROGRAM ALGORITHM """
# GET THE SECRET MESSAGE FROM THE USER.
message: str = input("Masukkan pesan misteri: ")
# CONVERT THE MESSAGE TO A NUMBER.
total: int = convertMessage(message)
# CHECK AND PRINT THE FATE.
checkFate(total)