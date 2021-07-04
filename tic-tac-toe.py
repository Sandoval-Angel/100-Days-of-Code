from os import system, name

used_choices = []
p1_used_choices = []
p2_used_choices = []
curr_turn = 1
game_over = False
choice_map = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def generate_board():
    print(f'''
     {choice_map[7]} | {choice_map[8]} | {choice_map[9]}
    ---+---+---
     {choice_map[4]} | {choice_map[5]} | {choice_map[6]}
    ---+---+---
     {choice_map[1]} | {choice_map[2]} | {choice_map[3]}
    ''')


def p1_turn():
    while True:
        try:
            p1_choice = int(input('Player 1 - Enter choice between 1-9: '))
            if p1_choice in range(1, 10) and p1_choice not in used_choices:
                p1_used_choices.append(p1_choice)
                used_choices.append(p1_choice)
                return p1_choice
            else:
                print('Invalid choice - not in 1-9 range or already picked!')
        except ValueError:
            print('Input not an integer!')


def p2_turn():
    while True:
        try:
            p2_choice = int(input('Player 2 - Enter choice between 1-9: '))
            if p2_choice in range(1, 10) and p2_choice not in used_choices:
                p2_used_choices.append(p2_choice)
                used_choices.append(p2_choice)
                return p2_choice
            else:
                print('Invalid choice - not in 1-9 range or already picked!')
        except ValueError:
            print('Input not an integer!')


def check_game_over():
    global game_over

    p1_win = (7 in p1_used_choices and 8 in p1_used_choices and 9 in p1_used_choices) or\
             (4 in p1_used_choices and 5 in p1_used_choices and 6 in p1_used_choices) or\
             (1 in p1_used_choices and 2 in p1_used_choices and 3 in p1_used_choices) or\
             (7 in p1_used_choices and 4 in p1_used_choices and 1 in p1_used_choices) or\
             (8 in p1_used_choices and 5 in p1_used_choices and 2 in p1_used_choices) or\
             (9 in p1_used_choices and 6 in p1_used_choices and 3 in p1_used_choices) or\
             (7 in p1_used_choices and 5 in p1_used_choices and 3 in p1_used_choices) or\
             (9 in p1_used_choices and 5 in p1_used_choices and 1 in p1_used_choices)
    
    p2_win = (7 in p2_used_choices and 8 in p2_used_choices and 9 in p2_used_choices) or\
             (4 in p2_used_choices and 5 in p2_used_choices and 6 in p2_used_choices) or\
             (1 in p2_used_choices and 2 in p2_used_choices and 3 in p2_used_choices) or\
             (7 in p2_used_choices and 4 in p2_used_choices and 1 in p2_used_choices) or\
             (8 in p2_used_choices and 5 in p2_used_choices and 2 in p2_used_choices) or\
             (9 in p2_used_choices and 6 in p2_used_choices and 3 in p2_used_choices) or\
             (7 in p2_used_choices and 5 in p2_used_choices and 3 in p2_used_choices) or\
             (9 in p2_used_choices and 5 in p2_used_choices and 1 in p2_used_choices)

    if p1_win:
        game_over = True
        print('Player 1 wins!')
    elif p2_win:
        game_over = True
        print('Player 2 wins!')
    elif len(used_choices) == 9:
        game_over = True
        print('No more moves available - draw!')


def tic_tac_toe():
    global curr_turn

    clear()
    generate_board()

    while not game_over:
        if curr_turn == 1:
            choice_map[p1_turn()] = 'x'
            curr_turn += 1
        else:
            choice_map[p2_turn()] = 'o'
            curr_turn -= 1

        clear()

        generate_board()
        check_game_over()


tic_tac_toe()
