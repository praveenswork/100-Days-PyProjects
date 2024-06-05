import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "praveenisgod"
TOKEN = "97242638246"
GRAPHID = "graph1"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes"

}

graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params ={
    "id" : GRAPHID ,
    "name" : "running",
    "unit" : "km",
    "type" : "float",
    "color" : "momiji",
}
headers = {
        "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
today = datetime.now()

graph_pixel_endpoint = f" {graph_endpoint}/{GRAPHID}"


graph_pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "10.2",

}

# response = requests.post(url=graph_pixel_endpoint,json=graph_pixel_params, headers=headers)
# print(response.text)

put_pixel_endpoint = f" {graph_pixel_endpoint}/add"

put_pixel_params = {
    "quantity": "12.3"
}

# response = requests.put(url=put_pixel_endpoint,json=put_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{graph_pixel_endpoint}/{20240528}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)