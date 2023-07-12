from lib.album import Album
from lib.album_repository import AlbumRepository

def test_get_all_records(db_connection): 
    db_connection.seed("seeds/albums.sql")
    repository = AlbumRepository(db_connection) 

    albums = repository.all()
    assert albums == [
        Album(1, 'Wasting Light', 2010, 1),
        Album(2, 'Speak Now', 2023, 2),
    ]


def test_create_record(db_connection):
    db_connection.seed("seeds/albums.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "OK Computer", 1997, 3))

    result = repository.all()
    assert result == [
        Album(1, 'Wasting Light', 2010, 1),
        Album(2, 'Speak Now', 2023, 2),
        Album(3, 'OK Computer', 1997, 3)
    ]
