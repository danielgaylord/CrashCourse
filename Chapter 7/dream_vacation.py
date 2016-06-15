dreams = {}
active = True

while active:
    name = input("What is your name? ")
    vacation = input("Where would you most like to visit? ")
    dreams[name] = vacation

    next = input("Would someone else like to enter their dream vacation? (yes/no)")
    if next == 'no':
        active = False

print('\nHere is everyone"s dream vacation: ')
for name, vacation in dreams.items():
    print('\t' + name.title() + " wants to go to " + vacation.title())
