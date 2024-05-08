from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
score = ScoreBoard()

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    #ball y bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #ball x bounce and paddle bounce
    if  ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect right paddle miss
    if ball.xcor() > 380 :
        ball.ball_reset()
        score.l_point()

    # detect left paddle miss
    if ball.xcor() < -380:
        ball.ball_reset()
        score.r_point()


screen.exitonclick()

