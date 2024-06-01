import os
import requests
from pandas import *
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")

TWILIO_NUMBER=os.environ.get("TWILIO_NUMBER")
MY_NUMBER=os.environ.get("MY_NUMBER")
twilio_sid = os.environ.get("TWILIO_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_KEY")

sheety_endpoint = "https://api.sheety.co/1c303ce0021e12124dcbf75095a932d6/myCostFlightFinder/prices"

token_endpoint =  "https://test.api.amadeus.com/v1/security/oauth2/token"
flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

#-----------------------------------------------------sheety--------------------------------------------------------------------------------#
sheety_response = requests.get(url=sheety_endpoint)
data = sheety_response.json()["prices"]
destination_data = data
data_form = DataFrame.from_dict(destination_data)


IATACODE = [i for i in data_form["iataCode"]]
#-----------------------------------------------------flight--------------------------------------------------------------------------------#
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    
}
body = {
    "grant_type" : "client_credentials",
    "client_id" : API_KEY,
    "client_secret": API_SECRET
}

token_response = requests.post(url= token_endpoint,headers=headers,data=body)
new_token = token_response.json()
new_token = new_token['access_token']

from_location = "IND"
to_location = "TYO"

flight_params = {
    "originLocationCode" : "IND",
    "destinationLocationCode" : "TYO",
    "departureDate" : "2024-06-01",
    "adults" :  1,

}
flight_headers = {
     "Authorization" : f"Bearer {new_token}"
}
response = requests.get(url=flight_endpoint,headers=flight_headers,params=flight_params)
data = response.json()["data"][1]
# print(data)

currency = data["price"]["currency"]
price = data["price"]["total"]

print(currency,price)

#------------------------------------------------------------messages-----------------------------------------------------------------------#
message_format = f"Book your flight now ,your registered country {from_location} to {to_location}flight price is low again its {price} {currency} "
# print(message_format)

if float(price) < 2000:
    try:
        client = Client(twilio_sid, twilio_auth_token)
        message = client.messages.create(
            body=message_format,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
        print(message.status)
    except Exception as e:
        print(f"Error sending SMS with Twilio: {e}")


