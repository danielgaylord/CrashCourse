filename = 'sherlock.txt'

with open(filename) as file:
    times = file.read().lower().count('the')

print("The word 'the' appeared " + str(times) + " times")