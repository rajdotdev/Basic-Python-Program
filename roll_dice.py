# By Raj Shekhar Aryal
# Simple dice roller in python

import random

def roll_dice():

    dice_drawing = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│ ●       │",
            "│         │",
            "│       ● │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│ ●       │",
            "│    ●    │",
            "│       ● │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│ ●     ● │",
            "│         │",
            "│ ●     ● │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│ ●     ● │",
            "│    ●    │",
            "│ ●     ● │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│ ●     ● │",
            "│ ●     ● │",
            "│ ●     ● │",
            "└─────────┘",
        ),
    }

    roll = input("Do you want to roll the dice ? (Yes / No):")

    if roll.lower() == "no":
        print("\n Thank you for playing")

    while roll.lower() == 'yes':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("You rolled {} and {}".format(dice1,dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Do you want to roll the dice again ? (Yes / No): ")





roll_dice()