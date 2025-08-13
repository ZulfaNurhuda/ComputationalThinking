""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Pascal Matrix Generator>      |
# +----------------------------------------+
# | GENERATES AND PRINTS A PASCAL'S        |
# | TRIANGLE-LIKE MATRIX OF SIZE N X N     |
# | BASED ON SPECIFIC RULES.               |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | matrix_size        | INTEGER   |
# | pascal_matrix      | LIST      |
# | row_index          | INTEGER   |
# | col_index          | INTEGER   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT MATRIX SIZE N FROM USER
# PROMPT USER TO ENTER THE SIZE OF THE PASCAL MATRIX
matrix_size: int = int(input("Masukkan N: "))

# INITIALIZE N X N MATRIX WITH ZEROS
# CREATE 2D LIST WITH ALL ELEMENTS INITIALLY SET TO 0
pascal_matrix: list[list[int]] = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

# FILL THE MATRIX ACCORDING TO THE PASCAL TRIANGLE RULES
# ITERATE THROUGH EACH ROW OF THE MATRIX
for row_index in range(matrix_size):
    # ITERATE THROUGH EACH COLUMN OF THE CURRENT ROW
    for col_index in range(matrix_size):
        # CHECK IF CURRENT POSITION IS ON FIRST ROW OR FIRST COLUMN
        if row_index == 0 or col_index == 0:
            # SET BORDER ELEMENTS (FIRST ROW AND FIRST COLUMN) TO 1
            pascal_matrix[row_index][col_index] = 1
        else:
            # CALCULATE VALUE AS SUM OF ELEMENT ABOVE AND ELEMENT TO THE LEFT
            # PASCAL RULE: CURRENT = TOP + LEFT
            pascal_matrix[row_index][col_index] = pascal_matrix[row_index - 1][col_index] + pascal_matrix[row_index][col_index - 1]

# PRINT THE MATRIX IN FORMATTED OUTPUT
# ITERATE THROUGH EACH ROW FOR PRINTING
for row_index in range(matrix_size):
    # ITERATE THROUGH EACH COLUMN IN THE CURRENT ROW
    for col_index in range(matrix_size):
        # PRINT CURRENT ELEMENT FOLLOWED BY SPACE
        print(pascal_matrix[row_index][col_index], end=" ")
    # PRINT NEWLINE TO COMPLETE THE CURRENT ROW
    print("")
