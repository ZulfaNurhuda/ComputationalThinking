""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Lego Cube Calculator>         |
# +----------------------------------------+
# | CALCULATES THE MAXIMUM NUMBER OF CUBES |
# | THAT CAN BE FORMED FROM A GIVEN NUMBER |
# | OF LEGO PIECES.                        |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | total_lego_pieces  | INTEGER   |
# | num_cubes          | INTEGER   |
# | side_length        | INTEGER   |
# | lego_used          | INTEGER   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT TOTAL NUMBER OF LEGO PIECES FROM USER
# PROMPT USER TO ENTER THE TOTAL AMOUNT OF LEGO PIECES AVAILABLE
total_lego_pieces: int = int(input("Masukkan banyak potongan lego: "))

# INITIALIZE NUMBER OF CUBES COUNTER
# START WITH ZERO CUBES FORMED
num_cubes: int = 0

# ITERATE WHILE THERE ARE LEGO PIECES REMAINING
# CONTINUE FORMING CUBES UNTIL NO MORE PIECES ARE LEFT
while total_lego_pieces > 0:
    # FIND THE LARGEST CUBE SIDE LENGTH THAT CAN BE FORMED
    # START WITH SIDE LENGTH OF 0 AND INCREMENT UNTIL LIMIT
    side_length: int = 0
    # CHECK IF NEXT LARGER CUBE CAN BE FORMED WITH REMAINING PIECES
    # CUBE VOLUME = side_length^3, SO CHECK IF (side_length + 1)^3 <= remaining pieces
    while (side_length + 1) ** 3 <= total_lego_pieces:
        side_length += 1
    
    # CHECK IF A CUBE CAN BE FORMED (SIDE LENGTH > 0)
    if side_length > 0:
        # CALCULATE LEGO PIECES USED FOR THE CURRENT CUBE
        # VOLUME OF CUBE = side_length^3
        lego_used: int = side_length ** 3
        # SUBTRACT USED PIECES FROM TOTAL REMAINING
        total_lego_pieces -= lego_used
        # INCREMENT CUBE COUNTER
        num_cubes += 1
    else: # NO MORE CUBES OF SIZE 1X1X1 OR LARGER CAN BE FORMED
        # ADD REMAINING LEGO PIECES AS 1X1X1 CUBES
        # EACH REMAINING PIECE FORMS ONE 1X1X1 CUBE
        num_cubes += total_lego_pieces
        # SET REMAINING PIECES TO ZERO TO EXIT LOOP
        total_lego_pieces = 0

# PRINT THE TOTAL NUMBER OF CUBES FORMED
# DISPLAY FINAL RESULT TO USER
print(f"Tuan Leo dapat membuat {num_cubes} kubus.")
