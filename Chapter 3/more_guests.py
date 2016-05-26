famous = []
famous.append('Abraham')
famous.append('Bill')
famous.append('Vin')

print("Hey " + famous[0] + ", would you like to join me for dinner?")
print("Hey " + famous[1] + ", would you like to join me for dinner?")
print("Hey " + famous[2] + ", would you like to join me for dinner?")

print()
print("Oh..." + famous[0] + " can't make it...well then...")

famous[0] = 'Robert'

print()
print("Hey " + famous[0] + ", would you like to join me for dinner?")
print("Hey " + famous[1] + ", would you like to join me for dinner?")
print("Hey " + famous[2] + ", would you like to join me for dinner?")

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
