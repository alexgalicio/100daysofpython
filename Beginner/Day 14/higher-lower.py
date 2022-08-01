import random
from game_data import data
from higher_lower_art import logo, vs
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')


def random_account():
    return random.choice(data)


def personalities(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description}, from {country}."


def check_answers(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = random_account()
    account_b = random_account()

    while game_should_continue:
        account_a = account_b
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {personalities(account_a)}")
        print(vs)
        print(f"Against B: {personalities(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answers(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
