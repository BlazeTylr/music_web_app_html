import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from flask import Flask, request

app = Flask(__name__)

@app.route('/albums', methods=['POST'])
def post_album():
    if has_invalid_album_parameters(request.form):
        return 'You need to submit a title, release_year and artist_id', 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, 
                request.form['title'],
                request.form['release_year'],
                request.form['artist_id'])
    repository.create(album)
    return '', 200

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    
    return '\n'.join(f'{album}' for album in repository.all())

def has_invalid_album_parameters(form):
    return 'title' not in form or 'release_year' not in form or 'artist_id' not in form

@app.route('/albums/<int:album_id>', methods=['GET'])
def get_album(album_id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.find(album_id)
    
    if album:
        html_content = f"""
        <html>
            <head></head>
            <body>
                <h1>{album.title}</h1>
                <p>
                    Release year: {album.release_year}<br>
                    Artist id: {album.artist_id}
                </p>
            </body>
        </html>
        """
        return html_content, 200
    else:
        return 'Album not found', 404

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

