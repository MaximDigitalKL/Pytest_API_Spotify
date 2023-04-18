from artists.request_artist_tracks import get_artist_tracks
from sample_data_folder.artist_sample_data import SpotifyArtistTrack


def test_artist_track_validation():
    response = get_artist_tracks()
    assert response.status_code == 200

    response_data = response.json()
    expected_track= SpotifyArtistTrack.make_artist_track()
    assert response_data['tracks'][0]['disc_number'] == expected_track.track_number
    assert response_data['tracks'][0]['duration_ms'] == expected_track.duration
    assert response_data['tracks'][0]['explicit'] == expected_track.explicit
    assert response_data['tracks'][0]['id'] == expected_track.id
    assert response_data['tracks'][0]['name'] == expected_track.name
    assert response_data['tracks'][0]['popularity'] == expected_track.popularity
    assert response_data['tracks'][0]['track_number'] == expected_track.track_number
    assert response_data['tracks'][0]['type'] == expected_track.track_type
    assert len(response_data['tracks']) == 10