import tkinter as tki

root = tki.Tk()
root.title("sample")
root.geometry('500x300')

lbl = tki.Label(root, text = "hello")
lbl.grid(row=0, column=1)

input = tki.Entry(width =10)
input.grid(row=0, column=2)

def change():
    lbl.config(text=input.get())

btn = tki.Button(text='click', command=change)
btn.grid(row=0, column=3)

root.mainloop()