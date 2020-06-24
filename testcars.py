""" This is the ford function for the main program below."""


def ford():
    choiceofcar = [1, 2, 3]
    number = (input("Which car do you want to choose: 1)Focus, 2)Mustang, or 3)Fusion"))
    if choiceofcar != number:
        print("Choose 1, 2, or 3 please")
    if number == 1 or "Focus":
        print("Focus has 5 letters in the name")
    elif number == 2 or "Mustang":
        print("The Mustang is hotter than a $2 pistol.  She is the hottest thing around")
    elif number == 3 or "Fusion":
        print("The Fusion is Meh.  Not much to say about it.  Sorry 'bout your luck dude.")


"""This is a function for Toyota cars that will eventually print a unique fact about each car"""


def toyota():
    choiceofcar = [1, 2, 3]
    number = (input("Which car do you want to choose: 1:Camry, 2:Carolla, or 3:Prius"))
    if choiceofcar != number:
        print("Choose 1, 2, or 3 please")
    if number == 1 or "Camry":
        print("Camry has 5 letters in the name")
    elif number == 2 or "Carolla":
        print("The Carolla comes in a multitude of colors.  Some of which you don't like")
    elif number == 3 or "Prius":
        print("The hybrid Prius is actually a good vehicle to get.")


"""This is the main program for the Ford and Toyota car functions I wrote.
What I hope to do is write a main program to where I can import
those files and use the functions in them to run the main program"""

print("Hello user.I haven't met you before.")
name = input("What is your name?")
print("Hi {} We are going to be making a couple of choices today-BIG choices".format(name))
print("We are going to be car shopping today!  Isn't that fun?")
print("First choice is manufacturer.")
choose = input("The list of manufacturers are 1: Toyota, or 2: Ford.  Choose please")
if choose == "Toyota":
    toyota()
elif choose == "Ford":
    ford()
