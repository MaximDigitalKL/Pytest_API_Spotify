from dataclasses import dataclass


COUNTRIES = ["RO", "TR", "XJZ"]


@dataclass
class SpotifyAlbum:
    id: str
    name: str
    artist: str
    copy_rights: str
    release_date: str
    album_type: str = "album"

    @classmethod
    def make_valid_album(cls):
        details = {
            "id": "5eA0qtE7Yu29XiMlwoby2G",
            "name": "Nevermind (30th Anniversary Super Deluxe)",
            "artist": "Nirvana",
            "copy_rights": "© 2021 UMG Recordings, Inc.",
            "release_date": "2021-11-12",
        }
        return cls(**details)

    @classmethod
    def several_album_ids(cls):
        ids = (
            "5eA0qtE7Yu29XiMlwoby2G",
            "4Gfnly5CzMJQqkUFfoHaP3",
            "2Lq2qX3hYhiuPckC8Flj21",
        )
        return ",".join(ids)

    @classmethod
    def several_album_names(cls):
        names = (
            "Nevermind (30th Anniversary Super Deluxe)",
            "Meteora",
            "Master Of Puppets (Remastered)",
        )
        return names


@dataclass
class SpotifyTrack:
    track_id: str
    track_name: str
    track_duration: int
    track_number: int
    track_type: str = "track"

    @classmethod
    def make_valid_track(cls):
        track_details = {
            "track_id": "4TMhakloPMPS84lNHNTSa3",
            "track_name": "Smells Like Teen Spirit - Remastered 2021",
            "track_duration": 300893,
            "track_type": "track",
            "track_number": 1,
        }
        return cls(**track_details)
