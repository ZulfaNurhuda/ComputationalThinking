""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Consecutive Group Counter>    |
# +----------------------------------------+
# | COUNTS THE NUMBER OF CONSECUTIVE GROUPS|
# | IN A SORTED LIST OF DISTINCT INTEGERS. |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | num_data_elements  | INTEGER   |
# | data_list          | LIST      |
# | group_count        | INTEGER   |
# | element            | INTEGER   |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT NUMBER OF DATA ELEMENTS
num_data_elements: int = int(input("Masukkan banyak data: "))
data_list: list[int] = [int(input(f"Masukkan data ke-{i + 1}: ")) for i in range(num_data_elements)]

# HANDLE EMPTY LIST CASE
if num_data_elements == 0:
    print("Banyak grup angka terurut adalah 0.")
else:
    # SORT THE DATA LIST USING BUBBLE SORT
    for i in range(num_data_elements):
        for j in range(0, num_data_elements - i - 1):
            if data_list[j] > data_list[j + 1]:
                # SWAP ELEMENTS
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    
    # INITIALIZE GROUP COUNT
    group_count: int = 1
    # ITERATE THROUGH SORTED LIST TO COUNT GROUPS
    for i in range(1, num_data_elements):
        # IF CURRENT ELEMENT DOES NOT FOLLOW THE PREVIOUS ONE CONSECUTIVELY, START A NEW GROUP
        if data_list[i] != data_list[i - 1] + 1:
            group_count += 1
            
    # PRINT THE RESULT
    print(f"Banyak grup angka terurut adalah {group_count}.")
