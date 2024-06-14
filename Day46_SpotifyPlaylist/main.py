import requests
from bs4 import BeautifulSoup

# date =input("Which date moth and year want to hear (yyyy-mm-dd)")
response = requests.get("https://www.billboard.com/charts/hot-100/2020-06-13/")
# data = response.text

soup = BeautifulSoup(response.text,'html.parser')
all_songs = soup.select("li ul li h3")

song_list = [song.get_text().strip() for song in all_songs]
print(song_list)


