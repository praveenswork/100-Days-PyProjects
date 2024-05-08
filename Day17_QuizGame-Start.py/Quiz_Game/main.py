from data import  question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for quest in question_data:
    quest_text = quest["text"]
    quest_answer = quest["answer"]
    new_question = Question(quest_text,quest_answer)
    question_bank.append(new_question)

quizz=QuizBrain(question_bank)

while quizz.has_question():
    quizz.next_question()

print("You have completed this quiz")
print(f"your final score was :{quizz.score}/{len(question_bank)}")







