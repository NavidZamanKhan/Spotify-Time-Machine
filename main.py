from bs4 import BeautifulSoup
import requests, spotipy, os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv("client.env")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]

date = input("Enter the date you want to travel to (YYYY-MM-DD): ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

if not song_names:
    print(f"No songs found for the date {date}.")
    exit()

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    if result["tracks"]["items"]:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    else:
        print(f"{song} doesn't exist on Spotify. Skipped.")

if song_uris:
    print(f"Collected {len(song_uris)} songs from Spotify.")
    playlist_name = f"{date} Billboard Hot 100"
    playlist_description = f"Top 100 songs from Billboard on {date}"
    playlist = sp.user_playlist_create(
        user=user_id, name=playlist_name, public=False, description=playlist_description
    )

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

    print(f"Playlist '{playlist_name}' created successfully!")
    print(f"Playlist URL: {playlist['external_urls']['spotify']}")
else:
    print("No songs could be added to the playlist.")
