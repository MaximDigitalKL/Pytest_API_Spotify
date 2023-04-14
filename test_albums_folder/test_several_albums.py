from albums.request_several_albums import (
    get_several_albums,
    get_several_albums_with_market_filter,
    get_several_albums_with_invalid_market
)
from album_sample_data import SpotifyAlbum


def test_get_several_albums_validation():
    response = get_several_albums()
    assert response.status_code == 200
    assert 'cache-control' in response.headers
    assert response.headers['access-control-max-age'] == '604800'

    response_data = response.json()
    expected_names = SpotifyAlbum.several_album_names()
    assert len(response_data['albums']) == 3
    actual_names = tuple(x['name'] for x in response_data['albums'])  #list/generator comprehension
    assert actual_names == expected_names
    
def test_get_several_albums_with_market_invalid_market():
    response = get_several_albums_with_invalid_market()
    assert response.status_code == 400
    response_data = response.json()
    assert response_data['error']['message'] == 'Invalid market code'



#------------Only two albums out of the 3 are available in TR------------# possible bug, question to devs, how filters should work
# def test_get_several_albums_with_market_albums_availability():
#     response = get_several_albums_with_market_filter()
#     assert len(response.json()['albums']) == 2
