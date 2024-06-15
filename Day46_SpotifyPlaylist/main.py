import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
# Get Billboard data
date = input("Which date (yyyy-mm-dd) do you want to get the top songs from? ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
all_songs = soup.select("li ul li h3")

song_list = [song.get_text().strip() for song in all_songs]
print("Billboard Top Songs:")
for idx, song in enumerate(song_list, 1):
    print(f"{idx}. {song}")

# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Get Spotify access token
token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}
token_headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
token_response = requests.post("https://accounts.spotify.com/api/token", headers=token_headers, data=token_data)
token_response.raise_for_status()
access_token = token_response.json()["access_token"]
print(f"Access token: {access_token}")

# Spotify headers with the access token
spotify_headers = {
    "Authorization": f"Bearer {access_token}"
}

# Get details for each song from Spotify
for song in song_list:
    query = f"track:{song}"
    spotify_response = requests.get(url=f'https://api.spotify.com/v1/search?q={query}&type=track&limit=1', headers=spotify_headers)
    spotify_response.raise_for_status()
    tracks = spotify_response.json()["tracks"]["items"]
    if tracks:
        track = tracks[0]
        track_name = track["name"]
        artist_name = track["artists"][0]["name"]
        spotify_url = track["external_urls"]["spotify"]
        print(f"Track: {track_name}, Artist: {artist_name}, URL: {spotify_url}")
    else:
        print(f"No match found on Spotify for: {song}")

