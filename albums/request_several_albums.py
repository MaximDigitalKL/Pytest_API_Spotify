import requests
from authorization.request_authorization import make_auth_header
from sample_data import SpotifyAlbum, COUNTRIES


def get_several_albums():
    albums = SpotifyAlbum.several_album_ids()
    api_url = f'https://api.spotify.com/v1/albums?ids={albums}'
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_several_albums_with_market():
    albums = SpotifyAlbum.several_album_ids()
    api_url = f'https://api.spotify.com/v1/albums?ids={albums}&market={COUNTRIES[0]}'
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_several_albums_with_market_filter():
    albums = SpotifyAlbum.several_album_ids()
    api_url = f'https://api.spotify.com/v1/albums?ids={albums}&market={COUNTRIES[1]}'
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_several_albums_with_invalid_market():
    albums = SpotifyAlbum.several_album_ids()
    api_url = f'https://api.spotify.com/v1/albums?ids={albums}&market={COUNTRIES[2]}'
    response = requests.get(api_url, headers=make_auth_header())
    return response