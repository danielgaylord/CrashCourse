from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

die = Die(6)
print("\nRolling 6-sided die:")
for x in range(1,11):
    print("\t" + str(x) + ": " + str(die.roll_die()))

die = Die(10)
print("\nRolling 10-sided die:")
for x in range(1,11):
    print("\t" + str(x) + ": " + str(die.roll_die()))

die = Die(20)
print("\nRolling 20-sided die:")
for x in range(1,11):
    print("\t" + str(x) + ": " + str(die.roll_die()))