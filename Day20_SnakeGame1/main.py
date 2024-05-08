from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

screen = Screen()
screen.bgcolor("blue")
screen.title("Snake Game")
screen.setup(width=500, height=500)
screen.tracer(0)

food = Food()
snake = Snake()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend_snake()
        score.increase_score()
        food.color_food()

    if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() > 245 or snake.head.ycor() < -245:
        game_on = False
        score.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
