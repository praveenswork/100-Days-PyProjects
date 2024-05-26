import smtplib
import datetime as dt
import random
import pandas as pd


my_email ="praveenpraveen25720@gmail.com"
password = "fhniaoitsgyperqm"

birthday = dt.datetime.now()
today = (birthday.month,birthday.day)
# print(today,)

birth_data = pd.read_csv("birthdays.csv")

birthdate_dict = {(row["month"],row["day"]):row for index,row in birth_data.iterrows()}

if(today in birthdate_dict):
    birthday_guy = birthdate_dict [today]
    file_path =f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_templates:
        letter_file = letter_templates.read()
        letter_file = letter_file.replace("[NAME]",birthday_guy["name"])
        # print(letter_file)

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(user=my_email,password=password)
        server.sendmail(from_addr=my_email,
                        to_addrs=birthday_guy["email"],
                        msg=f"Subject:Birthday Wishes\n\n This message is automated from python \n\n {letter_file}")


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)





