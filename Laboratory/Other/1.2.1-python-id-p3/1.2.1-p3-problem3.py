""" PROGRAM DESCRIPTION """
# +-------------------------------------------------------+
# | PROGRAM <Print Words With Important Information>      |
# +-------------------------------------------------------+
# | Prints words with the conditions:                     |
# | 1. The word is the most frequently occurring.         |
# | 2. The word is a palindrome                           |
# | (e.g., KAKAK = KAKAK when reversed)                   |
# +-------------------------------------------------------+

# +--------------------+--------------+
# | PROGRAM DICTIONARY | DATA TYPE    |
# +--------------------+--------------+
# | word_count         | integer      |
# | text               | string       |
# +--------------------+--------------+

def wordFrequency(text: str, word_to_find: str) -> int:
    """ Description: `[FUNCTION] wordFrequency` """
    # +------------------------------------------------+ 
    # | FUNCTION <Find Frequency of Occurrence>        |
    # +------------------------------------------------+ 
    # | Finds the frequency of occurrence of a word in |
    # | a text obtained from user input.               |
    # +------------------------------------------------+ 

    # +--------------------+--------------+
    # | LOCAL DICTIONARY   | DATA TYPE    |
    # +--------------------+--------------+
    # | text               | string       |
    # | word_to_find       | string       |
    # | text_array         | list[string] |
    # | per_word           | string       |
    # | word_to_find_count | integer      |
    # +--------------------+--------------+

    """ FUNCTION ALGORITHM """
    # PARSE THE TEXT INTO AN ARRAY CONTAINING EACH WORD IN THE TEXT
    text_array: list[str] = []
    per_word: str = ""
    for letter in (text + " "):
        if letter != " ":
            per_word += letter
        else:
            text_array += [per_word]
            per_word = ""

    # COUNT THE NUMBER OF TIMES THE WORD APPEARS IN THE TEXT
    word_to_find_count: int = 0
    for word in text_array:
        if word == word_to_find:
            word_to_find_count += 1

    # RETURN FUNCTION RESULT
    return word_to_find_count

def isPalindrome(word: str) -> bool:
    """ Description: `[FUNCTION] isPalindrome` """
    # +-------------------------------------+ 
    # | FUNCTION <Determine Palindrome>     |
    # +-------------------------------------+ 
    # | Determines whether a word is a      |
    # | palindrome or not.                  |
    # | A palindrome is a word that when    |
    # | its letter order is reversed, it    |
    # | still reads the same.               |
    # +-------------------------------------+ 

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | word               | string    |
    # | word_length        | integer   |
    # | reversed_word      | string    |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    # FIND THE LENGTH OF THE WORD TO BE USED FOR ITERATION
    word_length: int = 0
    for _ in word:
        word_length += 1

    # REVERSE THE ORDER OF THE WORD WITH BACKWARD ITERATION
    reversed_word: str = ""
    for i in range(word_length - 1, -1, -1):
        reversed_word += word[i]

    # RETURN FUNCTION RESULT (COMPARISON OF THE WORD AND THE REVERSED WORD)
    return word == reversed_word

def printWord(text: str) -> None:
    """ Description: `[PROCEDURE] printWord` """
    # +------------------------------------+ 
    # | PROCEDURE <Print Specific Words>   |
    # +------------------------------------+ 
    # | Prints a word if it appears most   |
    # | frequently or is a palindrome.     |
    # +------------------------------------+ 

    # +--------------------+--------------+
    # | LOCAL DICTIONARY   | DATA TYPE    |
    # +--------------------+--------------+
    # | text               | string       |
    # | text_array         | list[string] |
    # | per_word           | string       |
    # | max_frequency      | integer      |
    # | important_info     | string       |
    # +--------------------+--------------+

    """ PROCEDURE ALGORITHM """
    # PARSE THE TEXT INTO AN ARRAY CONTAINING EACH WORD IN THE TEXT
    text_array: list[str] = []
    per_word: str = ""
    for letter in (text + " "):
        if letter != " ":
            per_word += letter
        else:
            text_array += [per_word]
            per_word = ""

    # FIND THE MAXIMUM FREQUENCY OF OCCURRENCE OF A WORD IN THE TEXT
    max_frequency: int = 0
    for word in text_array:
        frequency = wordFrequency(text, word)
        if (max_frequency < frequency):
            max_frequency = frequency

    # FIND IMPORTANT INFORMATION WITH 2 CONDITIONS IN THE PROBLEM
    # 1. THE WORD IS THE MOST FREQUENTLY OCCURRING
    # 2. THE WORD IS A PALINDROME (E.G., KAKAK = KAKAK WHEN REVERSED)
    important_info: str = ""
    for word in text_array:
        if word not in important_info:
            if wordFrequency(text, word) == max_frequency:
                important_info += f"{word} "
            elif isPalindrome(word):
                important_info += f"{word} "

    # PRINT IMPORTANT INFORMATION OUTPUT
    print(important_info)

""" PROGRAM ALGORITHM """
# INPUT THE NUMBER OF WORDS IN THE TEXT AND THE TEXT ITSELF
word_count: int = int(input("Masukkan jumlah kata: "))
text: str = str(input("Masukkan teks: "))

# RUN THE PROCEDURE TO PRINT THE WORD
printWord(text)
