import smtplib
import datetime as dt
import random

my_email = "praveenpraveen25720@gmail.com"
password ="fhniaoitsgyperqm"

birthday = dt.datetime(year=2024,month=5,day=26,hour=12,minute=20,second=0)
today = dt.datetime.now()
print(birthday,today)


if (birthday.year == today.year and 
    birthday.month == today.month and birthday.day == today.day and 
    birthday.hour == today.hour and birthday.minute == today.minute) :
    with open("day_quotes.txt") as quote_file:
        all_quotes =quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_email,password=password)
        connect.sendmail(from_addr=my_email,
                        to_addrs="22107045@srcas.ac.in",
                        msg= f"Subject:This is python code\n\nHappy Sunday ,Here your sunday quote {quote}")
        
else:
    print("The current date and time do not match the specified birthday.")
    
