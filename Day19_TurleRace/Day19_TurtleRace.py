from turtle import  Turtle,Screen
import random


race_on=False
screen=Screen()
screen.setup(width=600,height=400)
user=screen.textinput(title="Turtle Race",prompt="Which color turtle are you betting").lower()
colors=['red','orange','yellow','green','blue','purple']
x_positions=[200,125,50,-25,-100,-175]

racer_turts=[]
for turtles_moves in range(0,6):
    timmy=Turtle(shape='turtle')
    timmy.setheading(90)
    timmy.color(colors[turtles_moves])
    timmy.penup()
    timmy.goto(x=x_positions[turtles_moves], y=-160)
    racer_turts.append(timmy)
if user:
    race_on=True

line = Turtle()
line.penup()
line.goto(x=-250,y=190)
line.pendown()
line.forward(500)
line.hideturtle()

while race_on:
    for turts in racer_turts:
        if turts.ycor() > 180:
            winning_color=turts.pencolor()
            if winning_color==user:
                print(f'you are the  winner ,{winning_color}')
                race_on=False
            else:
                print(f'you  lost , { winning_color} is  winner')
                race_on=False
        turts.fd(random.randint(0,10))

screen.exitonclick()



