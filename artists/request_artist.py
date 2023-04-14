import requests
from artist_sample_data import SpotifyArtist
from authorization.request_authorization import make_auth_header


def get_single_artist():
    artist = SpotifyArtist.make_valid_artist()
    api_url = f"https://api.spotify.com/v1/artists/{artist.id}"
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_single_artist_invalid():
    artist_id = SpotifyArtist.missing_artist_id()
    api_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    response = requests.get(api_url, headers=make_auth_header())
    return response