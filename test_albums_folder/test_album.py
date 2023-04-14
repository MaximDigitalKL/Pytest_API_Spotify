from albums.request_album import (
    get_single_album,
    get_single_album_invalid,
    get_single_album_with_market,
    get_single_album_with_invalid_market
)
from album_sample_data import SpotifyAlbum, COUNTRIES


def test_single_album_validation():
    response = get_single_album()
    assert response.status_code == 200

    response_data = response.json()
    expected_album = SpotifyAlbum.make_valid_album()
    assert response_data['album_type'] == expected_album.album_type
    assert response_data['name'] == expected_album.name
    assert response_data['artists'][0]['name'] == expected_album.artist
    assert len(response_data['available_markets']) == 172
    assert COUNTRIES[1] not in response_data['available_markets']
    assert response_data['total_tracks'] == 75

def test_single_album_invalid():
    response = get_single_album_invalid()
    assert response.status_code == 400, "invalid album id, valid status code"
    
def test_single_album_with_market_validation():
    response = get_single_album_with_market()
    assert response.status_code == 200

    response_data = response.json()
    expected_album = SpotifyAlbum.make_valid_album()
    assert expected_album.copy_rights in response_data['copyrights'][0]['text']
    assert response_data['release_date'] == expected_album.release_date
    assert len(response_data['tracks']['items']) == 50

def test_single_album_with_market_invalid():
    response = get_single_album_with_invalid_market()
    assert response.status_code == 400
