import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(URL + date)


soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
year = date.split("-")[0]
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

