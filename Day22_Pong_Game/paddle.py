from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(positions)

    def up(self):
        self.goto(self.xcor(), y=self.ycor()+40)

    def down(self):
        self.goto(self.xcor(), y=self.ycor()-40)


