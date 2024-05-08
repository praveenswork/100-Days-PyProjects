from turtle import Turtle
import random

colors = ['pink', 'yellow', 'cyan', 'lawngreen', 'magenta']


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color_food()
        self.speed('fastest')
        self.refresh_food()

    def refresh_food(self):
        x_random = random.randint(-230, 230)
        y_random = random.randint(-230, 230)
        self.goto(x_random, y_random)

    def color_food(self):
        self.color(random.choice(colors))

