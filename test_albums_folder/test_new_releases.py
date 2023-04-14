from albums.request_new_releases import (
    get_new_releases_with_valid_country,
    get_new_releases_with_invalid_country
)
from album_sample_data import COUNTRIES


def test_new_releases_with_valid_country_validation():
    response = get_new_releases_with_valid_country()
    assert response.status_code == 200
    assert "content-type" in response.headers
    assert "cache-control" in response.headers
    assert response.headers["Transfer-Encoding"] == "chunked"

    response_data = response.json()
    assert response_data["albums"]["items"][0]["type"] == "album"
    assert response_data["albums"]["items"][0]["release_date_precision"] == "day"
    assert response_data["albums"]["items"][0]["is_playable"]
    assert len(response_data["albums"]["items"]) == 20
    assert response_data["albums"]["limit"] == 20
    assert COUNTRIES[0] in response_data["albums"]["next"]

def test_new_releases_with_invalid_country():
    response = get_new_releases_with_invalid_country()
    assert response.status_code == 400
    
    response_data = response.json()
    assert response_data["error"]["message"] == "Invalid country code"


