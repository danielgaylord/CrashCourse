age = 0;

while age != 'quit':
    age = input("Please enter your age, or type 'quit' to exit: ")
    if age == 'quit':
        break
    else:
        if int(age) < 3:
            print("Free ticket!")
        elif int(age) >= 3 and int(age) <= 12:
            print("That'll be $10 please")
        else:
            print("$15 for your ticket, please")