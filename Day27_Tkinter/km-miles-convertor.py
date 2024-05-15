from tkinter import *

root = Tk()
root.geometry('250x100')
root.title('km to Miles convertor')

mile = Entry(width = 10 )
mile.grid(row=0, column=1)

lbl_1 = Label(text='miles')
lbl_1.grid(row=0, column=2)
lbl_1.config(padx=5, pady=5)

# 1 mile 1.609

def convert ():
    miles = mile.get()
    kilom = round( float(miles) * 1.6 , 2)
    km.config(text=f'{kilom}')

km = Label(text="       ")
km.grid(row=1 ,column=1)

lbl_2 = Label(text=f"is  eqals  to >>  ")
lbl_2.grid(row=1 , column=0)
lbl_2.config(padx=2, pady=2)

lbl_3 = Label(text="Kilometers")
lbl_3.grid(row=1 , column=2)
lbl_3.config(padx=2, pady=2)

btn =Button(text="Convert", command=convert)
btn.grid(row=2 ,column=1)


root.mainloop()