import random
import hangman_art
import hangman_words
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


word = random.choice(hangman_words.available_words)
word_tracker = ['_'] * len(word)
guessed_letters = []

lives = 6
game_over = False

print(hangman_art.logo)

while not game_over:
    guess = input('\nGuess a letter: ')[0]

    clear()

    if guess in guessed_letters:
        print(f'\nYou have already guessed that!')
        print(hangman_art.stages[lives])
        print(' '.join(word_tracker))
        continue
    else:
        guessed_letters.append(guess)

        if guess not in word:
            lives -= 1
            print('\nIncorrect guess!')
        else:
            for index, letter in enumerate(word):
                if guess == letter:
                    word_tracker[index] = letter

            print('\nGood guess!')

    print(hangman_art.stages[lives])
    print(' '.join(word_tracker))

    if lives == 0:
        print('\nYou lose!')
        game_over = True
    elif '_' not in word_tracker:
        print('\nYou win!')
        game_over = True
