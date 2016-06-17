filename = 'programming_poll.txt'

with open(filename, 'a') as file:
    active = True

    while active:
        reason = input("Why do you like programming? (enter 'q' to quit): ")
        if reason == 'q':
            break
        file.write(reason + "\n")