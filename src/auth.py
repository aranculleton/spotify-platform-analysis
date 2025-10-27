"""
Spotify API Authentication Module
Handles authentication with automatic token caching
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables
load_dotenv('config/.env')

def get_spotify_client(cache_path='.cache'):
    """
    Get authenticated Spotify client
    Returns: Authenticated spotipy.Spotify object
    """
    
    # Set up authentication with open_browser=True
    auth_manager = SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope=os.getenv('SPOTIFY_SCOPE'),
        cache_path=cache_path,
        open_browser=True  # This is key!
    )
    
    return spotipy.Spotify(auth_manager=auth_manager)