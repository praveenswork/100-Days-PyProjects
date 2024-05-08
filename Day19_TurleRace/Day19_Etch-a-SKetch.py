from turtle import  Turtle,Screen

tim=Turtle()
screen=Screen()

screen.bgpic('D:/project file/python_100day_projects/Day18_HirstPaintings_Turtle/color_pallete_light.jpeg')

def front():
    tim.fd(100)

def a():
    new_angle=tim.heading()+10
    tim.setheading(new_angle)

def w():
    tim.setheading(90)

def d():
    new_angle = tim.heading() - 10
    tim.setheading(new_angle)
def s():
    tim.setheading(270)
def c():
    tim.circle(100)
def clear():
    tim.clear()

    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(front, "space")
screen.onkey(a, "a")
screen.onkey(w, "w")
screen.onkey(d, "d")
screen.onkey(s, "s")
screen.onkey(clear, "e")
screen.onkey(c,'c')
screen.listen()

screen.exitonclick()