def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('nf', 'hope')
print(album)

album = make_album('michael jackson', 'history')
print(album)

album = make_album('lil uzi vert', 'luv is rage 2')
print(album)