def make_sandwich(*ingredients):
    print("\nOn your sandwich you would like: ")
    for ingredient in ingredients:
        print(" - " + ingredient)

make_sandwich('bread')
make_sandwich('bread', 'ham')
make_sandwich('bread', 'ham', 'cheese')
