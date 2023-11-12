import random
import math


# FUNCTIONS
# Product the random number
def start_game(lower, upper):
    print(f"\n\t*************** I CHOOSE A NUMBER BETWEEN {lower} TO {upper} GUESS THAT NUMBER *********************")
    return random.randint(lower, upper)


# Take the lower and upper number from user
def get_upper_lower():
    while True:
        try:
            lower = int(input('\tEnter Lower bound : '))
            upper = int(input('\tEnter Upper bound : '))
            if lower < 0 or upper < 0:
                print('\n\tInvalid input: please enter a POSITIVE INTEGER\n')
                continue
            elif lower > upper:
                print('\n\tAttention: your lower is greater than your upper PLEASE TRY AGAIN...\n')
                continue
            elif lower == upper:
                print('\n\tAre you kidding me? the upper and lower can not be the same PLEASE ENTER DIFFERENT '
                      'NUMBERS...\n')
                continue
        except ValueError:
            print('\n\tInvalid input: please enter a POSITIVE INTEGER\n')
        else:
            chance_guess = round(math.log(upper - lower + 1, 2))
            return lower, upper, chance_guess


# Declare failure
def lose():
    print('\n\tUnfortunately you could not guess the number. Better Luck Next Time!')


# Welcome and run the game
print('\n\tWELCOME TO NUMBER GUESSING GAME PLEASE ENTER LOWER AND UPPER BOUNDS\n')
confirmed_lower, confirmed_upper, chance = get_upper_lower()

# Show user chance for guess
print(f"\n\tYou've only {chance} chances to guess the integer!\n")

random_number = start_game(confirmed_lower, confirmed_upper)
# Number of user attempts
attempts = 0

while chance > 0:
    guess = input("\n\tYour guess : ")
    if not guess.isdigit():
        print('\tWrong input : please try again ')
        continue
    elif random_number == int(guess):
        print(
            f'\t***************************************\n\tCongratulations ... {random_number} is correct\n '
            f'\tNumber of attempts: {attempts+1}\n'
            f'\t***************************************')
        break
    elif random_number < int(guess):
        print(f"\tSMALLER than {guess} ...")
        attempts += 1
        chance -= 1
        if chance == 0:
            lose()
        continue
    elif random_number > int(guess):
        print(f"\tGREATER than {guess}...")
        attempts += 1
        chance -= 1
        if chance == 0:
            lose()
        continue
input('')
