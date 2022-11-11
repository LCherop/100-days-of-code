from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for i in question_data:
    question_txt = i["question"]
    question_ans = i["correct_answer"]
    new_question = Question(txt=question_txt,ans=question_ans)
    question_bank.append(new_question)
    
quiz = Quizbrain(question_bank)

while quiz.r_u_still_smart :
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")