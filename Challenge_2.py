# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")


# set the initial values
the_number = random.randint(1, 100)
question = 'Take a guess: '
tries = 1
low = 1
high = 101


def ask_number(question, low, high, step = 1):
    guess = None
    while guess not in range(low, high):
        guess = int(input(question))
    return guess

guess = ask_number(question, low, high, step = 1)
# guessing loop
def main(the_number, guess):
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")
        global tries
        tries += 1
        guess = ask_number(question, low, high, step = 1)
main(the_number, guess)
print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
