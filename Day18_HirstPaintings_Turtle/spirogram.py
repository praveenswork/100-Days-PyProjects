import turtle as t
import random

t.colormode(255)
t.bgcolor('black')
tim=t.Turtle()

def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color=(r,g,b)
    return rand_color

tim.speed('fastest')

def draw_spirograph(size):

    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size)

draw_spirograph(6)



screen= t.Screen()
screen.exitonclick()


