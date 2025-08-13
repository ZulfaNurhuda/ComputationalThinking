""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Palindrome Checker>           |
# +----------------------------------------+
# | READS A STRING AND DETERMINES IF IT IS |
# | A PALINDROME.                          |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | string_length      | INTEGER   |
# | input_string       | STRING    |
# | reversed_string    | STRING    |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# READ THE INPUT STRING FROM USER
# PROMPT USER TO ENTER A STRING FOR PALINDROME CHECKING
input_string: str = input("Masukkan string: ")

# CONVERT TO LOWERCASE FOR CASE-INSENSITIVE COMPARISON
# NORMALIZE STRING TO LOWERCASE TO IGNORE CASE DIFFERENCES
lowercase_string: str = input_string.lower()

# CHECK IF THE STRING IS A PALINDROME
# INITIALIZE FLAG TO TRACK PALINDROME STATUS (ASSUME TRUE INITIALLY)
is_palindrome_flag: bool = True
# GET THE LENGTH OF THE STRING FOR ITERATION BOUNDS
string_length: int = len(lowercase_string)

# COMPARE CHARACTERS FROM BOTH ENDS MOVING TOWARDS CENTER
# ONLY NEED TO CHECK HALF THE STRING (MIDDLE CHAR DOESN'T MATTER FOR ODD LENGTH)
for i in range(string_length // 2):
    # COMPARE CHARACTER AT POSITION i WITH CHARACTER AT MIRROR POSITION
    # IF ANY PAIR DOESN'T MATCH, IT'S NOT A PALINDROME
    if lowercase_string[i] != lowercase_string[string_length - 1 - i]:
        # SET FLAG TO FALSE AND EXIT LOOP EARLY
        is_palindrome_flag = False
        break

# PRINT THE RESULT BASED ON PALINDROME CHECK
# IF FLAG IS TRUE, STRING IS A PALINDROME
if is_palindrome_flag:
    print(f"\"{input_string}\" adalah palindrom")
else:
    # IF FLAG IS FALSE, STRING IS NOT A PALINDROME
    print(f"\"{input_string}\" bukan palindrom")
