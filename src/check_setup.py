"""
Check if everything is set up correctly
"""
from dotenv import load_dotenv
import os

load_dotenv('config/.env')

print("="*50)
print("CHECKING YOUR SETUP")
print("="*50)

# Check each variable
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
scope = os.getenv('SPOTIFY_SCOPE')

print("\n1. CLIENT ID:")
if client_id:
    print(f"   ✓ Found: {client_id[:10]}... (first 10 chars)")
    if 'your_' in client_id.lower():
        print("   ✗ ERROR: You still have placeholder text!")
        print("   → Go to Spotify Dashboard and copy your real Client ID")
else:
    print("   ✗ Missing!")

print("\n2. CLIENT SECRET:")
if client_secret:
    print(f"   ✓ Found: {client_secret[:10]}... (first 10 chars)")
    if 'your_' in client_secret.lower():
        print("   ✗ ERROR: You still have placeholder text!")
        print("   → Go to Spotify Dashboard and copy your real Client Secret")
else:
    print("   ✗ Missing!")

print("\n3. REDIRECT URI:")
if redirect_uri:
    print(f"   ✓ Found: {redirect_uri}")
    if redirect_uri == 'http://127.0.0.1:8888/callback':
        print("   ✓ Correct format!")
    else:
        print("   ⚠ Warning: Should be http://127.0.0.1:8888/callback")
else:
    print("   ✗ Missing!")

print("\n4. SCOPE:")
if scope:
    print(f"   ✓ Found: {scope}")
else:
    print("   ✗ Missing!")

print("\n" + "="*50)

# Check if ready
if all([client_id, client_secret, redirect_uri, scope]):
    if 'your_' not in client_id.lower() and 'your_' not in client_secret.lower():
        print("✓ ALL CHECKS PASSED - Ready to authenticate!")
    else:
        print("✗ STILL HAVE PLACEHOLDER VALUES")
        print("\nTO FIX:")
        print("1. Go to https://developer.spotify.com/dashboard")
        print("2. Click your app")
        print("3. Click 'Settings'")
        print("4. Copy Client ID and Client Secret")
        print("5. Paste into config/.env")
else:
    print("✗ MISSING REQUIRED VALUES")

print("="*50)