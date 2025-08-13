""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Determining Graduation>       |
# +----------------------------------------+
# | Determining graduation based on the    |
# | average of 3 quiz scores               |
# +----------------------------------------+

# +--------------------+-----------+
# | PROGRAM DICTIONARY | DATA TYPE |
# +--------------------+-----------+
# | quiz_one           | integer   |
# | quiz_two           | integer   |
# | quiz_three         | integer   |
# | average            | real      |
# +--------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT QUIZ SCORES 1, 2, AND 3
quiz_one: int = int(input("Masukkan nilai kuis pertama: "))
quiz_two: int = int(input("Masukkan nilai kuis kedua: "))
quiz_three: int = int(input("Masukkan nilai kuis ketiga: "))

# CALCULATE THE AVERAGE OF 3 QUIZZES
average: float = (quiz_one + quiz_two + quiz_three) / 3

# ANALYZE AVERAGE SCORE AND DETERMINE STATUS
if average >= 80:
    print("Tuan Leo mendapatkan nilai Lulus Memuaskan.")
elif 80 > average >= 70:
    print("Tuan Leo mendapatkan nilai Lulus.")
else:
    print("Tuan Leo mendapatkan nilai Tidak Lulus.")