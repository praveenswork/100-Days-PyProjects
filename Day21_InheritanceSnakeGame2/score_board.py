from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 08520
        self.hight_score = 0
        with open('data.txt') as data:
            self.hight_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score { self.score}  Highscore {self.hight_score}', align=ALIGNMENT, font=FONT)


    def reseting(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.hight_score}')
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()


