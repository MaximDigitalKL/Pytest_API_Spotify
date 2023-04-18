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
            'id': '711MCceyCBcFnzjGY4Q7Un',
            'name': 'AC/DC',
            'genres': 'rock',
            'popularity': 82,
            'images': 3
        }
        return cls(**details)
    
    @classmethod
    def missing_artist_id(cls):
        return '711MCceyCBcFnzjGY4Q7Un4'
    
    @classmethod
    def several_artists_ids(cls):
        ids = ('711MCceyCBcFnzjGY4Q7Un', '6FBDaR13swtiWwGhX1WQsP', '27T030eWyCQRmDyuvr1kxY')
        return ",".join(ids)
    
    @classmethod
    def several_artists_names(cls):
        names = ('AC/DC', 'blink-182', 'Scorpions')
        return names

    
