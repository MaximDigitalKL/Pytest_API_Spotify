from artists.request_artist_related_artists import get_artist_related_artists
from sample_data_folder.artist_sample_data import SpotifyRelatedArtist


def test_artist_related_artist_validation():
    response = get_artist_related_artists()
    assert response.status_code == 200

    response_data = response.json()
    assert len(response_data['artists']) == 20

    expected_artist= SpotifyRelatedArtist.make_artist_one()
    assert expected_artist.genres in response_data['artists'][0]['genres']
    assert response_data['artists'][0]['id'] == expected_artist.id
    assert response_data['artists'][0]['name'] == expected_artist.name
    assert response_data['artists'][0]['popularity'] == expected_artist.popularity

    expected_artist= SpotifyRelatedArtist.make_artist_two()
    assert expected_artist.genres in response_data['artists'][1]['genres']
    assert response_data['artists'][1]['id'] == expected_artist.id
    assert response_data['artists'][1]['name'] == expected_artist.name
    assert response_data['artists'][1]['popularity'] == expected_artist.popularity

    expected_artist= SpotifyRelatedArtist.make_artist_three()
    assert expected_artist.genres in response_data['artists'][2]['genres']
    assert response_data['artists'][2]['id'] == expected_artist.id
    assert response_data['artists'][2]['name'] == expected_artist.name
    assert response_data['artists'][2]['popularity'] == expected_artist.popularity
    