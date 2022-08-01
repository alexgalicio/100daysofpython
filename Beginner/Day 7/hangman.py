import random
import hangman_words
import hangman_art

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(f"{' '.join(display)}")

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guess {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print('You lose.')
            print(f'The word is {chosen_word}')
            break

    if '_' not in display:
        end_of_game = True
        print('You win.')
