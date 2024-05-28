import os
from twilio.http.http_client import TwilioHttpClient
import requests
from twilio.rest import *

MyLat = 11.016844
MyLong = 76.955833

TWILIO_NUM = "+13614056564"
MY_NUM = "+919500617928"
endpoint  = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC87da0003fadd90cc691b5e1e13b03e6f"
account_token = os.environ.get("OWM_AUTH_TOKEN")

parameter = {
    "lat":MyLat,
    "lon":MyLong,
    "appid":api_key,
    "cnt":5
}

response = requests.get(endpoint, params = parameter)
response.raise_for_status()
weather_data = response.json()
data= weather_data["list"][0]["weather"][0]["id"]
degree_data =  weather_data["list"][0]['main']['temp']

for hour_data in weather_data["list"]:
    condition_id = hour_data["weather"][0]["id"]
    K_degree =  hour_data['main']['temp'] 
    celsius = round(K_degree - 273.15,2)
    if int(condition_id) < 700 : 
        will_rain= True
        #print(condition_id,celsius)
msg =(f"Rain expected with Condition ID:{condition_id},Temperature: {celsius}°C")

if will_rain:
    #proxy_client =TwilioHttpClient()
    #proxy_client.session.proxies = {'http':os.environ['https_proxy']}

    client = Client(account_sid,account_token)  #,http_client=proxy_client)
    message = client.messages \
        .create(
            body = msg,
            from_ = TWILIO_NUM,
            to  = MY_NUM
        )
    print(message.status)
 