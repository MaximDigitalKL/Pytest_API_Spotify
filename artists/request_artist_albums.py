import requests
from authorization.request_authorization import make_auth_header
from sample_data_folder.artist_sample_data import SpotifyArtist


def get_artist_album():
    artist = SpotifyArtist.make_valid_artist()
    api_url = f'https://api.spotify.com/v1/artists/{artist.id}/albums'
    response =  requests.get(api_url, headers=make_auth_header())
    return response