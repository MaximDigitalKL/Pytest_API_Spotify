from dataclasses import dataclass


@dataclass
class SpotifyArtist:
    id: str
    name: str
    genres: str
    popularity: int
    images: int
    artist_type: str = "artist"
    followers: bool = True

    @classmethod
    def make_valid_artist(cls):
        details = {
            "id": "711MCceyCBcFnzjGY4Q7Un",
            "name": "AC/DC",
            "genres": "rock",
            "popularity": 82,
            "images": 3,
        }
        return cls(**details)


    @classmethod
    def several_artists_ids(cls):
        ids = (
            "711MCceyCBcFnzjGY4Q7Un",
            "6FBDaR13swtiWwGhX1WQsP",
            "27T030eWyCQRmDyuvr1kxY",
        )
        return ",".join(ids)

    @classmethod
    def several_artists_names(cls):
        names = ("AC/DC", "blink-182", "Scorpions")
        return names


@dataclass
class SpotifyArtistAlbum:
    id: str
    name: str
    release_date: str
    total_tracks: int
    album_type: str = "album"

    @classmethod
    def make_artist_album(cls):
        details = {
            "id": "3bTNxJYk2bwdWBMtrjBxb0",
            "name": "POWER UP",
            "release_date": "2020-11-13",
            "total_tracks": 12,
        }
        return cls(**details)


@dataclass
class SpotifyArtistTrack:
    disc_number: int
    duration: int
    explicit: bool
    id: str
    is_local: bool
    is_playable: bool
    name: str
    popularity: int
    track_number: int
    track_type: str = "track"

    @classmethod
    def make_artist_track(cls):
        details = {
            "disc_number": 1,
            "duration": 208400,
            "explicit": False,
            "id": "2zYzyRzz6pRmhPzyfMEC8s",
            "is_local": False,
            "is_playable": True,
            "name": "Highway to Hell",
            "popularity": 85,
            "track_number": 1,
        }
        return cls(**details)


@dataclass
class SpotifyRelatedArtist:
    id: str
    name: str
    genres: str
    popularity: int

    @classmethod
    def make_artist_one(cls):
        details = {
            "id": "6urzdpGY5yUimWZsgJUoTb",
            "name": "Airbourne",
            "genres": "hard rock",
            "popularity": 61,
        }
        return cls(**details)

    @classmethod
    def make_artist_two(cls):
        details = {
            "id": "3qm84nBOXUEQ2vnTfUTTFC",
            "name": "Guns N' Roses",
            "genres": "hard rock",
            "popularity": 80,
        }
        return cls(**details)

    @classmethod
    def make_artist_three(cls):
        details = {
            "id": "07XSN3sPlIlB2L2XNcTwJw",
            "name": "KISS",
            "genres": "glam rock",
            "popularity": 73,
        }
        return cls(**details)
