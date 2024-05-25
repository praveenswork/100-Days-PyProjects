from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

data = {
     
}
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters=['a','b','c','d','e','F','g','h','i','j','k','l','m',
            'N','O','P','Q','r','S','t','U','V','W','X','y','Z']
    number=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','@','#','$','^','&','*','{','}','(',')','?','/' ]

    password_leter = [choice(letters) for _ in range(randint(8,10))]
    password_number = [choice(number) for _ in range(randint(2,4))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]

    password_list=password_leter + password_number + password_symbol

    shuffle(password_list)

    password= "".join(password_list)
    pass_text.insert(0,password)
    pyperclip.copy(password)

#-----------------------------SEARCH BUTTON----------------------------------#
def find_password():
    website = web_text.get()
    try:
     with open ('data.json','r') as data_read:
        data =json.load(data_read)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="File Not Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,message=f"email:{email}\n password:{password}")
        else:
            messagebox.showinfo(title="ERROR",message="Add your password first")
     
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_text.get()
    email = email_text.get()
    password = pass_text.get()

    data_obj = {
         website:{
         "email":email,
         "password":password,
         }
    }
    new_data = {
         website:{
         "email":email,
         "password":password,
         }}
    
    if len(website) ==0 or len(email)==0 or len(password)==0:
        messagebox.askokcancel(title='Error', message='Fill every line to ADD' )
    else:
        try:
            with open ('data.json' , mode='r') as data_file :
                data = json.load(data_file)
        except FileNotFoundError:
                with open('data.json',mode='w') as data_file :
                     json.dump(data_obj,data_file,indent=4)
        else:
             data.update(new_data)
             with open("data.json","w") as data_file:
                  json.dump(data,data_file,indent=4)
                
        finally:
                web_text.delete(0,END)
                email_text.delete(0,END)
                pass_text.delete(0,END)
        
        

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title('Password Manager')
root.config(padx=50,pady=50)

canvas = Canvas(width=200 , height=200 )
img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image =img)
canvas.grid(row=0,column=1)

website_lbl = Label(text='website:')
website_lbl.grid(row=1,column=0)
email_lbl = Label(text='Email/Username:' )
email_lbl.grid(row=2,column=0)
password_lbl = Label(text='Password:')
password_lbl.grid(row=3,column=0)

web_text = Entry(width=33)
web_text.grid(row=1,column=1,columnspan=1 )
email_text= Entry(width=52)
email_text.grid(row=2, column=1,columnspan=2)
email_text.insert(0,'elangothanga@srcas.in')
pass_text= Entry(width=33)
pass_text.grid(row=3, column=1,columnspan=1)

search_btn = Button(text='Search',width=15, command=find_password)
search_btn.grid(row=1,column=2)
pass_btn = Button(text='Generate password',command=generate)
pass_btn.grid(row=3,column=2)
add_btn = Button(text='Add', width=44, command=save )
add_btn.grid(row=4, column=1, columnspan=2)

root.mainloop()
