from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, roll_times=1):
        results = []
        for roll in range(roll_times):
            results.append(randint(1, self.sides))
        print(results)


print("_____Die6_____")
die6 = Die()
die6.roll_die(10)

print("_____Die10_____")
die10 = Die(10)
die10.roll_die(10)

print("_____Die20_____")
die20 = Die(20)
die20.roll_die(10)

