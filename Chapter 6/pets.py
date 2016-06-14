pet0 = {'name': 'Spot', 'type': 'dog', 'owner': 'dan'}
pet1 = {'name': 'Scar', 'type': 'cat', 'owner': 'jim'}
pet2 = {'name': 'Scale', 'type': 'snake', 'owner': 'shien'}

pets = [pet0, pet1, pet2]

for p in pets:
    for key in p:
        print(key + " is " + str(p[key]))
    print()