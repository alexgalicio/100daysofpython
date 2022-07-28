from random import randint
from guess_the_number_art import logo

EASY = 10
HARD = 5


def difficulty():
    prompt = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if prompt == 'easy':
        return EASY
    else:
        return HARD


def check_number(guess, number, turns):
    if guess > number:
        print("Too high.")
        return turns - 1
    elif guess < number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {number}.")


def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100")
    number = randint(1, 100)

    attempts = difficulty()
    guess = 0

    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        attempts = check_number(guess, number, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number is {number}")
            return
        elif guess != number:
            print("Guess again.")


game()
