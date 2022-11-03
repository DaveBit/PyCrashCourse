def make_album(artist_name, album_title, tracks_number=0):
    #  prepare the dictionary
    album_dic = {'artist': artist_name.title(),
                 'album': album_title.title(),
                 }
    if tracks_number:
        album_dic['tracks'] = tracks_number
    return album_dic


#  prepare the prompts
title_prompt = "What's the artist name?"
artist_prompt = "What's the album name?"
tracks_prompt = "What's the number of tracks?"

#  prepare the while loop
while True:
    print("Insert 'quit' to exit the program")
    artist_name = input(title_prompt)
    if artist_name == 'quit':
        break
    album_title = input(artist_prompt)
    if album_title == 'quit':
        break
    tracks_number = input("What's the number of tracks? (Insert 0 if you don't know)")
    if tracks_number == 'quit':
        break
    elif int(tracks_number) == 0:
        album = make_album(artist_name, album_title)
    else:
        album = make_album(artist_name, album_title, int(tracks_number))
    print(album)