"""
Simple test to see if we can get data from Spotify
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import pandas as pd

# Load credentials
load_dotenv('config/.env')

# Set up auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope=os.getenv('SPOTIFY_SCOPE')
))

# Get recent tracks
print("Fetching your recent tracks...")
results = sp.current_user_recently_played(limit=50)

# Look at what we got
print(f"\nFound {len(results['items'])} tracks")
print("\nFirst track:")
first_track = results['items'][0]
print(f"  Song: {first_track['track']['name']}")
print(f"  Artist: {first_track['track']['artists'][0]['name']}")
print(f"  Played at: {first_track['played_at']}")

# Convert to DataFrame just to see the structure
tracks_data = []
for item in results['items']:
    track = item['track']
    tracks_data.append({
        'played_at': item['played_at'],
        'track_name': track['name'],
        'artist_name': track['artists'][0]['name'],
        'duration_ms': track['duration_ms']
    })

df = pd.DataFrame(tracks_data)
print("\nDataFrame preview:")
print(df.head())

print("\n✓ Success! Data collection works.")