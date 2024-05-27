import requests
from twilio.rest import *

MyLat = 11.016844
MyLong = 76.955833
account_sid = "AC87da0003fadd90cc691b5e1e13b03e6f"
account_token ="a3eda824b781ad8a38f59ececf85a055"

parameter = {
    "lat":MyLat,
    "lon":MyLong,
    "appid":"8f02b4995f3db82f010d7b632922f712",
    "cnt":5
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params = parameter)
response.raise_for_status()
weather_data = response.json()
data= weather_data["list"][0]["weather"][0]["id"]



for hour_data in weather_data["list"]:
    condition_id = hour_data["weather"][0]["id"] 
    if int(condition_id) < 700 : 
        will_rain= True

if will_rain:
    client = Client(account_sid,account_token)
    message = client.messages \
        .create(
            body = "its going to rain today",
            from_ = "+13614056564",
            to  = "+919500617928"
        )
    print(message.status)
   