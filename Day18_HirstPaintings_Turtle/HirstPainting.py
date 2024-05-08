'''import  colorgram

colors=colorgram.extract('color_pallete_light.jpeg',10)

rgb_color=[]
for col in colors:
    r = col.rgb.r
    g = col.rgb.g
    b = col.rgb.b
    new_color=(r,g,b)

    rgb_color.append(new_color)
print(rgb_color)'''
import turtle as t
from random import choice

color_pallet = [(131, 77, 113), (247, 237, 179), (213, 119, 195), (251, 194, 208), (253, 252, 45), (129, 234, 157), (248, 143, 205), (233, 138, 96), (236, 58, 193), (100, 192, 203)]
t.colormode(255)
t.bgcolor("black")
tim = t.Turtle()
tim.hideturtle()
tim.speed('fastest')
def rows_circle ():
    for _ in range(10):
        tim.color(choice(color_pallet))
        tim.fd(50)
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()

dots=5
tim.up()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
tim.down()
for dot_count in range(1,dots+1):
    tim.up()
    tim.bk(50)
    rows_circle()
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.bk(50)
    rows_circle()
    tim.setheading(90)
    tim.fd(15)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()



