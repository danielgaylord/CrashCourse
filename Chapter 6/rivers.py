rivers = {'nile': 'egypt', 'mississipi': "usa", 'french': "france"}

for river, country in rivers.items():
    print("The " + river.title() + " river runs through " + country.title())

print("\nRivers included:")
for river in sorted(rivers.keys()):
    print("\t" + river.title())

print("\nCountries included:")
for country in sorted(rivers.values()):
    print("\t" + country.title())