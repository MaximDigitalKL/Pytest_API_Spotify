import pytest
from api_layer import call_api
from authorization.request_authorization import make_auth_header
from sample_data_folder.album_sample_data import SpotifyAlbum
from sample_data_folder.artist_sample_data import SpotifyArtist


@pytest.fixture
def auth_header():
    token = make_auth_header()
    header = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    return header


@pytest.fixture
def album_id():
    album = SpotifyAlbum.make_valid_album()
    return album.id


@pytest.fixture
def user_album(album_id, auth_header):
    api_url = f"me/albums/{album_id}"
    response = call_api(api_url, "PUT", payload=None, headers=auth_header)
    return response


@pytest.fixture
def artist_id():
    artist = SpotifyArtist.make_valid_artist()
    return artist.id