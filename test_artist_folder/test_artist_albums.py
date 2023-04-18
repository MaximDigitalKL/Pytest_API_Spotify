from artists.request_artist_albums import get_artist_album
from sample_data_folder.artist_sample_data import SpotifyArtistAlbum


def test_artist_album_validation():
    response = get_artist_album()
    assert response.status_code == 200

    response_data = response.json()
    expected_album = SpotifyArtistAlbum.make_artist_album()
    assert response_data['items'][0]['id'] == expected_album.id
    assert response_data['items'][0]['name'] == expected_album.name
    assert response_data['items'][0]['release_date'] == expected_album.release_date
    assert response_data['items'][0]['total_tracks'] == expected_album.total_tracks
    assert response_data['items'][0]['type'] == expected_album.album_type
    assert 'US' in response_data['items'][0]['available_markets']
    assert len(response_data['items']) == 20
    assert len(response_data['items'][0]['available_markets']) == 184


