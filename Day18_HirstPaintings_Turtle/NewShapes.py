import turtle
from turtle import *


prat=Turtle()
turtle.bgcolor("black")

'''shapes=2
for _ in range(10):
    shapes += 1
    degree=360/shapes
    for __ in range(shapes):
        prat.color("aqua")
        prat.forward(100)
        prat.left(degree)

'''
import random
colors=["cyan1",'DeepPink1','lawngreen','green','LightPink']
def shapes(sides):
    angle=360 / sides
    for _ in range(sides):
        prat.forward(100)
        prat.left(angle)

for _ in range(3,11):
    prat.color(random.choice(colors))
    shapes(_)







