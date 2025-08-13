""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Decrypting Encryption Code>   |
# +----------------------------------------+
# | Decrypts messages based on             |
# | predetermined rules.                   |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | encrypted_word     | string    |
# | decrypted_word     | string    |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
def findOriginalNumberFromEncryptedNumber(number: str) -> int:
    """ Description: `[FUNCTION] findOriginalNumberFromEncryptedNumber` """
    # +------------------------------------------------+
    # | FUNCTION <Find Original Number From Encrypted> |
    # +------------------------------------------------+
    # | Finds the actual number from the encrypted     |
    # | message based on predetermined rules.          |
    # +------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | number             | string    |
    # | encrypted_number   | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # CONVERT ENCRYPTED NUMBER TO INTEGER
    encrypted_number: int = int(number)

    # PROCESS WITH PREDETERMINED CONDITIONS
    if encrypted_number % 2 == 0:
        return encrypted_number // 2
    else:
        return encrypted_number // 3

def convertEncryptedNumberToLetter(encrypted_word: str) -> str:
    """ Description: `[FUNCTION] convertEncryptedNumberToLetter` """
    # +------------------------------------------------+
    # | FUNCTION <Convert Encrypted Number To Letter>  |
    # +------------------------------------------------+
    # | Finds the actual letter message from the       |
    # | encrypted message.                             |
    # +------------------------------------------------+

    # +--------------------+-----------------+
    # | LOCAL DICTIONARY   | DATA TYPE       |
    # +--------------------+-----------------+
    # | encrypted_word     | string          |
    # | word_length        | integer         |
    # | decrypted_word     | string          |
    # | i                  | integer         |
    # | latin_letters      | list of string  |
    # | original_encrypted_number | integer  |
    # +--------------------+-----------------+

    """ FUNCTION ALGORITHM """
    # FIND WORD LENGTH
    word_length: int = 0

    for i in encrypted_word:
        word_length += 1

    # INITIALIZE DECRYPTED_WORD TO STORE THE DECRYPTED MESSAGE
    decrypted_word: str = ""

    # ITERATE FOR EVERY 2 CHARACTERS IN ENCRYPTED_WORD TO PERFORM DECRYPTION
    for i in range(0, word_length, 2):
        latin_letters: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # USE "findOriginalNumberFromEncryptedNumber" FUNCTION TO FIND THE ORIGINAL NUMBER
        original_encrypted_number: int = findOriginalNumberFromEncryptedNumber(
            encrypted_word[i] + encrypted_word[i + 1]
        )

        decrypted_word += latin_letters[original_encrypted_number - 1]

    # RETURN DATA IN THE FORM OF THE DECRYPTED MESSAGE
    return decrypted_word

""" PROGRAM ALGORITHM """
# INPUT ENCRYPTED SECRET MESSAGE
encrypted_word: str = str(input("Pesan rahasia: "))

# USE "convertEncryptedNumberToLetter" FUNCTION TO DECRYPT THE MESSAGE
decrypted_word: str = convertEncryptedNumberToLetter(encrypted_word)

# PRINT INFORMATION FROM THE DECRYPTED MESSAGE
print(f"Pesan rahasia dari Tuan Leo adalah {decrypted_word}")