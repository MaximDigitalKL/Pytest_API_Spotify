from api_layer import call_api
from sample_data_folder.album_sample_data import COUNTRIES
from sample_data_folder.artist_sample_data import (
    SpotifyArtist,
    SpotifyArtistAlbum,
    SpotifyArtistTrack,
    SpotifyRelatedArtist,
)


def test_artist_album_validation(auth_header):
    artist = SpotifyArtist.make_valid_artist()
    api_url = f"artists/{artist.id}/albums"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 200

    response_data = response.json()
    expected_album = SpotifyArtistAlbum.make_artist_album()
    assert response_data["items"][0]["id"] == expected_album.id
    assert response_data["items"][0]["name"] == expected_album.name
    assert response_data["items"][0]["release_date"] == expected_album.release_date
    assert response_data["items"][0]["total_tracks"] == expected_album.total_tracks
    assert response_data["items"][0]["type"] == expected_album.album_type
    assert "US" in response_data["items"][0]["available_markets"]
    assert len(response_data["items"]) == 20
    assert len(response_data["items"][0]["available_markets"]) == 184


def test_single_artist(auth_header):
    artist = SpotifyArtist.make_valid_artist()
    api_url = f"artists/{artist.id}"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 200
    assert "content-type" in response.headers
    assert "cache-control" in response.headers
    assert "content-encoding" in response.headers
    assert response.headers["Transfer-Encoding"] == "chunked"

    response_data = response.json()
    artist = SpotifyArtist.make_valid_artist()
    assert response_data["followers"]
    assert "rock" in response_data["genres"]
    assert response_data["id"] == artist.id
    assert response_data["name"] == artist.name
    assert len(response_data["images"]) == 3
    assert response_data["popularity"] == 81
    assert response_data["type"] == artist.artist_type


def test_get_single_artist_invalid_id(auth_header):
    artist = SpotifyArtist.make_valid_artist()
    api_url = f"artists/{artist.id}xs"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 400

    response_data = response.json()
    assert response_data["error"]["message"] == "invalid id"


def test_get_several_artists_validation(auth_header):
    artists = SpotifyArtist.several_artists_ids()
    api_url = f"artists?ids={artists}"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 200

    response_data = response.json()
    assert len(response_data["artists"]) == 3

    expected_names = SpotifyArtist.several_artists_names()
    actual_names = tuple(x["name"] for x in response_data["artists"])
    assert actual_names == expected_names


def test_artist_track(artist_id, auth_header):
    api_url = f"artists/{artist_id}/top-tracks?market={COUNTRIES[0]}"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 200

    response_data = response.json()
    expected_track = SpotifyArtistTrack.make_artist_track()
    assert response_data["tracks"][0]["disc_number"] == expected_track.track_number
    assert response_data["tracks"][0]["duration_ms"] == expected_track.duration
    assert response_data["tracks"][0]["explicit"] == expected_track.explicit
    assert response_data["tracks"][0]["id"] == expected_track.id
    assert response_data["tracks"][0]["name"] == expected_track.name
    assert response_data["tracks"][0]["popularity"] == expected_track.popularity
    assert response_data["tracks"][0]["track_number"] == expected_track.track_number
    assert response_data["tracks"][0]["type"] == expected_track.track_type
    assert len(response_data["tracks"]) == 10


def test_artist_related(artist_id, auth_header):
    api_url = f"artists/{artist_id}/related-artists"
    response = call_api(api_url, "GET", payload=None, headers=auth_header)
    assert response.status_code == 200

    response_data = response.json()
    assert len(response_data["artists"]) == 20

    expected_artist = SpotifyRelatedArtist.make_artist_one()
    assert expected_artist.genres in response_data["artists"][0]["genres"]
    assert response_data["artists"][0]["id"] == expected_artist.id
    assert response_data["artists"][0]["name"] == expected_artist.name
    assert response_data["artists"][0]["popularity"] == expected_artist.popularity

    expected_artist = SpotifyRelatedArtist.make_artist_two()
    assert expected_artist.genres in response_data["artists"][1]["genres"]
    assert response_data["artists"][1]["id"] == expected_artist.id
    assert response_data["artists"][1]["name"] == expected_artist.name
    assert response_data["artists"][1]["popularity"] == expected_artist.popularity

    expected_artist = SpotifyRelatedArtist.make_artist_three()
    assert expected_artist.genres in response_data["artists"][2]["genres"]
    assert response_data["artists"][2]["id"] == expected_artist.id
    assert response_data["artists"][2]["name"] == expected_artist.name
    assert response_data["artists"][2]["popularity"] == expected_artist.popularity
