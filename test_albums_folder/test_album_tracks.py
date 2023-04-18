from albums.request_album_tracks import (
    get_album_tracks,
    get_album_tracks_invalid
)
from sample_data_folder.album_sample_data import SpotifyTrack


def test_get_album_tracks_validation():
    response = get_album_tracks()
    assert response.status_code == 200

    response_data = response.json()
    expected_track = SpotifyTrack.make_valid_track()
    assert len(response_data) == 7
    assert response_data['items'][0]['id'] == expected_track.track_id
    assert response_data['items'][0]['name'] == expected_track.track_name
    assert response_data['items'][0]['duration_ms'] == expected_track.track_duration
    assert response_data['items'][0]['type'] == expected_track.track_type
    assert response_data['items'][0]['track_number'] == expected_track.track_number


def test_get_album_tracks_invalid_status_code():
    response = get_album_tracks_invalid()
    assert response.status_code == 400