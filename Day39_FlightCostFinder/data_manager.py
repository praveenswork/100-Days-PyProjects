import os
import requests
import pandas as pd
from twilio.rest import Client

# Ensure the environment variables are set correctly
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_KEY = os.environ.get("TWILIO_AUTH_KEY")

# Sheety API endpoint
sheety_endpoint = "https://api.sheety.co/1c303ce0021e12124dcbf75095a932d6/myCostFlightFinder/prices"

# Amadeus API credentials
API_KEY = "C9riNiDQLBHAT4KeL2DoqEDvYG34CUur"
API_SECRET = "5tRZgAYiWTbNZFBL"
token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

#-----------------------------------------------------sheety--------------------------------------------------------------------------------#
# Fetch data from Sheety
try:
    sheety_response = requests.get(url=sheety_endpoint)
    sheety_response.raise_for_status()  # Raise an error for bad status codes
    data = sheety_response.json()["prices"]
    data_form = pd.DataFrame.from_dict(data)
    print(data_form)
except requests.RequestException as e:
    print(f"Error fetching data from Sheety: {e}")
    exit(1)

# Extract IATA codes
ITACODE = data_form["iataCode"].tolist()
print(ITACODE)

#-----------------------------------------------------flight--------------------------------------------------------------------------------#
# Fetch Amadeus API token
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
body = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET
}

try:
    token_response = requests.post(url=token_endpoint, headers=headers, data=body)
    token_response.raise_for_status()  # Raise an error for bad status codes
    new_token = token_response.json()["access_token"]
except requests.RequestException as e:
    print(f"Error fetching token from Amadeus API: {e}")
    exit(1)

# Set flight search parameters
from_location = "IND"
to_location = "TYO"
flight_params = {
    "originLocationCode": from_location,
    "destinationLocationCode": to_location,
    "departureDate": "2024-06-01",
    "adults": 1,
}

flight_headers = {
    "Authorization": f"Bearer {new_token}"
}

# Fetch flight offers
try:
    response = requests.get(url=flight_endpoint, headers=flight_headers, params=flight_params)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()["data"][1]
except requests.RequestException as e:
    print(f"Error fetching flight data from Amadeus API: {e}")
    exit(1)
except KeyError:
    print("Unexpected response format from Amadeus API")
    exit(1)

# Extract price and currency
currency = data["price"]["currency"]
price = data["price"]["total"]
print(currency, price)

#------------------------------------------------------------messages-----------------------------------------------------------------------#
# Message to send
message_format = f"Book your flight now, your registered country {from_location} to {to_location} flight price is low again at {price} {currency}"

# Send SMS if price is below threshold
if float(price) < 1000:
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_KEY)
        message = client.messages.create(
            body=message_format,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
        print(message.status)
    except Exception as e:
        print(f"Error sending SMS with Twilio: {e}")


