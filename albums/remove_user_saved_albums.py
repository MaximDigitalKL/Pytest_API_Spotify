import requests
from authorization.request_authorization import make_auth_header
from sample_data import SpotifyAlbum


def remove_user_albums():
    album = SpotifyAlbum.make_valid_album()
    api_url = f"https://api.spotify.com/v1/me/albums/{album.id}"
    response = requests.delete(api_url, headers=make_auth_header())
    return response