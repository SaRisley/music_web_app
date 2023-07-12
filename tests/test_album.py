from lib.album import *

def test_album_constructs():
    album = Album(1, "Test Title", 2023, 1)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2023
    assert album.artist_id == 1

def test_books_format_nicely():
    album = Album(1, "Test Title", 2023, 1)
    assert str(album) == "Album(1, Test Title, 2023, 1)"
    # Try commenting out the `__repr__` method in lib/book.py
    # And see what happens when you run this test again.

    