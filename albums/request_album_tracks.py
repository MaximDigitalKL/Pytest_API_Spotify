import requests
from album_sample_data import SpotifyAlbum
from authorization.request_authorization import make_auth_header


def get_album_tracks():
    album = SpotifyAlbum.make_valid_album()
    api_url = f"https://api.spotify.com/v1/albums/{album.id}/tracks"
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_album_tracks_invalid():
    album_id = SpotifyAlbum.missing_album_id()
    api_url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    response = requests.get(api_url, headers=make_auth_header())
    return response

