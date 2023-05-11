from api_layer import call_api
from sample_data_folder.album_sample_data import SpotifyAlbum, SpotifyTrack, COUNTRIES


def test_get_single_album(auth_header):
    album = SpotifyAlbum.make_valid_album()
    album_id = album.id
    api_url = f"albums/{album_id}"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["album_type"] == album.album_type
    assert response_data["name"] == album.name
    assert response_data["artists"][0]["name"] == album.artist
    assert len(response_data["available_markets"]) == 172
    assert COUNTRIES[1] not in response_data["available_markets"]
    assert response_data["total_tracks"] == 75


def test_get_single_album_invalid_id(auth_header):
    album = SpotifyAlbum.make_valid_album()
    album_id = album.id
    api_url = f"albums/{album_id}y"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 400

    response_data = response.json()
    expected_message = "invalid id"
    assert response_data["error"]["message"] == expected_message


def test_single_album_with_market_validation(auth_header):
    album = SpotifyAlbum.make_valid_album()
    album_id = album.id
    api_url = f"albums/{album_id}?market={COUNTRIES[0]}"
    response = call_api(
        api_url,
        "GET",
        payload=None,
        headers=auth_header,
    )
    assert response.status_code == 200

    response_data = response.json()
    assert album.copy_rights in response_data["copyrights"][0]["text"]
    assert response_data["release_date"] == album.release_date
    assert len(response_data["tracks"]["items"]) == 50


def test_single_album_with_market_invalid(auth_header):
    album = SpotifyAlbum.make_valid_album()
    album_id = album.id
    api_url = f"albums/{album_id}?market={COUNTRIES[2]}"
    response = call_api(
        api_url,
        "GET",
        payload=None,
        headers=auth_header,
    )
    assert response.status_code == 400

    response_data = response.json()
    expected_message = "Invalid market code"
    assert response_data["error"]["message"] == expected_message


def test_get_several_albums(auth_header):
    albums = SpotifyAlbum.several_album_ids()
    api_url = f"albums?ids={albums}"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 200
    assert "cache-control" in response.headers
    assert response.headers["access-control-max-age"] == "604800"

    response_data = response.json()
    expected_albums = SpotifyAlbum.several_album_names()
    assert len(response_data["albums"]) == 3
    actual_names = tuple(x["name"] for x in response_data["albums"])
    assert actual_names == expected_albums


def test_get_several_albums_with_invalid_market(auth_header):
    albums = SpotifyAlbum.several_album_ids()
    api_url = f"albums?ids={albums}&market={COUNTRIES[2]}"
    response = call_api(
        api_url,
        "GET",
        payload=None,
        headers=auth_header,
    )
    assert response.status_code == 400

    response_data = response.json()
    assert response_data["error"]["message"] == "Invalid market code"


# ------------Only two albums out of the 3 are available in TR------------
#        possible bug, question to devs, how filters should work
# def test_get_several_albums_with_market_albums_availability(auth_header):
#     albums = SpotifyAlbum.several_album_ids()
#     response = call_api(
#         f"albums?ids={albums}&market={COUNTRIES[1]}",
#         "GET",
#         payload=None,
#         headers=auth_header,
#     )
#     assert response.status_code == 200
#     assert len(response.json()["albums"]) == 2


def test_get_album_tracks(album_id, auth_header):
    api_url = f"albums/{album_id}/tracks"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 200

    response_data = response.json()
    expected_track = SpotifyTrack.make_valid_track()
    assert len(response_data) == 7
    assert response_data["items"][0]["id"] == expected_track.track_id
    assert response_data["items"][0]["name"] == expected_track.track_name
    assert response_data["items"][0]["duration_ms"] == expected_track.track_duration
    assert response_data["items"][0]["type"] == expected_track.track_type
    assert response_data["items"][0]["track_number"] == expected_track.track_number


def test_get_album_tracks_invalid_album_id(album_id, auth_header):
    api_url = f"albums/{album_id}s/tracks"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 400

    response_data = response.json()
    expected_message = "invalid id"
    response_data["error"]["message"] = expected_message


def test_new_releases_with_valid_country(auth_header):
    api_url = f"browse/new-releases?market={COUNTRIES[0]}"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
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


def test_new_releases_with_valid_country(auth_header):
    api_url = f"browse/new-releases?market={COUNTRIES[2]}"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 400

    response_data = response.json()
    assert response_data["error"]["message"] == "Invalid country code"
