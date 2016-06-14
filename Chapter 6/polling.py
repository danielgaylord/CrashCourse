favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

need_to_take = ['dan', 'jen', 'jim', 'sarah']

for name in need_to_take:
    if name in favorite_languages.keys():
        print("Thanks for taking the poll " + name.title())
    else:
        print("Hey, " + name.title() + ", you still need to take the poll!")