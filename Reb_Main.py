from Reb_Methods import RebMethods
import collections
import copy


print ("""
                |>>>                                                      |>>>
                |                     |>>>          |>>>                  |
                *                     |             |                     *
               / \                    *             *                    / \.
              /___\                 _/ \           / \_                 /___\.
              [   ]                |/   \_________/   \|                [   ]
              [ I ]                /     \       /     \                [ I ]
              [   ]_ _ _          /       \     /       \          _ _ _[   ]
              [   ] U U |        {#########}   {#########}        | U U [   ]
              [   ]====/          \=======/     \=======/          \====[   ]
              [   ]    |           |   I |_ _ _ _| I   |           |    [   ]
              [___]    |_ _ _ _ _ _|     | U U U |     |_ _ _ _ _ _|    [___]
              \===/  I | U U U U U |     |=======|     | U U U U U | I  \===/
               \=/     |===========| I   | + W + |   I |===========|     \=/
                |  I   |           |     |_______|     |           |   I  |
                |      |           |     |||||||||     |           |      |
                |      |           |   I ||vvvvv|| I   |           |      |
    _-_-_-_-_-_-|______|-----------|_____||     ||_____|-----------|______|-_-_-_-_-_-
               /________\         /______||     ||______\         /________\_
    ----------|__________|-------|________\_____/________|-------|__________|---------""")

print ()
print (" ----------------------------------- R E B E L L I O N ----------------------------------")
print (" |                                                                                      |")
print (" |                                                                                      |")
print (" |               Rebellion is a variation of chess with two opposing teams:             |")
print (" |                                                                                      |")
print (" |                  Team 1 : Nobles (1 King and 2 Queens)                               |")
print (" |                  Team 2 : Rebels (2 Rooks, 2 Bishops, and 2 Knights)                 |")
print (" |                                                                                      |")
print (" |                                                                                      |")
print (" ----------------------------------------------------------------------------------------")
print ()

# ------------- important variables ------------

boardObj = RebMethods(0)                        # creating RebMethod object to access its functions

noble_selected = False                          # nobles selected boolean
rebel_selected = False                          # rebels selected boolean
team_selected = 0                               # stores selected team
opposing_team = 0                               # stores opposing team number
starting_board = []                             # starting board, orientation depends on team selected
boards_deque = collections.deque()              # deque containing the boards
check_counter = 0

# booleans
winner_found = False

# team selection
while (True):
    try:
        team_selected = int(input("Pick a team. Enter 1 for Nobles and 2 for Rebels: "))
    except:
        print("Invalid choice. Enter 1 or 2.")
        continue
    else:
        if ((team_selected < 1) or (team_selected > 2)):
            print("Invalid choice. Enter 1 or 2.")
            continue
        else:
            break

print ()
if (team_selected == 1):
    opposing_team = 2
    noble_selected = True
    starting_board = copy.deepcopy(boardObj.start_board_nobles())
    boards_deque.append(starting_board)
    print (" --------------------------------------------------------------------------")
    print ("|                You play as the Nobles. The game begins!                  |")
    print (" --------------------------------------------------------------------------")
    print ()
elif (team_selected == 2):
    opposing_team = 1
    rebel_selected = True
    starting_board = copy.deepcopy(boardObj.start_board_rebels())
    boards_deque.append(starting_board)
    print (" --------------------------------------------------------------------------")
    print ("|                 You play as the Rebels. The game begins!                 |")
    print (" --------------------------------------------------------------------------")
    print ()


# making the starting board into the current board
current_player_board = copy.deepcopy(starting_board)


# The game begins and the human player always starts first
while (winner_found == False):

    if team_selected == 1:
        # human player's turn
        if boardObj.check(current_player_board) == True:
            check_counter += 1
            print("===========================")
            print("|   The king is checked   |")
            print("===========================")
        else:
            check_counter = 0

        current_player_board = copy.deepcopy(boardObj.process_player_move(current_player_board, team_selected))

        if boardObj.check(current_player_board) == True:
            check_counter += 1
            print("===========================")
            print("|   The king is checked   |")
            print("===========================")
        else:
            check_counter = 0

        if boardObj.checkMate(current_player_board) == True or check_counter > 0:
            winner_found = True
            print("==============================")
            print("|   Checkmate. Rebels win!   |")
            print("==============================")
            break
        if boardObj.rebels_lost(current_player_board) == True:
            winner_found = True
            print("==========================================")
            print("|   All rebels eliminated. Nobles win!   |")
            print("==========================================")
            break


        #computer player's turn

        current_player_board = copy.deepcopy(boardObj.alpha_beta_search(current_player_board, opposing_team))

        if boardObj.rebels_lost(current_player_board) == True:
            winner_found = True
            print("==========================================")
            print("|   All rebels eliminated. Nobles win!   |")
            print("==========================================")
            break


    elif team_selected == 2:

        # human player's turn

        current_player_board = copy.deepcopy(boardObj.process_player_move(current_player_board, team_selected))

        if boardObj.rebels_lost(current_player_board) == True:
            winner_found = True
            print("==========================================")
            print("|   All rebels eliminated. Nobles win!   |")
            print("==========================================")
            break

        # computer player's turn
        if boardObj.check(current_player_board) == True:
            check_counter += 1
            print("=========================")
            print("|  The king is checked  |")
            print("=========================")
        else:
            check_counter = 0

        current_player_board = copy.deepcopy(boardObj.alpha_beta_search(current_player_board, opposing_team))

        if boardObj.check(current_player_board) == True:
            check_counter += 1
            print("===========================")
            print("|   The king is checked   |")
            print("===========================")
        else:
            check_counter = 0

        if boardObj.checkMate(current_player_board) == True or check_counter > 0:
            winner_found = True
            print("==============================")
            print("|   Checkmate. Rebels win!   |")
            print("==============================")
            break
        if boardObj.rebels_lost(current_player_board) == True:
            winner_found = True
            print("==========================================")
            print("|   All rebels eliminated. Nobles win!   |")
            print("==========================================")
            break


