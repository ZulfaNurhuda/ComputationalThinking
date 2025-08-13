""" PROGRAM DESCRIPTION """
# +----------------------------------------------------+
# | PROGRAM <Sum of Largest Prime Factors>             |
# +----------------------------------------------------+
# | Calculates the sum of the largest prime factors    |
# | for all numbers in a given range [m, n].           |
# +----------------------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | m                  | integer   |
# | n                  | integer   |
# | result             | integer   |
# +--------------------+-----------+

def largestPrimeFactor(n: int) -> int:
    """ Description: `[FUNCTION] largestPrimeFactor` """
    # +----------------------------------------------------+
    # | FUNCTION <Find the largest prime factor of a number> |
    # +----------------------------------------------------+
    # | Finds the largest prime factor of a given integer. |
    # +----------------------------------------------------+

    # +--------------------+-----------+
    # | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | n                  | integer   |
    # | largest_factor     | integer   |
    # | i                  | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    if n <= 1:
        return 0
    
    largest_factor: int = 0
    
    # CHECK FOR FACTOR 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
        
    # CHECK FOR ODD FACTORS
    i: int = 3
    while i * i <= n:
        while n % i == 0:
            largest_factor = i
            n //= i
        i += 2
        
    if n > 2:
        largest_factor = n
        
    return largest_factor

def sumLargestPrimeFactors(m: int, n: int) -> int:
    """ Description: `[FUNCTION] sumLargestPrimeFactors` """
    # +------------------------------------------------------------+
    # | FUNCTION <Sum the largest prime factors in a range>        |
    # +------------------------------------------------------------+
    # | Calculates the sum of the largest prime factors for all    |
    # | numbers in a given range [m, n].                           |
    # +------------------------------------------------------------+

    # +--------------------+-----------+
# | LOCAL DICTIONARY   | DATA TYPE |
    # +--------------------+-----------+
    # | m                  | integer   |
    # | n                  | integer   |
    # | total_sum          | integer   |
    # | i                  | integer   |
    # +--------------------+-----------+

    """ FUNCTION ALGORITHM """
    total_sum: int = 0
    for i in range(m, n + 1):
        total_sum += largestPrimeFactor(i)
    return total_sum

""" PROGRAM ALGORITHM """
# INPUT RANGE [M, N]
m: int = int(input("Masukkan nilai m: "))
n: int = int(input("Masukkan nilai n: "))

# CALCULATE AND PRINT THE SUM OF LARGEST PRIME FACTORS
result: int = sumLargestPrimeFactors(m, n)
print(f"Jumlah faktor prima terbesar adalah {result}.")