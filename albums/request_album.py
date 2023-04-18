import requests
from sample_data_folder.album_sample_data import SpotifyAlbum, COUNTRIES
from authorization.request_authorization import make_auth_header


def get_single_album():
    album = SpotifyAlbum.make_valid_album()
    api_url = f"https://api.spotify.com/v1/albums/{album.id}"
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_single_album_invalid():
    album_id = SpotifyAlbum.missing_album_id()
    api_url = f"https://api.spotify.com/v1/albums/{album_id}"
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_single_album_with_market():
    album = SpotifyAlbum.make_valid_album()
    api_url = f"https://api.spotify.com/v1/albums/{album.id}?market={COUNTRIES[0]}"
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_single_album_with_invalid_market():
    album = SpotifyAlbum.make_valid_album()
    api_url = f"https://api.spotify.com/v1/albums/{album.id}?market={COUNTRIES[2]}"
    response = requests.get(api_url, headers=make_auth_header())
    return response