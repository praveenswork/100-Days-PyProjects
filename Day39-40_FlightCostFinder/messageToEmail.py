import os
import requests
from pandas import *
from twilio.rest import Client
import smtplib
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("EMAIL_PASSWORD")

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")

TWILIO_NUMBER=os.environ.get("TWILIO_NUMBER")
MY_NUMBER=os.environ.get("MY_NUMBER")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_KEY = os.environ.get("TWILIO_AUTH_KEY")

sheety_endpoint = "https://api.sheety.co/1c303ce0021e12124dcbf75095a932d6/flightEmailToUser/sheet1"

token_endpoint =  "https://test.api.amadeus.com/v1/security/oauth2/token"
flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"



#------------------------------------------------------userdata-----------------------------------------------------------------------------#
print("Welcome to praveen's flight finder")
user_name = input("Enter your full name : ")
from_location = input("Enter your from location in iatacode (PAR): ")
to_location = input("Enter your to location iatacode(IND): ")
email = input("Enter your valid gmail only: ")
#-----------------------------------------------------sheety--------------------------------------------------------------------------------#

body ={
    "sheet1" : {
        "name" : user_name,
        "from" : from_location,
        "to" : to_location,
        "email" : email
    }
}
sheety_response = requests.post(url=sheety_endpoint,json=body)
print(sheety_response.json)


# #=====================================================flight==================================================================================#
#accessing token
headers = {"Content-Type": "application/x-www-form-urlencoded"}
body = {
    "grant_type" : "client_credentials",
    "client_id" : API_KEY,
    "client_secret": API_SECRET
}

token_response = requests.post(url= token_endpoint,headers=headers,data=body)
new_token = token_response.json()
new_token = new_token['access_token']
# print(new_token)

flight_params = {
    "originLocationCode" : from_location,
    "destinationLocationCode" :to_location,
    "departureDate" : "2024-06-05",
    "adults" :  1,
}
flight_headers = {
     "Authorization" : f"Bearer {new_token}"
}
response = requests.get(url=flight_endpoint,headers=flight_headers,params=flight_params)
response.raise_for_status()
data = response.json()["data"][1]
# print(data)

currency = data["price"]["currency"]
price = data["price"]["total"]

print(currency,price)

if price <2000:
    try:
        with smtplib.SMTP('smtp.gmail.com') as server:
            server.starttls()
            server.login(user=my_email, password=my_password)
            server.sendmail(
                from_addr=my_email,
                to_addrs="22107045@srcas.ac.in",
                msg=f"Subject:Flight for cheap\n\nHere your registered flight price was down \n\ngrab your seat for {price}"
            )
    except Exception as e:
        print(f"try another time or check your details {e}")
