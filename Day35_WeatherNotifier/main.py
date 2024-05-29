import os
from twilio.http.http_client import TwilioHttpClient
import requests
from twilio.rest import *
from dotenv import load_dotenv

load_dotenv()

MyLat = 11.016844
MyLong = 76.955833

TWILIO_NUM = os.getenv("TWILIO_NUMBER")
MY_NUM = os.getenv("MY_NUMBER")
endpoint  = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.getenv("TWILIO_SID")
account_token = os.environ.get("TWILIO_AUTH_KEY")

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
 