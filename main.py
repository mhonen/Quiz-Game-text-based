#*************************************************************
#
# main.py
#
# Version: 1.0
# 
# Comments: This is a tutorial that I followed from Angela's 
#           100 days of code.  I will turn this into a Graphical
#           Interface later.
#****************************************************************

#imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Define question list
question_bank = []

# Populate question_bank
for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)

# Call AI that runs through each question
quiz = QuizBrain(question_bank)

# Quit when end of list is reached
while quiz.still_has_questions():
  quiz.next_question()

# Final print statements
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")
final_percent = round((quiz.score/quiz.question_number) * 100)
print(f"Your final percent score is: {final_percent}%.")
