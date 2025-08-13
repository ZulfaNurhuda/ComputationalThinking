""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Frog Jump Simulator>          |
# +----------------------------------------+
# | SIMULATES A FROG'S JUMPS BASED ON      |
# | GIVEN RULES AND CALCULATES ITS FINAL   |
# | COORDINATE.                            |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | initial_coordinate | INTEGER   |
# | jump_right_length  | INTEGER   |
# | jump_left_length   | INTEGER   |
# | num_jumps          | INTEGER   |
# | left_jumps         | INTEGER   |
# | right_jumps        | INTEGER   |
# | final_coordinate   | INTEGER   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT INITIAL COORDINATE, JUMP RIGHT LENGTH, AND JUMP LEFT LENGTH FROM USER
# PROMPT USER TO ENTER FROG'S STARTING COORDINATE AND CONVERT TO INTEGER
initial_coordinate: int = int(input("Masukkan koordinat katak: "))
# PROMPT USER TO ENTER LENGTH OF RIGHT JUMPS AND CONVERT TO INTEGER
jump_right_length: int = int(input("Masukkan panjang lompatan katak ke kanan: "))
# PROMPT USER TO ENTER LENGTH OF LEFT JUMPS AND CONVERT TO INTEGER
jump_left_length: int = int(input("Masukkan panjang lompatan katak ke kiri: "))

# DETERMINE THE NUMBER OF JUMPS (k) BASED ON COORDINATE RULES
# INITIALIZE NUMBER OF JUMPS TO ZERO
num_jumps: int = 0
# RULE 1: IF COORDINATE IS NEGATIVE AND DIVISIBLE BY 3
if initial_coordinate < 0 and initial_coordinate % 3 == 0: # NEGATIVE MULTIPLE OF 3
    # NUMBER OF JUMPS = LEFT JUMP LENGTH * 2
    num_jumps = jump_left_length * 2
# RULE 2: IF COORDINATE IS NEGATIVE (NOT DIVISIBLE BY 3) OR EVEN
elif initial_coordinate < 0 or initial_coordinate % 2 == 0: # NEGATIVE NON-MULTIPLE OF 3 AND EVEN
    # NUMBER OF JUMPS = RIGHT JUMP LENGTH * LEFT JUMP LENGTH
    num_jumps = jump_right_length * jump_left_length
# RULE 3: IF COORDINATE IS POSITIVE AND ODD
else: # POSITIVE ODD
    # NUMBER OF JUMPS = RIGHT JUMP LENGTH * 2
    num_jumps = jump_right_length * 2

# DETERMINE THE NUMBER OF LEFT JUMPS AND RIGHT JUMPS
# LEFT JUMPS = HALF OF TOTAL JUMPS (INTEGER DIVISION)
left_jumps: int = num_jumps // 2
# RIGHT JUMPS = REMAINING JUMPS AFTER LEFT JUMPS
right_jumps: int = num_jumps - left_jumps

# SIMULATE FROG JUMPS AND CALCULATE FINAL COORDINATE
# FINAL POSITION = INITIAL + (RIGHT JUMPS * RIGHT LENGTH) - (LEFT JUMPS * LEFT LENGTH)
final_coordinate: int = initial_coordinate + (jump_right_length * right_jumps) - (jump_left_length * left_jumps)

# PRINT FINAL COORDINATE RESULT
# DISPLAY THE FROG'S FINAL POSITION AFTER ALL JUMPS
print(f"Koordinat katak sekarang adalah {final_coordinate}")
