from lib.artist import *

def test_album_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.artist == "Test Artist"
    assert artist.genre == "Test Genre"

def test_artists_format_nicely():
    artist = Artist(1, 'Test Artist', 'Test Genre')
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"
