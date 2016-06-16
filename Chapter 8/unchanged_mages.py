def show_magicians(magicians):
    for mage in magicians:
        print(mage.title())

def make_great(magicians):
    new_mages = []
    for mage in magicians:
        new_mages.append(mage + ' the Great')
    return new_mages

mages = ['merlin', 'dumbledore', 'gandalf']
show_magicians(make_great(mages[:]))
show_magicians(mages)