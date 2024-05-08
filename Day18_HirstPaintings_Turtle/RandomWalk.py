
import colorsys
import random
import turtle as t
from random import choice
t.hideturtle()
t.width(9)
t.speed('fastest')
#colors=["cyan1",'DeepPink1','lawngreen','green','LightPink','PaleGreen','OliveDrab']
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color=(r,g,b)
    return rand_color

direction=[0,90,180,270]

for _ in range(300):
    t.color(random_color())
    t.setheading(choice(direction))
    t.fd(20)





















'''
t.bgcolor("black")
t.speed('fastest')
t.pensize(3)
h=0.0
t.hideturtle()
for i in range(1000):
    color=colorsys.hsv_to_rgb(h,1,1,)
    t.pencolor(color)
    t.fd(i)
    t.rt(98.5)
    t.circle(50)
    h+=0.008

t.exitonclick()
'''

