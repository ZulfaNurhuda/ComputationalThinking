""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Even Sum Sublist Counter>     |
# +----------------------------------------+
# | COUNTS THE NUMBER OF SUBLISTS          |
# | (CONTIGUOUS SUBARRAYS) IN A GIVEN LIST |
# | WHOSE SUM IS AN EVEN NUMBER.           |
# +----------------------------------------+

# +------------------------+-----------+
# | PROGRAM DICTIONARY     | DATA TYPE |
# +------------------------+-----------+
# | num_elements           | INTEGER   |
# | number_list            | LIST      |
# | even_sum_sublist_count | INTEGER   |
# | current_sum            | INTEGER   |
# | element                | INTEGER   |
# +------------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT NUMBER OF ELEMENTS
num_elements: int = int(input("Masukkan nilai N: "))
number_list: list[int] = [int(input(f"Masukkan bilangan ke-{i + 1}: ")) for i in range(num_elements)]

# INITIALIZE COUNTER FOR SUBLISTS WITH EVEN SUM
even_sum_sublist_count: int = 0

# ITERATE THROUGH ALL POSSIBLE SUBLISTS
for i in range(num_elements):
    current_sum: int = 0
    for j in range(i, num_elements):
        current_sum += number_list[j]
        if current_sum % 2 == 0:
            even_sum_sublist_count += 1

# PRINT THE RESULT
print(f"Terdapat {even_sum_sublist_count} potong list yang jumlahnya genap.")
