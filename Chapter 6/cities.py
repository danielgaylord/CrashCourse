cities = {
    'blarg': {'country': 'afrg', 'population': 1000, 'fact': 'people smell'},
    'meurg': {'country': 'trgtrs', 'population': 1, 'fact': 'lots of toilets'},
    'drats': {'country': 'afrg', 'population': 505050505, 'fact': 'nice dogs'},
    }

for city in cities:
    print(city.title() + ":")
    for info in cities[city]:
        print("\t" + info.title() + ": " + str(cities[city][info]))
    print()