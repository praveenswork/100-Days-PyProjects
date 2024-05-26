import requests
import datetime as dt
import json

my_lat = 11.016844
my_lng = 76.955833
current_time =  dt.datetime.now()
parameter = {
    "lat":my_lat,
    "lng":my_lng,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']


print(sunrise.split('T')[1].split(":")[0])

print(sunset.split('T')[1].split(":")[0])
print(current_time)
