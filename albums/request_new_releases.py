import requests
from authorization.request_authorization import make_auth_header
from sample_data_folder.album_sample_data import COUNTRIES


def get_new_releases_with_valid_country():
    api_url = f'https://api.spotify.com/v1/browse/new-releases?market={COUNTRIES[0]}'
    response = requests.get(api_url, headers=make_auth_header())
    return response

def get_new_releases_with_invalid_country():
    api_url = f'https://api.spotify.com/v1/browse/new-releases?market={COUNTRIES[2]}'
    response = requests.get(api_url, headers=make_auth_header())
    return response