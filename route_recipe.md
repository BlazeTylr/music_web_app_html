# {{ Albums }} Route Design Recipe

## 1. Design the Route Signature

```
# Request:
POST /albums
    title: string
    release_year: number (str)
    artist_id: number (str)

GET /albums
```

## 2. Create Examples as Tests

```python

# POST /albums
# title: 'Randezvous'
# release_year: 2023
# artist_id: 2
#  Expected response (200 OK):
"""
(no content)
"""

# GET /albums
#  Expected response (200 OK):
"""
Album (1, 'Imagine', 1978, 1)
Album (2, 'Randesvouz', 2023, 1)
"""

# POST /albums
#  Expected response (400 Bad Request):
"""
(no content)
"""

# GET /albums
#  Expected response (200 OK):
"""
Album (1, 'Imagine', 1978, 1)
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```
