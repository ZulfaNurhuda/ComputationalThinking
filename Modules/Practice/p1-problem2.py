""" PROGRAM DESCRIPTION """
# +----------------------------------------+
# | PROGRAM <Tuan Riz Exam Completion>     |
# +----------------------------------------+
# | DETERMINES IF TUAN RIZ CAN FINISH ALL  |
# | REMAINING EXAM QUESTIONS WITHIN THE    |
# | GIVEN TIME.                            |
# +----------------------------------------+

# +------------------------+-----------+
# | PROGRAM DICTIONARY     | DATA TYPE |
# +------------------------+-----------+
# | short_answer_completed | INTEGER   |
# | essay_completed        | INTEGER   |
# | short_answer_remaining | INTEGER   |
# | essay_remaining        | INTEGER   |
# | time_needed            | INTEGER   |
# | time_available         | INTEGER   |
# +------------------------+-----------+

""" PROGRAM ALGORITHM """
# INPUT NUMBER OF COMPLETED SHORT ANSWER AND ESSAY QUESTIONS
# PROMPT USER TO ENTER HOW MANY SHORT ANSWER QUESTIONS HAVE BEEN COMPLETED
# CONVERT STRING INPUT TO INTEGER FOR MATHEMATICAL OPERATIONS
short_answer_completed: int = int(input("Masukkan banyak soal isian singkat yang sudah diselesaikan: "))
# PROMPT USER TO ENTER HOW MANY ESSAY QUESTIONS HAVE BEEN COMPLETED
# CONVERT STRING INPUT TO INTEGER FOR MATHEMATICAL OPERATIONS
essay_completed: int = int(input("Masukkan banyak soal esai yang sudah diselesaikan: "))

# CALCULATE REMAINING QUESTIONS BASED ON TOTAL QUESTIONS IN EXAM
# TOTAL SHORT ANSWER QUESTIONS IS 14, SUBTRACT COMPLETED ONES
short_answer_remaining: int = 14 - short_answer_completed
# TOTAL ESSAY QUESTIONS IS 2, SUBTRACT COMPLETED ONES
essay_remaining: int = 2 - essay_completed

# CALCULATE TIME NEEDED AND TIME AVAILABLE FOR REMAINING QUESTIONS
# EACH SHORT ANSWER QUESTION TAKES 10 MINUTES, EACH ESSAY TAKES 20 MINUTES
# MULTIPLY REMAINING QUESTIONS BY TIME PER QUESTION AND SUM THEM
time_needed: int = (short_answer_remaining * 10) + (essay_remaining * 20)
# EXAM IS 2 HOURS TOTAL (120 MINUTES), 1ST HOUR HAS PASSED, SO 60 MINUTES REMAINING
time_available: int = 120 - 60 # EXAM IS 2 HOURS, 1ST HOUR HAS PASSED, 1 HOUR (60 MINUTES) REMAINING

# DETERMINE IF TUAN RIZ WILL SUCCEED BY COMPARING TIME NEEDED VS AVAILABLE
# IF TIME NEEDED IS LESS THAN OR EQUAL TO TIME AVAILABLE, HE CAN FINISH
if time_needed <= time_available:
    # PRINT SUCCESS MESSAGE WHEN TIME IS SUFFICIENT
    print("Tuan Riz akan berhasil mengerjakan semua soal")
else:
    # PRINT FAILURE MESSAGE WHEN TIME IS INSUFFICIENT
    print("Tuan Riz tidak akan berhasil mengerjakan semua soal tepat waktu")
