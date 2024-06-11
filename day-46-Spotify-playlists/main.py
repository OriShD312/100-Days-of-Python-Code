import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Constants #
# CLIENT_ID = "f83b91ec7b784de8a24d601b89ebe2ec"
# CLIENT_SECRET = "704903bba97e4b5c9c3d0fce0078e159"

BILLBOARD_TOP_100_URL = "https://www.billboard.com/charts/hot-100/"

SPOTIFY_USERNAME = "21ngcz4vvxsg7kmx5ai2u4wpy"
SPOTIFY_API_ENDPOINT = "https://api.spotify.com/v1/search"
SPOTIFY_SCOPE = "playlist-modify-private"

# User date input #
target_date = input("Which date would you like to travel to? Please type it in the following format YYYY-MM-DD: ")
target_url = BILLBOARD_TOP_100_URL + target_date

# Scraping top 100 from billboard.com #
response = requests.get(target_url)
soup = BeautifulSoup(response.text, "html.parser")
filtered_soup = soup.select("li ul li h3.c-title, li ul li span.c-label.a-no-trucate")

# Organizing data into songs and artists in different parallel lists #
songs_and_artists = [song.getText().replace("\n", "").replace("\t", "").strip() for song in filtered_soup]
songs = songs_and_artists[0:len(songs_and_artists):2]
artists = songs_and_artists[1:len(songs_and_artists):2]

# Spotipy authentication ###
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SPOTIFY_SCOPE))
playlist_id = sp.user_playlist_create(SPOTIFY_USERNAME, f"{target_date} Billboard Top 100", public=False)["id"]

# Searching and adding songs from top 100 to new playlist #
target_year = target_date.split("-")[0]
top_100 = []
for i in range(0, len(songs)):
    try:
        results = sp.search(f"track:{songs[i]} artist:{artists[i]}")
        top_100.append(results["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{songs[i]} not found")

sp.playlist_add_items(playlist_id=playlist_id, items=top_100)
