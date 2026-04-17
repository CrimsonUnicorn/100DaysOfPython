from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank= []
for data in question_data:
  q_text = data["text"]
  q_ans = data["answer"]
  new_question = Question(q_text , q_ans)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")