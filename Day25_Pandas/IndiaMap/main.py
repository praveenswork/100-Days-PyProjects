import turtle

import pandas
from turtle import Screen

screen = Screen()
screen.setup(600, 600)
screen.title('Name any 10 states to win ')
screen.bgpic('india_outline.gif')

data = pandas.read_csv('india_states.csv')
all_states = data.state.to_list()
guessed_state = []

while len(data) < 27:
    user_state = screen.textinput(f'{len(guessed_state)}/10 your points',
                                  'Enter a name for place the state name in correct place').title()
    place = data[data.state == user_state]

    if user_state == 'Exit':
        missing_state = [missing_state.append(state) for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv('new_missing_states')

    if user_state in user_state:
        guessed_state.append(user_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color()
        place = data[data.state == user_state]
        t.goto(int(place.x), int(place.y))
        t.color('orange')
        t.write(f"* {user_state}", font=('sarif', 12, 'bold'))

    else:
        print('check you input')

    if len(guessed_state) == 10:
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.penup()
        turt.color('Blue')
        turt.write('You Guessed 10 states in india !!!', align='center', font=('courier', 20, 'normal'))


turtle.mainloop()
