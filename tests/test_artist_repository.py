from lib.artist import Artist
from lib.artist_repository import ArtistRepository

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection) 

    artists = repository.all()
    assert artists == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]


def test_create_record(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "Wild Nothing", "Indie"))

    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild Nothing', 'Indie')
    ]
