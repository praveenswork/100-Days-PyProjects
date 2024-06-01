import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/1c303ce0021e12124dcbf75095a932d6/workoutPythonCsv/sheet1"
API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")

user_query = input("tell about your workout")

headers = {
    "Content-Type": 'application/json',
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY
}

track_params = {
    "query" :user_query,
}

response = requests.post(url=endpoint, headers=headers, json=track_params)
response.raise_for_status()
exercises_data = response.json()["exercises"][0]
duration = exercises_data["duration_min"]
calories = exercises_data["nf_calories"]
exercises_name = exercises_data["name"]
met = exercises_data["met"]
now = datetime.now()
today_date = now.strftime("%Y-%m-%d")

date = datetime.now()

body ={
    "sheet1" : {
        "date":today_date,
        "exercise":exercises_name,
        "duration" :duration,
        "calories":calories,
        "met":met,
    }
}
response = requests.post(url=sheety_url,json=body)
print(response.text)
