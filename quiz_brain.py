###########################################################################
#
# QuizBrain module
#
# Version: 1.0
#
# Comments: Again, will save this module to use in the updated GUI porject.
#           of The Quiz Game
###########################################################################
class QuizBrain:
  def __init__(self, q_list): # Constructor
    self.question_number = 0
    self.question_list = q_list
    self.score = 0

  # Checks if there are any remaining questions.
  def still_has_questions(self):
    return self.question_number < len(self.question_list)
  # Adds count to question_number, Calls check_answer function and increases question_number += 1.
  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer, current_question.answer)
  # Checks to see if user chose correct answer
  def check_answer(self, user_input, answer):
    if user_input.lower() == answer.lower():
      print("You got the question right!!")
      self.score += 1
    else:
      print("You got it wrong.")

    print(f"The correct answer was: {answer}.")
    print(f"Your current score is: {self.score}/{self.question_number}")
    print("\n")


