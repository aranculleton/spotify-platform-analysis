"""
Spotify API Authentication Module
Handles OAuth authentication for multiple users
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import json
from pathlib import Path

class SpotifyAuthenticator:
    """Handle Spotify API authentication for multiple users"""
    
    def __init__(self, config_path='config/.env'):
        """Initialise authenticator with credentials"""
        load_dotenv(config_path)
        
        self.client_id = os.getenv('SPOTIPY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
        self.scope = os.getenv('SPOTIFY_SCOPE')
        
        # User mapping file (NOT committed to git)
        self.mapping_file = Path('data/processed/user_mapping.json')
        self.user_mapping = self._load_user_mapping()
        
    def _load_user_mapping(self):
        """Load user ID to pseudonym mapping"""
        if self.mapping_file.exists():
            with open(self.mapping_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_user_mapping(self):
        """Save user mapping to file"""
        self.mapping_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.mapping_file, 'w') as f:
            json.dump(self.user_mapping, f, indent=2)
    
    def authenticate_user(self, user_label=None):
        """
        Authenticate a user and return Spotify client
        
        Args:
            user_label: Optional label for this user (e.g., 'friend1')
        
        Returns:
            Tuple of (spotify_client, anonymised_user_id)
        """
        # Create auth manager
        auth_manager = SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope,
            cache_path=f'.cache-{user_label}' if user_label else '.cache'
        )
        
        # Create Spotify client
        sp = spotipy.Spotify(auth_manager=auth_manager)
        
        # Get user's actual Spotify ID
        user_info = sp.current_user()
        actual_user_id = user_info['id']
        
        # Create or retrieve anonymised ID
        if actual_user_id not in self.user_mapping:
            # Create new pseudonym
            user_number = len(self.user_mapping) + 1
            pseudonym = f"User_{chr(64 + user_number)}"  # User_A, User_B, etc.
            self.user_mapping[actual_user_id] = pseudonym
            self._save_user_mapping()
            print(f"✓ New user authenticated: {pseudonym}")
        else:
            pseudonym = self.user_mapping[actual_user_id]
            print(f"✓ Existing user authenticated: {pseudonym}")
        
        return sp, pseudonym
    
    def get_all_authenticated_users(self):
        """Get list of all authenticated pseudonyms"""
        return list(self.user_mapping.values())


# Example usage
if __name__ == "__main__":
    auth = SpotifyAuthenticator()
    
    # Authenticate first user
    print("Authenticate User 1 (you)")
    sp1, user1_id = auth.authenticate_user('self')
    
    # Authenticate friends (they'll need to run this on their device)
    print("\nAuthenticate User 2 (friend 1)")
    sp2, user2_id = auth.authenticate_user('friend1')