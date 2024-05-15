from tkinter import *

root = Tk()
root.title('Widget Examples')
root.geometry('500x500') 


lbl = Label(text='Enter your name:  ')
lbl.grid(row=0, column=1)

input = Entry(width=20)
input.grid(row=0,column=2)

def submit(): 
    name = Label(text='welcome ' + input.get())
    name.grid(row=3,column=2)

btn = Button(text='Submit', command=submit)
btn.grid(row=2, column=1)

def scale_used(value):
    print(value)

#Scale
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid()

#spinbox
spin = Spinbox(from_=0, to=10, width=10)
spin.grid()

#check state
def check_button():
    print(check_state.get())

check_state =IntVar()
check_btn = Checkbutton(text="on",variable=check_state, command=check_button)
check_state.get()
check_btn.grid()

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radio1 = Radiobutton(text ="male", value = 1, variable=radio_state, command = radio_used)
radio2 = Radiobutton(text ="female", value = 2, variable =radio_state, command = radio_used)

radio1.grid()
radio2.grid()

#listbox
def listbox_used():
    print(list_box.get(list_box.curselection()))

list_box = Listbox(height=5)
names = ["Dharshan", "Elango", "Nithees", "Praveen"]
for n in names:
    list_box.insert(names.index(n),n)
list_box.bind("<<ListboxSelector >>",
listbox_used)
list_box.grid()

root.mainloop()