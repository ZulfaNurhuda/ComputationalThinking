""" PROGRAM DESCRIPTION """
# +------------------------------------------+
# | PROGRAM <Word Analysis>                  |
# +------------------------------------------+
# | Analyzes a word to find missing letters  |
# | and count the number of unique letters.  |
# +------------------------------------------+

# +-------------------+-----------------+
# | PROGRAM DICTIONARY| DATA TYPE       |
# +-------------------+-----------------+
# | word              | string          |
# +-------------------+-----------------+

def findMissingLetters(word: str) -> None:
    """ Description: `[PROCEDURE] findMissingLetters` """
    # +------------------------------------+
    # | PROCEDURE <Find Missing Letters>   |
    # +------------------------------------+
    # | Finds which letters are missing    |
    # | based on the word obtained from    |
    # | user input.                        |
    # +------------------------------------+

    # +-------------------+-----------+
    # | LOCAL DICTIONARY  | DATA TYPE |
    # +-------------------+-----------+
    # | word              | string    |
    # | existing_letters  | string    |
    # | alphabet          | string    |
    # | missing_letters   | string    |
    # +-------------------+-----------+

    """ PROCEDURE ALGORITHM """
    # FIND ALL THE LETTERS THAT ARE IN THE WORD
    existing_letters: str = ""
    for letter in word:
        if letter not in existing_letters:
            existing_letters += letter

    # INITIALIZE ALL ALPHABET LETTERS
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"

    # FIND THE MISSING LETTERS BY COMPARING ALL LETTERS WITH THE LETTERS IN THE WORD
    missing_letters: str = ""
    for letter in alphabet:
        if letter not in existing_letters:
            missing_letters += letter

    # PRINT INFORMATION ABOUT WHICH LETTERS ARE MISSING
    print(f"Huruf yang hilang: {missing_letters}")

def countUniqueLetters(word: str) -> None:
    """ Description: `[PROCEDURE] countUniqueLetters` """
    # +-------------------------------------------+
    # | PROCEDURE <Count Unique Letters>          |
    # +-------------------------------------------+
    # | Counts the number of unique letters based |
    # | on the word obtained from user input.     |
    # +-------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | word               | string    |
    # | unique_letters_data| string    |
    # | unique_letters_sum | integer   |
    # +--------------------+-----------+

    """ PROCEDURE ALGORITHM """
    # FIND UNIQUE LETTERS (TO AVOID DUPLICATE LETTERS)
    unique_letters_data: str = ""
    for letter in word:
        if letter not in unique_letters_data:
            unique_letters_data += letter

    # COUNT THE NUMBER OF UNIQUE LETTERS
    unique_letters_sum: int = 0
    for _ in unique_letters_data:
        unique_letters_sum += 1

    # PRINT INFORMATION ABOUT THE NUMBER OF UNIQUE LETTERS
    print(f"Jumlah huruf unik: {unique_letters_sum}")

""" PROGRAM ALGORITHM """
# INPUT WORD
word: str = str(input("Masukkan kata: "))

# EXECUTE PROCEDURES
findMissingLetters(word)
countUniqueLetters(word)
