def make_album(artist_name, album_title, tracks_number=0):
    if tracks_number:
        album = {'artist': artist_name.title(),
                 'album': album_title.title(),
                 'tracks_number': tracks_number}
    else:
        album = {'artist': artist_name, 'album': album_title}
    return album


album = make_album('Bob', 'Roses')
print(album)
album = make_album('Avril', 'Complicated')
print(album)
album = make_album('Jesus', 'Save us')
print(album)
album = make_album('Carlota', 'Renegade', 22)
print(album)
