from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def random_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-230, 230)
            new_car.goto(300, y_pos)
            self.all_cars.append(new_car)

    def car_moves(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT



