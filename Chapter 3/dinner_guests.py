famous = []
famous.append('Abraham')
famous.append('Bill')
famous.append('Vin')

print("Hey " + famous[0] + ", would you like to join me for dinner?")
print("Hey " + famous[1] + ", would you like to join me for dinner?")
print("Hey " + famous[2] + ", would you like to join me for dinner?")
print("Currently inviting " + str(len(famous)) + " guests for dinner")

print()
print("Oh..." + famous[0] + " can't make it...well then...")

famous[0] = 'Robert'

print()
print("Hey " + famous[0] + ", would you like to join me for dinner?")
print("Hey " + famous[1] + ", would you like to join me for dinner?")
print("Hey " + famous[2] + ", would you like to join me for dinner?")
print("Currently inviting " + str(len(famous)) + " guests for dinner")

print()
print("Hey! I found a bigger table!")

famous.insert(0, 'Morgan')
famous.insert(int(famous.__len__()/2), 'Sam')
famous.append('Jackie')

print()
print("Hey " + famous[0] + ", would you like to join me for dinner?")
print("Hey " + famous[1] + ", would you like to join me for dinner?")
print("Hey " + famous[2] + ", would you like to join me for dinner?")
print("Hey " + famous[3] + ", would you like to join me for dinner?")
print("Hey " + famous[4] + ", would you like to join me for dinner?")
print("Hey " + famous[5] + ", would you like to join me for dinner?")
print("Currently inviting " + str(len(famous)) + " guests for dinner")

print()
print("Well this is awkward...I actually only have room for two guests...")

print()
print("Um, hey..." + famous.pop() + " there's actually no room for you. Maybe next time?")
print("Um, hey..." + famous.pop() + " there's actually no room for you. Maybe next time?")
print("Um, hey..." + famous.pop() + " there's actually no room for you. Maybe next time?")
print("Um, hey..." + famous.pop() + " there's actually no room for you. Maybe next time?")
print("Currently inviting " + str(len(famous)) + " guests for dinner")

print()
print("Hey " + famous[0] + ", we are still on for dinner, right?")
print("Hey " + famous[1] + ", we are still on for dinner, right?")
print("Currently inviting " + str(len(famous)) + " guests for dinner")

del famous[0]
del famous[0]

print()
print(famous)
print("Currently inviting " + str(len(famous)) + " guests for dinner")
