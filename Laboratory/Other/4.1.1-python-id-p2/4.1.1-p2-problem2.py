""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Cube Pattern Generator>       |
# +----------------------------------------+
# | Generates a 3D cube pattern using     |
# | asterisks (*) based on user input     |
# | for the cube side length.             |
# +----------------------------------------+

# +-----------------------+-----------------+
# | PROGRAM DICTIONARY    | DATA TYPE       |
# +-----------------------+-----------------+
# | side_length           | integer         |
# | initial_space         | string          |
# | middle_space          | string          |
# +-----------------------+-----------------+

""" PROGRAM ALGORITHM """
# INITIALIZE CUBE SIDE LENGTH INPUT
side_length: int = int(input("Masukkan panjang kubus: "))

# PRINT TOP PART OF CUBE PATTERN WITH CHANGING SPACE AND ASTERISK PATTERN
for i in range(side_length):
    print(" " * (2 * (side_length - i - 1)) + "*" * (4 * i + 1))

# PRINT MIDDLE PART OF CUBE PATTERN WITH COMBINATION OF ASTERISKS AND SPACES
for i in range(side_length - 1):
    print("*" + (" " * (1 + 2 * i) if i > 0 else " ") + "*" * (4 * (side_length - i - 2) + 1) + (" " * (1 + 2 * i) if i > 0 else " ") + "*")

# PRINT BOTTOM PART OF CUBE PATTERN WITH CHANGING PATTERN FOR EACH ROW
for i in range(side_length - 2):
    initial_space: str = " " * (2 * (i + 1))
    middle_space: str = " " * (2 * (side_length - 3 - i) + 1)
    print(initial_space + "*" + middle_space + "*" + middle_space + "*")

# PRINT FINAL ASTERISK TO COMPLETE CUBE PATTERN
print(" " * (2 * (side_length - 1)) + "*")