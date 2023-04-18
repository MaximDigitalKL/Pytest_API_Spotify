from artists.request_artist import (
    get_single_artist,
    get_single_artist_invalid
)

from sample_data_folder.artist_sample_data import SpotifyArtist

def test_single_artist_validation():
    response = get_single_artist()
    assert response.status_code == 200
    assert 'content-type' in response.headers
    assert 'cache-control' in response.headers
    assert 'content-encoding' in response.headers
    assert response.headers['Transfer-Encoding'] == 'chunked'

    response_data = response.json()
    expected_artist = SpotifyArtist.make_valid_artist()
    assert response_data['followers']
    assert 'rock' in response_data['genres']
    assert response_data['id'] == expected_artist.id
    assert response_data['name'] == expected_artist.name
    assert len(response_data['images']) == 3
    assert response_data['popularity'] == 82
    assert response_data['type'] == expected_artist.artist_type

def test_single_artist_invalid():
    response = get_single_artist_invalid()
    assert response.status_code == 400
    assert response.json()['error']['message'] == 'invalid id'
