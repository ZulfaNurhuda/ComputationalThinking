""" PROGRAM DESCRIPTION """
# +-----------------------------------------+
# | PROGRAM <Anagram Checker>               |
# +-----------------------------------------+
# | DETERMINES IF ARRAY B IS AN ANAGRAM OF  |
# | ARRAY A, ASSUMING ELEMENTS ARE INTEGERS |
# | BETWEEN 1 AND 10.                       |
# +-----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | frequency_table    | LIST      |
# | num_elements_A     | INTEGER   |
# | element_A          | INTEGER   |
# | num_elements_B     | INTEGER   |
# | is_anagram_flag    | BOOLEAN   |
# | element_B          | INTEGER   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INITIALIZE FREQUENCY TABLE FOR COUNTING ELEMENT OCCURRENCES
# CREATE ARRAY OF SIZE 10 (FOR INTEGERS 1-9, INDEX 0 IS UNUSED)
frequency_table: list[int] = [0 for _ in range(10)]

# READ ARRAY A ELEMENTS AND UPDATE FREQUENCY TABLE
# PROMPT USER TO ENTER NUMBER OF ELEMENTS IN ARRAY A
num_elements_A: int = int(input("Masukkan banyaknya elemen A: "))
# ITERATE THROUGH ALL ELEMENTS OF ARRAY A
for i in range(num_elements_A):
    # READ EACH ELEMENT OF ARRAY A AND CONVERT TO INTEGER
    element_A: int = int(input(f"Masukkan elemen A ke-{i + 1}: "))
    # INCREMENT FREQUENCY COUNT FOR THIS ELEMENT
    frequency_table[element_A] += 1

# READ ARRAY B ELEMENTS AND CHECK FOR ANAGRAM PROPERTY
# PROMPT USER TO ENTER NUMBER OF ELEMENTS IN ARRAY B
num_elements_B: int = int(input("Masukkan banyaknya elemen B: "))
# CHECK IF ARRAYS HAVE DIFFERENT LENGTHS (CANNOT BE ANAGRAMS)
if num_elements_A != num_elements_B:
    # IF LENGTHS ARE DIFFERENT, IT'S NOT AN ANAGRAM
    # STILL READ ALL B ELEMENTS TO MAINTAIN INPUT FLOW
    for i in range(num_elements_B):
        input(f"Masukkan elemen B ke-{i + 1}: ") # READ AND DISCARD INPUT TO MATCH PROBLEM FLOW
    # PRINT NEGATIVE RESULT FOR DIFFERENT LENGTHS
    print("B bukan anagram dari A")
else:
    # ARRAYS HAVE SAME LENGTH, CHECK ELEMENT FREQUENCIES
    # INITIALIZE FLAG TO TRACK ANAGRAM STATUS
    is_anagram_flag: bool = True
    # READ ALL ELEMENTS OF ARRAY B AND DECREMENT FREQUENCY COUNTS
    for i in range(num_elements_B):
        # READ EACH ELEMENT OF ARRAY B AND CONVERT TO INTEGER
        element_B: int = int(input(f"Masukkan elemen B ke-{i + 1}: "))
        # DECREMENT FREQUENCY COUNT FOR THIS ELEMENT
        frequency_table[element_B] -= 1

    # CHECK FREQUENCY TABLE FOR ZEROS (ALL COUNTS SHOULD BE ZERO FOR ANAGRAM)
    # IF ALL FREQUENCIES ARE ZERO, ARRAYS ARE ANAGRAMS
    if is_anagram_flag:
        # ITERATE THROUGH ALL POSSIBLE ELEMENT VALUES (1-9)
        for i in range(10):
            # IF ANY FREQUENCY IS NOT ZERO, NOT AN ANAGRAM
            if frequency_table[i] != 0:
                is_anagram_flag = False
                break
    
    # PRINT THE RESULT BASED ON ANAGRAM CHECK
    # IF FLAG IS TRUE, ARRAYS ARE ANAGRAMS
    if is_anagram_flag:
        print("B adalah anagram dari A")
    else:
        # IF FLAG IS FALSE, ARRAYS ARE NOT ANAGRAMS
        print("B bukan anagram dari A")
