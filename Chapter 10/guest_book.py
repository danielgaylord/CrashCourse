filename = 'guest_book.txt'

with open(filename, 'a') as file:
    active = True

    while active:
        name = input("Please enter your name (enter 'q' to quit): ")
        if name == 'q':
            break
        file.write(name + "\n")
