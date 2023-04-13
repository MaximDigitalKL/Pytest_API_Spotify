import requests
from authorization.request_authorization import make_auth_header


def get_user_albums():
    response = requests.get("https://api.spotify.com/v1/me/albums", headers=make_auth_header())
    return response