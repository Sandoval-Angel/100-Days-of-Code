from time import sleep

def game_intro():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************

    Welcome to Treasure Island.
    Your mission is to find the treasure.''')


def initiate_game():
    play_choice = input("\nEnter (S) to start a new game or (Q) to quit: ").lower()

    if play_choice == 's':
        crossroads()
    elif play_choice == 'q':
        print('\nThanks for playing! The game will now quit.')
        sleep(3)
        exit()
    else:
        print("\nERROR: Invalid entry! Only 'S' and 'Q' are recognized.")
        initiate_game()


def crossroads():
    road_choice = input('\nYou come to a cross roads. '
                        'Do you choose the (L)eft or (R)ight path? ').lower()

    if road_choice[0] == 'l':
        river()
    elif road_choice[0] == 'r':
        print('\nAs you walk down this road the floor suddenly gives out under you. '
              'You fall into a spike-pit.\n'
              'GAME OVER!')
        initiate_game()
    else:
        print("\nERROR: Invalid entry! Only 'L' and 'R' are recognized.")
        crossroads()


def river():
    river_choice = input('\nThis road ends at the edge of a river. Will you (S)wim across or (W)ait for a boat? ').lower()

    if river_choice[0] == 'w':
        color_doors()
    elif river_choice[0] == 's':
        print('\nHalf-way across the river a strong current drags you under water. You drown.\n'
              'GAME OVER!')
        initiate_game()
    else:
        print("\nERROR: Invalid entry! Only 'S' and 'W' are recognized.")
        river()


def color_doors():
    color_choice = input('\nYou cross the river unharmed. You come across a house with 3 doors of different colors, '
                         '(R)ed, (Y)ellow, and (B)lue. Which color do you choose? ')

    if color_choice[0] == 'r':
        print('\nYou open the red door. Flames spill out the door, burning you.\n'
              'GAME OVER!')
        initiate_game()
    elif color_choice[0] == 'y':
        print('\nYou open the yellow door. Behind it rests a wooden chest full of bitcoin pre-Musk tweet.\n'
        input('\nPress Enter to exit: ')
        exit()
    elif color_choice[0] == 'b':
        print('\nThe door swings open to the sound of snarls and growls. A large beasts rushes at you and bites '
              'down around your neck. You died.\n'
              'GAME OVER!')
        initiate_game()
    else:
        print("\nERROR: Invalid entry! Only 'R', 'Y', and 'W' are recognized.")
        color_doors()


game_intro()
initiate_game()