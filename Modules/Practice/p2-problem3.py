""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Reverse Number Printer>       |
# +----------------------------------------+
# | READS N NUMBERS AND PRINTS THEM IN     |
# | REVERSE ORDER.                         |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | num_elements       | INTEGER   |
# | numbers_list       | LIST      |
# | number_input       | INTEGER   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT THE NUMBER OF ELEMENTS FROM USER
# PROMPT USER TO ENTER HOW MANY NUMBERS WILL BE INPUT
num_elements: int = int(input("Masukkan N: "))
# READ N NUMBERS INTO THE LIST USING LIST COMPREHENSION
# FOR EACH ITERATION, READ ONE INTEGER AND ADD TO LIST
numbers_list: list[int] = [int(input()) for _ in range(num_elements)]

# PRINT THE NUMBERS IN REVERSE ORDER (LAST TO FIRST)
# DISPLAY HEADER MESSAGE FOR REVERSED OUTPUT
print("Hasil dibalik:")
# ITERATE THROUGH LIST BACKWARDS FROM LAST INDEX TO FIRST
# START FROM (num_elements - 1), GO TO -1 (EXCLUSIVE), STEP BY -1
for i in range((num_elements - 1), -1, -1):
    # PRINT EACH NUMBER FOLLOWED BY SPACE (NO NEWLINE)
    print(numbers_list[i], end=" ")
# PRINT FINAL NEWLINE TO END THE OUTPUT LINE
print("")
