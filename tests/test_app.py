from lib.album_repository import *
from lib.artist_repository import *
# Tests for your routes go here

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Album(1, Wasting Light, 2010, 1)\n" \
        "Album(2, Speak Now, 2023, 2)"
    

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/albums.sql")
    response = web_client.post("/albums", data={
        'title': 'OK Computer',
        'release_year': '1997',
        'artist_id':'3'
    })
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Album(1, Wasting Light, 2010, 1)\n" \
        "Album(2, Speak Now, 2023, 2)\n" \
        "Album(3, OK Computer, 1997, 3)"
    
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/artists.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)"
    

def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/artists.sql")
    response = web_client.post("/artists", data={
        'artist': 'Wild Nothing',
        'genre': 'Indie'
    })
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)\n" \
        "Artist(5, Wild Nothing, Indie)"



# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
