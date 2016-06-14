favorite_places = {'dan': ['home', 'water park', 'pool'], 'jim': ['gym', 'bar', 'pool'], 'shien': ['home', 'water park', 'beach']}

for person in favorite_places:
    print(person.title() + ":")
    for place in favorite_places[person]:
        print("\t" + place)
    print()