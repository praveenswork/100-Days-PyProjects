from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"
FONT_ITALIC = ("Arial",20,"italic")

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.screen = Tk()
        self.screen.title("Quiz")
        self.screen.config(padx=20,pady=20)
        self.screen.config( bg=THEME_COLOR)

        self.score_lbl = Label(text='Score : 0' , bg=THEME_COLOR, fg="white")
        self.score_lbl.config()
        self.score_lbl.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250 )
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            font=FONT_ITALIC ,
            text="some text",
            fill=THEME_COLOR)
        self.canvas.grid(row=1 , column=0 , columnspan=2,pady=50)

        tick_img = PhotoImage(file="images/true.png")
        self.tick_btn = Button(image=tick_img,highlightthickness=0,command=self.tick)
        self.tick_btn.config(padx=20 , pady=20)
        self.tick_btn.grid(row=2 , column=0 )

        cross_img = PhotoImage(file="images/false.png")
        self.cross_btn = Button(image=cross_img, highlightthickness=0,command=self.wrong)
        self.cross_btn.config(padx=20 , pady=20)
        self.cross_btn.grid(row=2 , column=1 )

        self.get_next_Questions()
 
        self.screen.mainloop()

    def get_next_Questions(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.cross_btn(state = "disabled")
            
    def tick(self):
        # is_right = (self.quiz.check_answer("True"))
        self.feed_back(self.quiz.check_answer("True"))
    def wrong(self):
        is_right = (self.quiz.check_answer("False"))
        self.feed_back(is_right)
    
    def feed_back(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000,self.get_next_Questions)