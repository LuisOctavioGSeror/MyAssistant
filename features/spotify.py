import spotipy
import json
import webbrowser

from main.config import spotify_client_id, spotify_client_secret

SPOTIFY_ID = spotify_client_id
SPOTIFY_CLIENT_SECRET = spotify_client_secret

def connect_spotify_api():
    username = 'Mr. Luis'
    clientID = SPOTIFY_ID
    clientSecret = SPOTIFY_CLIENT_SECRET
    redirect_uri = 'http://localhost:3000'
    oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()

    print(json.dumps(user_name, sort_keys=True, indent=4))

    return spotifyObject

def play_a_song(specific_song) -> str:

    spotifyObject = connect_spotify_api()

    results = spotifyObject.search(specific_song, 1, 0, "track")
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)

    return "playing song"



if __name__ == "__main__":
    spotifyObject = connect_spotify_api()
    play_a_song("complicated")


