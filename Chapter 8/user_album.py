def make_album(artist, title, tracks=0):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

active = True
while active:
    artist = input("Enter an artist (or 'q' to quit): ")
    if artist == 'q':
        break

    title = input("Enter an album title (or 'q' to quit): ")
    if title == 'q':
        break

    print(make_album(artist, title))
