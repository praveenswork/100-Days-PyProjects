import requests
import smtplib
from datetime import datetime
import time

my_email = "praveenpraveen25720@gmail.com"
password ="fhniaoitsgyperqm"

MY_LAT =11.016844    # Your latitude
MY_LONG =76.955833   # Your longitude

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG -5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if  time_now <= sunrise or time_now >= sunset :
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login(user=my_email , password=password)
            server.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg='Subject:Look Up \n\n ISS is above here...'
            )





