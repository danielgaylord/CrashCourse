usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello master, what would you like me to do today?")
        else:
            print("Hey, " + user + ", you loser")
else:
    print("We need users!")