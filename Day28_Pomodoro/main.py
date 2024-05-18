from tkinter import *
from  winsound import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f9dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS =  0
timmer = None

def play():
     lambda: PlaySound("sound_asset\pop_sound.mp3", SND_FILENAME)
# ---------------------------- TIMER RESET ------------------------------- # 
def reset ():
    screen.after_cancel(timmer)
    timer_lbl.config(text='Timer')
    canvas.itemconfig(time_text,text="00:00")
    tick.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global REPS
    REPS +=1

    if REPS % 8 ==0:
        timer_func(LONG_BREAK_MIN*60)
        timer_lbl.config(text='Long Break', fg=RED)
        set_btn.config(bg=RED)
        reset_btn.config(bg=RED)
    elif REPS % 2 ==0:
        timer_func(SHORT_BREAK_MIN*60)
        timer_lbl.config(text=' Break', fg=YELLOW)
        set_btn.config(bg=YELLOW)
        reset_btn.config(bg=YELLOW)
    else:
        timer_func(WORK_MIN*60)
        timer_lbl.config(text='Work',fg=GREEN)
        set_btn.config(bg=GREEN)
        reset_btn.config(bg=GREEN)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer_func(count):
    mins = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec =f"0{sec}"
    if mins < 10:
        mins = f"0{mins}"
    
    

    canvas.itemconfig(time_text, text =f'{mins}:{sec}')
    if count > 0:
        global timmer
        timmer = screen.after(1000,timer_func,count -1)
    else :
        start()
        marks =""
        check_reps = math.floor(REPS/2)
        for _ in range(check_reps):
            marks+="✔"
        tick.config(text=marks)


    
# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("POMODORO")
screen.config(padx=50, pady=50, bg=PINK)

canvas = Canvas(width =220 , height =224, bg=PINK, highlightbackground=PINK)
img = PhotoImage(file="tomato.png")
canvas.create_image(110,112 ,image = img)
time_text = canvas.create_text(110,120,text="00:00", font=(FONT_NAME, 40, "bold"), fill="white")
canvas.grid(row=2, column=2)

timer_lbl = Label(text="Timer", font=(FONT_NAME, 34, "bold"), bg=PINK, fg=GREEN)
timer_lbl.grid(row=1, column=2)

set_btn = Button(text='set',bg=GREEN, command=start,) 
set_btn.grid(row=3, column=1)


reset_btn = Button(text='reset',bg=GREEN,command=reset)
reset_btn.grid(row=3, column=3)

tick = Label( fg=GREEN, bg=PINK, font=(FONT_NAME,24,"bold"))
tick.grid(row=3, column=2)
tick.config(pady=20)

screen.mainloop()