def make_album(artist, title, tracks=0):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

print(make_album("soul'd out", 'alive'))
print(make_album("hearts on fire", 'cut/copy'))
print(make_album("abby road", 'the beatles'))
print(make_album("bogally doo", 'the lamos', 10))
