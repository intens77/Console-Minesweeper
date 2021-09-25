import sys
from game_field import GameField
import os


def start_game():
    global game_field
    game_parameters = str(input("Please enter the game parameters "
                                "(field size in X, field size in Y,\n"
                                " number of mines). If you want to use the\n"
                                " default settings, just press enter:   "))
    params = process_game_parameters(game_parameters)
    if params is None:
        start_game()
    elif params == "":
        game_field = GameField()
    else:
        game_field = GameField(params['width'], params['height'], params['mines_count'])

    while True:
        display_field_state()
        command = str(input(console_message))
        process_player_command(command)


def process_game_parameters(game_parameters):
    if len(game_parameters) == 0:
        return ""
    else:
        params = game_parameters.strip().split()
        if "".join(params).isdigit() and len(params) == 3:
            params = list(map(int, params))
            if len(params) < 3:
                print("\n\n\nIncorrect game parameters. "
                      "Read the rules and try again!\n")
                return
            else:
                if params[0] * params[1] <= params[2]:
                    print("\n\n\nYou have mined the entire field. "
                          "The game is impossible. try again!\n")
                    return
                return {'width': params[0], 'height': params[1], 'mines_count': params[2]}
        else:
            print("\n\n\nIncorrect game parameters. "
                  "Read the rules and try again!\n")
            return


def process_player_command(command):
    global first_move_flag
    if command.strip() == "restart":
        os.system("clear")
        os.system("python3 main.py")
    elif len(command.strip().split()) == 3:
        x, y, action = command.split()
        if x.isdigit() and y.isdigit():
            x, y = int(x), int(y)
            if x > game_field.width or y > game_field.height:
                change_console_message("Going beyond the boundaries of the field. "
                                       "Read the rules and try again!\n")
            else:
                if action == "flag":
                    change_console_message()
                    game_field.set_flag(x, y)
                    if first_move_flag:
                        game_field.fill_playing_field(x, y)
                        first_move_flag = False
                elif action == "open":
                    change_console_message()
                    game_field.open_cell(x, y)
                    if first_move_flag:
                        game_field.fill_playing_field(x, y)
                        first_move_flag = False
                else:
                    change_console_message("Incorrect command. "
                                           "Read the rules and try again!\n")
        else:
            change_console_message("Incorrect command. "
                                   "Read the rules and try again!\n")
    else:
        change_console_message("Incorrect command. "
                               "Read the rules and try again!\n")


def display_field_state():
    os.system("clear")
    for row_index, row in enumerate(game_field.field):
        # print("{0} | ".format(row_index+1), end=' ')
        for number in row:
            print(str(number) + "   ", end='')
        for _ in range(2):
            print()
    # for column_index in range(game_field.width):
    #     print(" _", end=' ')
    # print()


def change_console_message(new_console_message=
                           "Enter the coordinates of the cell in X and Y:   "):
    globals().update({'console_message': new_console_message})


def restart_game():
    answer = str(input("Do you want to replay? Enter yes or no:   "))
    if answer == "yes":
        os.system("clear")
        os.system("python3 main.py")
        sys.exit()
    elif answer == "no":
        print("Thanks for playing!")
        sys.exit()
    else:
        print("The command was not recognized. Read the rules and try again!")
        sys.exit()


console_message = "Enter the coordinates of the cell in X and Y:   "
first_move_flag = True
