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


def player_choice():
    while True:
        try:
            p_choice = int(input(f'Player {curr_turn} - Enter choice between 1-9: '))
            if p_choice in range(1, 10) and p_choice not in used_choices:
                used_choices.append(p_choice)
                if curr_turn == 1:
                    p1_used_choices.append(p_choice)
                else:
                    p2_used_choices.append(p_choice)

                return p_choice
            else:
                print('Invalid choice - not in 1-9 range or already picked!')
        except ValueError:
            print('Input not an integer!')


def check_game_over():
    global game_over

    if curr_turn == 1:
        curr_player_choices = p1_used_choices
    else:
        curr_player_choices = p2_used_choices

    player_win = (7 in curr_player_choices and 8 in curr_player_choices and 9 in curr_player_choices) or\
                 (4 in curr_player_choices and 5 in curr_player_choices and 6 in curr_player_choices) or\
                 (1 in curr_player_choices and 2 in curr_player_choices and 3 in curr_player_choices) or\
                 (7 in curr_player_choices and 4 in curr_player_choices and 1 in curr_player_choices) or\
                 (8 in curr_player_choices and 5 in curr_player_choices and 2 in curr_player_choices) or\
                 (9 in curr_player_choices and 6 in curr_player_choices and 3 in curr_player_choices) or\
                 (7 in curr_player_choices and 5 in curr_player_choices and 3 in curr_player_choices) or\
                 (9 in curr_player_choices and 5 in curr_player_choices and 1 in curr_player_choices)

    if player_win:
        game_over = True
        print(f'Player {curr_turn} wins!')
    elif len(used_choices) == 9:
        game_over = True
        print('No more moves available - draw!')


def tic_tac_toe():
    global curr_turn

    clear()
    generate_board()

    while not game_over:
        if curr_turn == 1:
            choice_map[player_choice()] = 'x'
            clear()
            generate_board()
            check_game_over()
            curr_turn += 1
        else:
            choice_map[player_choice()] = 'o'
            clear()
            generate_board()
            check_game_over()
            curr_turn -= 1


tic_tac_toe()
