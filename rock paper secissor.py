import random
from typing import Coroutine
while True:
    choices = ["rock","paper","scissors"]

    comp = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock,paper,scissors?: ").lower()

    print("computer: "+ comp)
    print("Player: "+player)

    if player == comp:
        print("Tie!")

    elif player == "rock":

        if comp == "paper":
            print("You lose :( ")
        else:
            print("You won!")
    elif player == "paper":

        if comp == "scissors":
            print("You lose :( ")
        else:
            print("You won!")

    elif player == "scissors":

        if comp == "rock":
            print("You lose :( ")
        else:
            print("You won!")

    play = input("Play again?   (yes,no): ").lower()

    if play  != "yes" :

        break
print("bye")