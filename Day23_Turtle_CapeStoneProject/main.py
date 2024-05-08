import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkey(player.move_up, 'Up')

    cars_manager.random_car()
    cars_manager.car_moves()

    # detect collision
    for cars in cars_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.is_at_finish_line():
        player.starting_position()
        cars_manager.level_up()
        score_board.level_increase()

screen.exitonclick()