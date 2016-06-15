ent = ""

while ent != 'quit':
    ent = input("Type 'quit' to quit: ")
print("Exited 1/3 loops")

ent = ""
active = True

while active:
    ent = input("Type 'quit' to quit: ")
    if ent == 'quit':
        active = False
print("Exited 2/3 loops")

ent = ""

while True:
    ent = input("Type 'quit' to quit: ")
    if ent == 'quit':
        break
print("Exited 3/3 loops")
