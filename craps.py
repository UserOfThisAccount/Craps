import random


def roll_dice():

    global dice1, dice2
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def game():

    first_roll = roll_dice()

    if first_roll in (7, 11):
        print(f"The sum of dice is: {dice1} + {dice2} = {first_roll}")
        print("You won!")
    elif first_roll in (2, 3, 12):
        print(f"The sum of dice is: {dice1} + {dice2} = {first_roll}")
        print("You lost!")
    else:
        goal = first_roll
        print(f"The sum of dice is: {dice1} + {dice2} = {first_roll}")
        print(f"The goal is now change to {goal}")

        while True:
            next_roll = roll_dice()
            print(f"The sum of dice is: {dice1} + {dice2} = {next_roll}")
            print(f"The goal is now {next_roll}")
            
            if next_roll == goal:
                print("You won!")
                break
            elif next_roll == 7:
                print("You lost!")
                break


game()