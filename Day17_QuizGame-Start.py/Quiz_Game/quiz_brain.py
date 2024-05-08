
class QuizBrain:
    def __init__(self,quest_list):
        self.score=0
        self.question_number=0
        self.question_list=quest_list

    def has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_Question = self.question_list[self.question_number ]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}:{current_Question.text} (True/False): ")
        self.check_answer(user_ans,current_Question.answer)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower() ==  current_answer.lower() :
            self.score+=1
            print("you are right")
        else:
            print("you are wrong")
        print(f"The correct answer is : {current_answer} \n")

