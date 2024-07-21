from random import randint

game = True

while game:

        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        sum_of_dices = dice1 + dice2

        print(f"The sum of dices is {dice1} + {dice2} = {sum_of_dices}")

        if sum_of_dices == 7:
                print("You won!")
                game = False
        elif sum_of_dices == 2 or sum_of_dices == 3 or sum_of_dices == 12:
                print("The casino wins!")
                game = False
