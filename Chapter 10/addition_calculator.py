active = True

while active:
    x = input("Please enter a number to add (or 'q' to quit): ")
    if x == 'q':
        break

    y = input("Please enter a number to add (or 'q' to quit): ")
    if y == 'q':
        break

    try:
        print(str(int(x) + int(y)))
    except TypeError:
        print("You need to enter actual numbers, dude!")
    except ValueError:
        print("You need to enter actual numbers, dude!")
