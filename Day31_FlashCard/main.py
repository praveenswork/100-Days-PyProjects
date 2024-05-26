from tkinter import *
from pandas import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
screen =  Tk()
screen.title('Flash Card')
screen.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


try:
    data = read_csv("words.csv", encoding="latin-1")

except FileNotFoundError:
    orginal_data = read_csv("data/french_words.csv", encoding="latin-1")   
    to_learn = orginal_data.to_dict(orient="records")

else:     
    to_learn = data.to_dict(orient="records")


data = read_csv("data/french_words.csv")
to_learn =data.to_dict(orient="records")
random_french_words = choice(data["French"])

current_card={ }

def next_word():
    global current_card,flip_timer
    screen.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text =current_card["French"], fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = screen.after(3000,answer_card)

def answer_card():
    canvas.itemconfig(card_title,text ="English",fill="white")
    canvas.itemconfig(card_word,text =current_card["English"], fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

flip_timer = screen.after(3000,answer_card)

def tick():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("words.csv", index=False)
    next_word()

#---------------------------------UI---------------------------------#

canvas = Canvas(width=800,height=550)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
card_title  = canvas.create_text(400,150,text="",font=("arial",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("serif",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_img = PhotoImage (file="images/wrong.png")
wrong_btn = Button(image=wrong_img,highlightthickness=0,command=next_word)
wrong_btn.grid(row=1,column=0)

tick_img = PhotoImage (file="images/right.png")
tick_btn = Button(image=tick_img,highlightthickness=0,command=tick)
tick_btn.grid(row=1,column=1)

next_word()

screen.mainloop()
