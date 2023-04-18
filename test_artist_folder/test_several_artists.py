from artists.request_several_artists import get_several_artists
from sample_data_folder.artist_sample_data import SpotifyArtist


def test_get_several_artists_validation():
    response = get_several_artists()
    assert response.status_code == 200
    
    response_data =  response.json()
    assert len(response_data['artists']) == 3
    expected_names = SpotifyArtist.several_artists_names()
    actual_names = tuple(x['name'] for x in response_data['artists'])
    assert actual_names == expected_names


