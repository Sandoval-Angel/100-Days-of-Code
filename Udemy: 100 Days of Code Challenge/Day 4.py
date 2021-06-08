from random import randint
from time import sleep

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_choices = [rock, paper, scissors]


def initiate_game():
    play_choice = input("\nEnter (S) to start a new game or (Q) to quit: ").lower()

    if play_choice == 's':
        rps_game()
    elif play_choice == 'q':
        print('\nThanks for playing! The game will now quit.')
        sleep(3)
        exit()
    else:
        print("\nERROR: Invalid entry! Only 'S' and 'Q' are recognized.")
        initiate_game()


def rps_game():
    cpu_choice = randint(0, 2)

    while True:
        try:
            choice_int = int(input('\nWhich do you pick? Enter 0 for Rock, 1 for Paper, or 2 for Scissors: '))
            if choice_int < 0 or choice_int > 2:
                raise ValueError
        except ValueError:
            print('\nInvalid Entry: Entry not a number between 0 and 2.')
        else:
            break

    if choice_int == 0:
        print('\nYou picked:\n' + rps_choices[0] +
              '\nComputer picked:')
        if cpu_choice == 0:
            print(rps_choices[0] + '\nDraw!')
        elif cpu_choice == 1:
            print(rps_choices[1] + '\nYou lose!')
        else:
            print(rps_choices[2] + '\nYou win!')

    if choice_int == 1:
        print('\nYou picked:\n' + rps_choices[1] +
              '\nComputer picked:')
        if cpu_choice == 1:
            print(rps_choices[1] + '\nDraw!')
        elif cpu_choice == 2:
            print(rps_choices[2] + '\nYou lose!')
        else:
            print(rps_choices[0] + '\nYou win!')

    if choice_int == 2:
        print('\nYou picked:\n' + rps_choices[2] +
              '\nComputer picked:')
        if cpu_choice == 2:
            print(rps_choices[2] + '\nDraw!')
        elif cpu_choice == 0:
            print(rps_choices[0] + '\nYou lose!')
        else:
            print(rps_choices[1] + '\nYou win!')

    initiate_game()


initiate_game()
