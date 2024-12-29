from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

playlist_id = "0nfWE9tf1Br9GRwhtS5dtG"

results = sp.playlist_items(playlist_id, limit=10)

track_ids = [item["track"]["id"] for item in results["items"]]
"""
in the future spotify will allow users to download audio features, but for now Get Track's Audio Features method is 
deprecated and users are now allowed to use is, so i have to use some done datasets by other users ;((
"""




