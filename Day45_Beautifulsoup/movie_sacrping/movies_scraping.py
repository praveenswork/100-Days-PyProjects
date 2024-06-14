import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_web = response.text

soup = BeautifulSoup(movie_web,"html.parser")
tags = soup.find_all("h3")

movies_name = []
for tag in tags:
    new = tag.get_text().split()[1:]
    new_data = ' '.join(new)
    # movies_name.append(new_data)
    movies_name.append(new_data)

with open("new_data.txt", "w") as file:
    for names in movies_name:
        file.write(names + "\n")
    
