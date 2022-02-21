from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = ""  # insert client ID
SPOTIPY_CLIENT_SECRET = ""  # insert client key
SPOTIPY_REDIRECT_URI = 'http://example.com'
SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
top100_url = "https://www.billboard.com/charts/hot-100/{0}".format(user_date)

response = requests.get(url=top100_url)
top100_webpage = response.text
soup = BeautifulSoup(top100_webpage, "html.parser")

top100_songs = soup.find_all(name="span", class_="chart-element__information__song")
song_names = [songs.getText() for songs in top100_songs]

song_uris = []
for song in song_names:
    query = "track: {0}".format(song)
    song_dict = sp.search(q=query, type="track")
    try:
        # song_uri = song_dict["tracks"]["items"][0]["album"]["artists"][0]["id"]
        song_uri = song_dict["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print("{0} does not exist on Spotify".format(song))

new_playlist = sp.user_playlist_create(user_id, "{0} Billboard 100".format(user_date), public=False)
playlist_id = new_playlist["id"]
sp.playlist_add_items(playlist_id, song_uris)
