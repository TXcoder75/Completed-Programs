from random import randint

"""This will be a simple dice roll game of 2 dice.  The object of this is to be able to roll 2 6-sided dice"""


die_1 = randint(1, 6)
die_2 = randint(1, 6)
outcome = die_1 + die_2

print("you rolled a {} for your first number".format(die_1))
print("You rolled a {} for your second number".format(die_2))
print("You rolled a total of {}".format(outcome))
if outcome == 2:
    print("Awww, Snake eyes!")
elif outcome == 7:
    print("Winner")
elif outcome == 11:
    print("Winner")
elif outcome == 3 or 4 or 5 or 6 or 8 or 9 or 10:
    print("Roll again")