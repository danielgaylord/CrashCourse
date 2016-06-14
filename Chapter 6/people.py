person0 = {'first_name': "Dan", 'last_name': "Gaylord", 'city': "Hamilton", 'age': 29}
person1 = {'first_name': "Shien", 'last_name': "Zou", 'city': "Bellerose", 'age': 28}
person2 = {'first_name': "Jim", 'last_name': "Gaylord", 'city': "DC", 'age': 27}

people = [person0, person1, person2]

for p in people:
    for key in p:
        print(key + " is " + str(p[key]))
    print()