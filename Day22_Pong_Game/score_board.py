from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('sarif',64,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score=0
        self.l_score=0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(50, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(-50, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

