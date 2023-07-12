# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# create album route
POST /albums
  title: string
  release_year: int
  artist_id: int
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# POST /albums
#  Parameters:
#    title: OK Computer
#    release_year : 1997
#    artist_id : 3
#  Expected response (200 OK):
"""
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

def test_post_submit(web_client):
    response = web_client.post('/albums', data={'title': 'OK Computer', 'release_year': 1997, 'artist_id': 3})
    assert response.status_code == 200
    
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album('Wasting Light', 2010, 1)\n" \
        "Album('Speak Now', 2023, 2)\n" \
        "Album('OK Computer, 1997, 3)"
```
