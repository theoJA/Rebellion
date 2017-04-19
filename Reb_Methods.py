import copy
import collections

class RebMethods(object):


    def __init__(self, id):
        self.id = id
        #self.board_action = []


    # ------ Initiating board --------
    def start_board_nobles(self):
        self.start_chess_board = []
        for i in range(7):
            if (i == 6):
                # store a list at the 6th index for tracking heuristic values, parent, etc
                self.start_chess_board.append([0])
            else :
                self.start_chess_board.append(["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"])
        self.start_chess_board[5][1] = "[Q]"
        self.start_chess_board[5][2] = "[K]"
        self.start_chess_board[5][4] = "[Q]"
        self.start_chess_board[0][0] = "[R]"
        self.start_chess_board[0][1] = "[B]"
        self.start_chess_board[0][2] = "[N]"
        self.start_chess_board[0][3] = "[N]"
        self.start_chess_board[0][4] = "[B]"
        self.start_chess_board[0][5] = "[R]"

        return self.start_chess_board

    def start_board_rebels(self):
        self.start_chess_board = []
        for i in range(7):
            if (i == 6):
                # store a list at the 6th index for tracking heuristic values, parent, etc
                self.start_chess_board.append([0])
            else :
                self.start_chess_board.append(["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"])
        self.start_chess_board[0][1] = "[Q]"
        self.start_chess_board[0][2] = "[K]"
        self.start_chess_board[0][4] = "[Q]"
        self.start_chess_board[5][0] = "[R]"
        self.start_chess_board[5][1] = "[B]"
        self.start_chess_board[5][2] = "[N]"
        self.start_chess_board[5][3] = "[N]"
        self.start_chess_board[5][4] = "[B]"
        self.start_chess_board[5][5] = "[R]"

        return self.start_chess_board


    # ------ Printing board(s) function(s) -------
    def print_board(self, board):
        self.print_counter = 0
        print (" ".join(["   0 ", "1 ", "2 ", "3 ", "4 ", "5 "]))
        for row in range(6):
            print (str(self.print_counter) + " " + "".join(board[row]))
            self.print_counter += 1
        print ()

    def print_boards(self, boards):
        for board in boards:
            self.print_board(board)


    # ------- Processes the human player's move using the move validators -------
    def process_player_move(self, board, team):
        self.curr_board = copy.deepcopy(board)
        print("____________________\n")
        print ("   Current board    \n")
        self.print_board(self.curr_board)
        print("____________________\n")
        if (team == 1):
            print ("Pick a Noble piece.")
        elif (team == 2):
            print ("Pick a Rebel piece.")

        # selecting row and col for piece
        while (True):
            while (True):
                try:
                    self.piece_row = int(input("Piece row: "))
                except:
                    print ("You must enter an integer.")
                    continue
                else:
                    break

            while (True):
                try:
                    self.piece_col = int(input("Piece col: "))
                except:
                    print("You must enter an integer.")
                    continue
                else:
                    break

            # Making sure row and col are within bounds
            if ((self.piece_row > 5 or self.piece_row < 0) or (self.piece_col > 5 or self.piece_col < 0)):
                print("Row or col out of bounds! Pick a new row and col.")
            # Making sure the right pieces are selected
            if ((self.piece_row <= 5 and self.piece_row >= 0) and (self.piece_col <= 5 and self.piece_col >= 0)):
                if (board[self.piece_row][self.piece_col] == "[ ]"):
                    print ("No pieces there! Pick a new row and col.")
                else:
                    if (team == 1):
                        if ((board[self.piece_row][self.piece_col] == "[R]") or (board[self.piece_row][self.piece_col] == "[B]") or (board[self.piece_row][self.piece_col] == "[N]")):
                            print("Cannot select opponent's piece! Pick a new row and col.")
                        else:
                            break
                    elif (team == 2):
                        if ((board[self.piece_row][self.piece_col] == "[Q]") or (board[self.piece_row][self.piece_col] == "[K]")):
                            print("Cannot select opponent's piece! Pick a new row and col.")
                        else:
                            break

        # move the selected piece
        print("\nNow select row and col to move to.")
        while (True):
            while (True):
                try:
                    self.move_row = int(input("Move row: "))
                except:
                    print ("You must enter an integer.")
                    continue
                else:
                    break

            while (True):
                try:
                    self.move_col = int(input("Move col: "))
                except:
                    print ("You must enter an integer.")
                    continue
                else:
                    break

            # Making sure row and col are within bounds
            if ((self.move_row > 5 or self.move_row < 0) or (self.move_col > 5 or self.move_col < 0)):
                print("Row or col out of bounds! Pick a new row and col.")
            # Row and col are within bounds now making sure moves are valid
            if ((self.move_row <= 5 and self.move_row >= 0) and (self.move_col <= 5 and self.move_col >= 0)):
                if (team == 1):
                    if ((self.curr_board[self.move_row][self.move_col] == "[Q]") or (self.curr_board[self.move_row][self.move_col] == "[K]")):
                        print ("Invalid move! That tile has one of your pieces on it.")
                    else:
                        if (((self.curr_board[self.piece_row][self.piece_col] == "[Q]") and ((self.queen_valid_move(self.curr_board,self.piece_row,self.piece_col,self.move_row,self.move_col) == True)))
                            or ((self.curr_board[self.piece_row][self.piece_col] == "[K]") and (self.king_valid_move(self.curr_board,self.piece_row,self.piece_col,self.move_row,self.move_col) == True))):
                            break
                        else:
                            print("Invalid move! Pick a new row and col.")
                elif (team == 2):
                    if ((self.curr_board[self.move_row][self.move_col] == "[R]") or (self.curr_board[self.move_row][self.move_col] == "[B]") or (self.curr_board[self.move_row][self.move_col] == "[N]")):
                        print ("Invalid move! That tile has one of your pieces on it.")
                    else:
                        if (((self.curr_board[self.piece_row][self.piece_col] == "[R]") and (self.rook_valid_move(self.curr_board,self.piece_row,self.piece_col,self.move_row,self.move_col) == True))
                            or ((self.curr_board[self.piece_row][self.piece_col] == "[B]") and (self.bishop_valid_move(self.curr_board,self.piece_row,self.piece_col,self.move_row,self.move_col) == True))
                            or ((self.curr_board[self.piece_row][self.piece_col] == "[N]") and (self.knight_valid_move(self.curr_board,self.piece_row,self.piece_col,self.move_row,self.move_col) == True))):
                            break
                        else:
                            print("Invalid move! Pick a new row and col.")

        self.curr_board[self.move_row][self.move_col] = self.curr_board[self.piece_row][self.piece_col]
        self.curr_board[self.piece_row][self.piece_col] = "[ ]"
        #self.move_coordinates = [self.piece_row,self.piece_col,self.move_row,self.move_col]
        print ()
        return self.curr_board


    # ------ Move validators -------
    def rook_valid_move(self, board, piece_row, piece_col, move_row, move_col):
        if (move_row == piece_row):
            if (move_col == piece_col):
                return False
            else:
                if (move_col < piece_col):
                    for i in range(move_col + 1, piece_col):
                        if (board[move_row][i] != "[ ]" ):
                            return False
                    else:
                        return True
                else:
                    for i in range(piece_col + 1, move_col):
                        if (board[move_row][i] != "[ ]" ):
                            return False
                    else:
                        return True
        else:
            if (move_col == piece_col):
                if (move_row < piece_row):
                    for i in range(move_row + 1, piece_row):
                        if (board[i][move_col] != "[ ]" ):
                            return False
                    else:
                        return True
                else:
                    for i in range(piece_row + 1, move_row):
                        if (board[i][move_col] != "[ ]" ):
                            return False
                    else:
                        return True
            else:
                return False

    def bishop_valid_move(self, board, piece_row, piece_col, move_row, move_col):
        if (move_row == piece_row):
            return False
        else:
            if ((move_row == piece_row - 1) or (move_row == piece_row + 1)):
                if ((move_col == piece_col - 1) or (move_col == piece_col + 1)):
                    return True
                else:
                    return False
            elif ((move_row == piece_row - 2) or (move_row == piece_row + 2)):
                if ((move_col == piece_col - 2) or (move_col == piece_col + 2)):
                    if (move_row < piece_row) and (move_col < piece_col):
                        if (board[piece_row - 1][piece_col - 1] == "[ ]"):
                            return True
                    elif (move_row > piece_row) and (move_col < piece_col):
                        if (board[piece_row + 1][piece_col - 1] == "[ ]"):
                            return True
                    elif (move_row < piece_row) and (move_col > piece_col):
                        if (board[piece_row - 1][piece_col + 1] == "[ ]"):
                            return True
                    elif (move_row > piece_row) and (move_col > piece_col):
                        if (board[piece_row + 1][piece_col + 1] == "[ ]"):
                            return True
                    else:
                        return False
                else:
                    return False
            elif ((move_row == piece_row - 3) or (move_row == piece_row + 3)):
                if ((move_col == piece_col - 3) or (move_col == piece_col + 3)):
                    for i in range(1,3):
                        if (move_row < piece_row) and (move_col < piece_col):
                            if (board[piece_row - i][piece_col - i] != "[ ]"):
                                return False
                        elif (move_row > piece_row) and (move_col < piece_col):
                            if (board[piece_row + i][piece_col - i] != "[ ]"):
                                return False
                        elif (move_row < piece_row) and (move_col > piece_col):
                            if (board[piece_row - i][piece_col + i] != "[ ]"):
                                return False
                        elif (move_row > piece_row) and (move_col > piece_col):
                            if (board[piece_row + i][piece_col + i] != "[ ]"):
                                return False
                    else:
                        return True
                else:
                    return False
            elif ((move_row == piece_row - 4) or (move_row == piece_row + 4)):
                if ((move_col == piece_col - 4) or (move_col == piece_col + 4)):
                    for i in range(1,4):
                        if (move_row < piece_row) and (move_col < piece_col):
                            if (board[piece_row - i][piece_col - i] != "[ ]"):
                                return False
                        elif (move_row > piece_row) and (move_col < piece_col):
                            if (board[piece_row + i][piece_col - i] != "[ ]"):
                                return False
                        elif (move_row < piece_row) and (move_col > piece_col):
                            if (board[piece_row - i][piece_col + i] != "[ ]"):
                                return False
                        elif (move_row > piece_row) and (move_col > piece_col):
                            if (board[piece_row + i][piece_col + i] != "[ ]"):
                                return False
                    else:
                        return True
                else:
                    return False
            elif ((move_row == piece_row - 5) or (move_row == piece_row + 5)):
                if ((move_col == piece_col - 5) or (move_col == piece_col + 5)):
                    for i in range(1,5):
                        if (move_row < piece_row) and (move_col < piece_col):
                            if (board[piece_row - i][piece_col - i] != "[ ]"):
                                return False
                        elif (move_row > piece_row) and (move_col < piece_col):
                            if (board[piece_row + i][piece_col - i] != "[ ]"):
                                return False
                        elif (move_row < piece_row) and (move_col > piece_col):
                            if (board[piece_row - i][piece_col + i] != "[ ]"):
                                return False
                        elif (move_row > piece_row) and (move_col > piece_col):
                            if (board[piece_row + i][piece_col + i] != "[ ]"):
                                return False
                    else:
                        return True
                else:
                    return False

    def knight_valid_move(self, board, piece_row, piece_col, move_row, move_col):
        if (move_row == piece_row):
            return False
        else:
            if ((move_row == piece_row - 1) or (move_row == piece_row + 1)):
                if ((move_col == piece_col - 2) or (move_col == piece_col + 2)):
                    return True
                else:
                    return False
            elif ((move_row == piece_row - 2) or (move_row == piece_row + 2)):
                if ((move_col == piece_col - 1) or (move_col == piece_col + 1)):
                    return True
                else:
                    return False

    def queen_valid_move(self, board, piece_row, piece_col, move_row, move_col):
        if (move_row == piece_row):
            if (move_col == piece_col):
                return False
            else:
                if (move_col < piece_col):
                    for i in range(move_col + 1, piece_col):
                        if (board[move_row][i] != "[ ]" ):
                            return False
                    else:
                        return True
                else:
                    for i in range(piece_col + 1, move_col):
                        if (board[move_row][i] != "[ ]" ):
                            return False
                    else:
                        return True
        else:
            if (move_col == piece_col):
                if (move_row < piece_row):
                    for i in range(move_row + 1, piece_row):
                        if (board[i][move_col] != "[ ]" ):
                            return False
                    else:
                        return True
                else:
                    for i in range(piece_row + 1, move_row):
                        if (board[i][move_col] != "[ ]" ):
                            return False
                    else:
                        return True
            else:
                if ((move_row == piece_row - 1) or (move_row == piece_row + 1)):
                    if ((move_col == piece_col - 1) or (move_col == piece_col + 1)):
                        return True
                    else:
                        return False
                elif ((move_row == piece_row - 2) or (move_row == piece_row + 2)):
                    if ((move_col == piece_col - 2) or (move_col == piece_col + 2)):
                        if (move_row < piece_row) and (move_col < piece_col):
                            if (board[piece_row - 1][piece_col - 1] == "[ ]"):
                                return True
                        elif (move_row > piece_row) and (move_col < piece_col):
                            if (board[piece_row + 1][piece_col - 1] == "[ ]"):
                                return True
                        elif (move_row < piece_row) and (move_col > piece_col):
                            if (board[piece_row - 1][piece_col + 1] == "[ ]"):
                                return True
                        elif (move_row > piece_row) and (move_col > piece_col):
                            if (board[piece_row + 1][piece_col + 1] == "[ ]"):
                                return True
                        else:
                            return False
                    else:
                        return False
                elif ((move_row == piece_row - 3) or (move_row == piece_row + 3)):
                    if ((move_col == piece_col - 3) or (move_col == piece_col + 3)):
                        for i in range(1, 3):
                            if (move_row < piece_row) and (move_col < piece_col):
                                if (board[piece_row - i][piece_col - i] != "[ ]"):
                                    return False
                            elif (move_row > piece_row) and (move_col < piece_col):
                                if (board[piece_row + i][piece_col - i] != "[ ]"):
                                    return False
                            elif (move_row < piece_row) and (move_col > piece_col):
                                if (board[piece_row - i][piece_col + i] != "[ ]"):
                                    return False
                            elif (move_row > piece_row) and (move_col > piece_col):
                                if (board[piece_row + i][piece_col + i] != "[ ]"):
                                    return False
                        else:
                            return True
                    else:
                        return False
                elif ((move_row == piece_row - 4) or (move_row == piece_row + 4)):
                    if ((move_col == piece_col - 4) or (move_col == piece_col + 4)):
                        for i in range(1, 4):
                            if (move_row < piece_row) and (move_col < piece_col):
                                if (board[piece_row - i][piece_col - i] != "[ ]"):
                                    return False
                            elif (move_row > piece_row) and (move_col < piece_col):
                                if (board[piece_row + i][piece_col - i] != "[ ]"):
                                    return False
                            elif (move_row < piece_row) and (move_col > piece_col):
                                if (board[piece_row - i][piece_col + i] != "[ ]"):
                                    return False
                            elif (move_row > piece_row) and (move_col > piece_col):
                                if (board[piece_row + i][piece_col + i] != "[ ]"):
                                    return False
                        else:
                            return True
                    else:
                        return False
                elif ((move_row == piece_row - 5) or (move_row == piece_row + 5)):
                    if ((move_col == piece_col - 5) or (move_col == piece_col + 5)):
                        for i in range(1, 5):
                            if (move_row < piece_row) and (move_col < piece_col):
                                if (board[piece_row - i][piece_col - i] != "[ ]"):
                                    return False
                            elif (move_row > piece_row) and (move_col < piece_col):
                                if (board[piece_row + i][piece_col - i] != "[ ]"):
                                    return False
                            elif (move_row < piece_row) and (move_col > piece_col):
                                if (board[piece_row - i][piece_col + i] != "[ ]"):
                                    return False
                            elif (move_row > piece_row) and (move_col > piece_col):
                                if (board[piece_row + i][piece_col + i] != "[ ]"):
                                    return False
                        else:
                            return True
                    else:
                        return False

    def king_valid_move(self, board, piece_row, piece_col, move_row, move_col):
        if (move_row == piece_row):
            if (move_col == piece_col):
                return False
            else:
                if ((move_col == piece_col - 1) or (move_col == piece_col + 1)):
                    return True
                else:
                    return False
        else:
            if (move_col == piece_col):
                if ((move_row == piece_row - 1) or (move_row == piece_row + 1)):
                    return True
                else:
                    return False
            else:
                if ((move_row == piece_row - 1) or (move_row == piece_row + 1)):
                    if ((move_col == piece_col - 1) or (move_col == piece_col + 1)):
                        return True
                    else:
                        return False



    # -------- Heuristics ------------
    def eval_function(self, board, team):
        self.heu_board = copy.deepcopy(board)
        self.heu_team = team
        self.heu_val = (self.material_adv(self.heu_board,self.heu_team)) + \
                       (self.space_adv(self.heu_board,self.heu_team)) + \
                       (self.kingAndQueen_position(self.heu_board,self.heu_team))
        return self.heu_val

    # Material Advantage
    def material_adv(self, board, team):
        self.value = 0
        for row in range(0,6):
            for tile in range(0,6):
                if (team == 1):
                    if (board[row][tile] == "[Q]"):
                        self.value += 2
                    elif (board[row][tile] == "[K]"):
                        self.value += 2
                elif (team == 2):
                    if (board[row][tile] == "[B]") or (board[row][tile] == "[N]"):
                        self.value += 1
                    elif (board[row][tile] == "[R]"):
                        self.value += 1
        return self.value


    # Space Advantage
    def space_adv(self, board, team):
        self.value = 0
        self.row_adv = 0
        self.col_adv = 0
        for row in range(0,6):
            if (row == 0) or (row == 5):
                self.row_adv = 1
            elif (row == 1) or (row == 4):
                self.row_adv = 2
            elif (row == 2) or (row == 3):
                self.row_adv = 3
            for tile in range(0,6):
                if (tile == 0) or (tile == 5):
                    self.col_adv = 1
                elif (tile == 1) or (tile == 4):
                    self.col_adv = 2
                elif (tile == 2) or (tile == 3):
                    self.col_adv = 3
                if (team == 1):
                    if (board[row][tile] == "[Q]") or (board[row][tile] == "[K]"):
                        self.value += (1 + self.row_adv + self.col_adv)*2
                elif (team == 2):
                    if (board[row][tile] == "[R]") or (board[row][tile] == "[B]") or (board[row][tile] == "[N]"):
                        self.value += (1 + self.row_adv + self.col_adv)
        return self.value


    # King and Queens' position relative to the Rooks, Bishops and Knights -- very messy and inelegant -- will be fixed in future iterations
    def kingAndQueen_position(self, board, team):
        self.board = board
        self.value = 0
        for row in range(6):
            for col in range(6):
                if (board[row][col] == "[K]") or (board[row][col] == "[Q]"):
                    if team == 1:

                        # relative to bishop - upper left
                        for i in range(1,6):
                            if (row - i >= 0) and (col - i >= 0):
                                if (board[row - i][col - i] == "[R]") or (board[row - i][col - i] =="[N]"):
                                    self.value += 2
                                    break
                                elif board[row - i][col - i] == "[ ]":
                                    self.value += 0
                                elif board[row - i][col - i] == "[B]":
                                    if board[row][col] == "[K]":
                                        self.value += -2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += -2
                                        break
                        # relative to bishop - upper right
                        for i in range(1, 6):
                            if (row - i >= 0) and (col + i <= 5):
                                if (board[row - i][col + i] == "[R]") or (board[row - i][col + i] == "[N]"):
                                    self.value += 2
                                    break
                                elif board[row - i][col + i] == "[ ]":
                                    self.value += 0
                                elif board[row - i][col + i] == "[B]":
                                    if board[row][col] == "[K]":
                                        self.value += -2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += -2
                                        break
                        # relative to bishop - lower left
                        for i in range(1, 6):
                            if (row + i <= 5) and (col - i >= 0):
                                if (board[row + i][col - i] == "[R]") or (board[row + i][col - i] == "[N]"):
                                    self.value += 2
                                    break
                                elif board[row + i][col - i] == "[ ]":
                                    self.value += 0
                                elif board[row + i][col - i] == "[B]":
                                    if board[row][col] == "[K]":
                                        self.value += -2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += -2
                                        break
                        # relative to bishop - lower right
                        for i in range(1, 6):
                            if (row + i <= 5) and (col + i <= 5):
                                if (board[row + i][col + i] == "[R]") or (board[row + i][col + i] == "[N]"):
                                    self.value += 2
                                    break
                                elif board[row + i][col + i] == "[ ]":
                                    self.value += 0
                                elif board[row + i][col + i] == "[B]":
                                    if board[row][col] == "[K]":
                                        self.value += -2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += -2
                                        break


                        # relative to rook - top
                        for i in range(1,6):
                            if (row - i >= 0):
                                if (board[row - i][col] == "[B]") or (board[row - i][col] == "[N]"):
                                    self.value += 2
                                    break
                                elif (board[row - i][col] == "[ ]"):
                                    self.value += 0
                                elif (board[row - i][col] == "[R]"):
                                    if board[row][col] == "[K]":
                                        self.value += -2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += -2
                                        break
                        # relative to rook - left
                        for i in range(1, 6):
                            if (col - i >= 0):
                                if (board[row][col - i] == "[B]") or (board[row][col - i] == "[N]"):
                                    self.value += 2
                                    break
                                elif (board[row][col - i] == "[ ]"):
                                    self.value += 0
                                elif (board[row][col - i] == "[R]"):
                                    if board[row][col] == "[K]":
                                        self.value += -2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += -2
                                        break
                        # relative to rook - right
                        for i in range(1, 6):
                            if (col + i <= 5):
                                if (board[row][col + i] == "[B]") or (board[row][col + i] == "[N]"):
                                    self.value += 2
                                    break
                                elif (board[row][col + i] == "[ ]"):
                                    self.value += 0
                                elif (board[row][col + i] == "[R]"):
                                    if board[row][col] == "[K]":
                                        self.value += -2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += -2
                                        break
                        # relative to rook - bottom
                        for i in range(1, 6):
                            if (row + i <= 5):
                                if (board[row + i][col] == "[B]") or (board[row + i][col] == "[N]"):
                                    self.value += 2
                                    break
                                elif (board[row + i][col] == "[ ]"):
                                    self.value += 0
                                elif (board[row + i][col] == "[R]"):
                                    if board[row][col] == "[K]":
                                        self.value += -2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += -2
                                        break


                        # relative to knight - top
                        if (row - 2 >= 0):
                            if col - 1 >= 0 and (board[row - 2][col - 1] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += -2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += -2
                                    break
                            if col + 1 <= 5 and (board[row - 2][col + 1] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += -2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += -2
                                    break
                    # relative to knight - bottom
                        if (row + 2 <= 5):
                            if col - 1 >= 0 and (board[row + 2][col - 1] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += -2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += -2
                                    break
                            if col + 1 <= 5 and (board[row + 2][col + 1] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += -2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += -2
                                    break
                                self.value += -2
                        # relative to knight - left
                        if (col - 2 >= 0):
                            if row - 1 >= 0 and (board[row - 1][col - 2] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += -2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += -2
                                    break
                            if row + 1 <= 5 and (board[row + 1][col - 2] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += -2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += -2
                                    break
                    # relative to knight - right
                        if (col + 2 <= 5):
                            if row - 1 >= 0 and (board[row - 1][col + 2] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += -2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += -2
                                    break
                            if row + 1 <= 5 and (board[row + 1][col + 2] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += -2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += -2
                                    break

                    elif team == 2:

                        # relative to bishop - upper left
                        for i in range(1, 6):
                            if (row - i >= 0) and (col - i >= 0):
                                if (board[row - i][col - i] == "[R]") or (board[row - i][col - i] == "[N]"):
                                    self.value += -2
                                    break
                                elif board[row - i][col - i] == "[ ]":
                                    self.value += 0
                                elif board[row - i][col - i] == "[B]":
                                    if board[row][col] == "[K]":
                                        self.value += 2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += 2
                                        break
                        # relative to bishop - upper right
                        for i in range(1, 6):
                            if (row - i >= 0) and (col + i <= 5):
                                if (board[row - i][col + i] == "[R]") or (board[row - i][col + i] == "[N]"):
                                    self.value += -2
                                    break
                                elif board[row - i][col + i] == "[ ]":
                                    self.value += 0
                                elif board[row - i][col + i] == "[B]":
                                    if board[row][col] == "[K]":
                                        self.value += 2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += 2
                                        break
                        # relative to bishop - lower left
                        for i in range(1, 6):
                            if (row + i <= 5) and (col - i >= 0):
                                if (board[row + i][col - i] == "[R]") or (board[row + i][col - i] == "[N]"):
                                    self.value += -2
                                    break
                                elif board[row + i][col - i] == "[ ]":
                                    self.value += 0
                                elif board[row + i][col - i] == "[B]":
                                    if board[row][col] == "[K]":
                                        self.value += 2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += 2
                                        break
                        # relative to bishop - lower right
                        for i in range(1, 6):
                            if (row + i <= 5) and (col + i <= 5):
                                if (board[row + i][col + i] == "[R]") or (board[row + i][col + i] == "[N]"):
                                    self.value += -2
                                    break
                                elif board[row + i][col + i] == "[ ]":
                                    self.value += 0
                                elif board[row + i][col + i] == "[B]":
                                    if board[row][col] == "[K]":
                                        self.value += 2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += 2
                                        break


                        # relative to rook - top
                        for i in range(1, 6):
                            if (row - i >= 0):
                                if (board[row - i][col] == "[B]") or (board[row - i][col] == "[N]"):
                                    self.value += -2
                                    break
                                elif (board[row - i][col] == "[ ]"):
                                    self.value += 0
                                elif (board[row - i][col] == "[R]"):
                                    if board[row][col] == "[K]":
                                        self.value += 2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += 2
                                        break
                        # relative to rook - left
                        for i in range(1, 6):
                            if (col - i >= 0):
                                if (board[row][col - i] == "[B]") or (board[row][col - i] == "[N]"):
                                    self.value += -2
                                    break
                                elif (board[row][col - i] == "[ ]"):
                                    self.value += 0
                                elif (board[row][col - i] == "[R]"):
                                    if board[row][col] == "[K]":
                                        self.value += 2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += 2
                                        break
                        # relative to rook - right
                        for i in range(1, 6):
                            if (col + i <= 5):
                                if (board[row][col + i] == "[B]") or (board[row][col + i] == "[N]"):
                                    self.value += -2
                                    break
                                elif (board[row][col + i] == "[ ]"):
                                    self.value += 0
                                elif (board[row][col + i] == "[R]"):
                                    if board[row][col] == "[K]":
                                        self.value += 2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += 2
                                        break
                        # relative to rook - bottom
                        for i in range(1, 6):
                            if (row + i <= 5):
                                if (board[row + i][col] == "[B]") or (board[row + i][col] == "[N]"):
                                    self.value += -2
                                    break
                                elif (board[row + i][col] == "[ ]"):
                                    self.value += 0
                                elif (board[row + i][col] == "[R]"):
                                    if board[row][col] == "[K]":
                                        self.value += 2
                                        break
                                    elif board[row][col] == "[Q]":
                                        self.value += 2
                                        break


                        # relative to knight - top
                        if (row - 2 >= 0):
                            if col - 1 >= 0 and (board[row - 2][col - 1] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += 2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += 2
                                    break
                            if col + 1 <= 5 and (board[row - 2][col + 1] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += 2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += 2
                                    break
                    # relative to knight - bottom
                        if (row + 2 <= 5):
                            if col - 1 >= 0 and (board[row + 2][col - 1] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += 2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += 2
                                    break
                            if col + 1 <= 5 and (board[row + 2][col + 1] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += 2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += 2
                                    break
                    # relative to knight - left
                        if (col - 2 >= 0):
                            if row - 1 >= 0 and (board[row - 1][col - 2] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += 2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += 2
                                    break
                            if row + 1 <= 5 and (board[row + 1][col - 2] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += 2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += 2
                                    break
                    # relative to knight - right
                        if (col + 2 <= 5):
                            if row - 1 >= 0 and (board[row - 1][col + 2] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += 2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += 2
                                    break
                            if row + 1 <= 5 and (board[row + 1][col + 2] == "[N]"):
                                if board[row][col] == "[K]":
                                    self.value += 2
                                    break
                                elif board[row][col] == "[Q]":
                                    self.value += 2
                                    break

        return self.value



    # ----------- Check and Checkmate ------------ Rebels Win Condition ------------
    def check(self, board):
        self.board = copy.deepcopy(board)
        for row in range(6):
            for col in range(6):
                if board[row][col] == "[K]":

                    # relative to bishop - upper left
                    for i in range(1, 6):
                        if (row - i >= 0) and (col - i >= 0) and board[row - i][col - i] == "[B]" and self.bishop_valid_move(self.board, row - i, col - i, row, col) == True:
                            return True
                    # relative to bishop - upper right
                    for i in range(1, 6):
                        if (row - i >= 0) and (col + i <= 5) and board[row - i][col + i] == "[B]" and self.bishop_valid_move(self.board, row - i, col + i, row, col) == True:
                            return True
                    # relative to bishop - lower left
                    for i in range(1, 6):
                        if (row + i <= 5) and (col - i >= 0) and board[row + i][col - i] == "[B]" and self.bishop_valid_move(self.board, row + i, col - i, row, col) == True:
                            return True
                    # relative to bishop - lower right
                    for i in range(1, 6):
                        if (row + i <= 5) and (col + i <= 5) and board[row + i][col + i] == "[B]" and self.bishop_valid_move(self.board, row + i, col + i, row, col) == True:
                            return True


                    # relative to rook - top
                    for i in range(1, 6):
                        if (row - i >= 0) and (board[row - i][col] == "[R]") and self.rook_valid_move(self.board, row - i, col, row, col) == True:
                            return True
                    # relative to rook - left
                    for i in range(1, 6):
                        if (col - i >= 0) and (board[row][col - i] == "[R]") and self.rook_valid_move(self.board, row, col - i, row, col) == True:
                            return True
                    # relative to rook - right
                    for i in range(1, 6):
                        if (col + i <= 5) and (board[row][col + i] == "[R]") and self.rook_valid_move(self.board, row, col + i, row, col) == True:
                            return True
                    # relative to rook - bottom
                    for i in range(1, 6):
                        if (row + i <= 5) and (board[row + i][col] == "[R]") and self.rook_valid_move(self.board, row + i, col, row, col) == True:
                            return True


                    # relative to knight - top
                    if (row - 2 >= 0):
                        if col - 1 >= 0 and (board[row - 2][col - 1] == "[N]") and self.knight_valid_move(self.board, row - 2, col - 1, row, col) == True:
                            return True
                        if col + 1 <= 5 and (board[row - 2][col + 1] == "[N]") and self.knight_valid_move(self.board, row - 2, col + 1, row, col) == True:
                            return True
                    # relative to knight - bottom
                    if (row + 2 <= 5):
                        if col - 1 >= 0 and (board[row + 2][col - 1] == "[N]") and self.knight_valid_move(self.board, row + 2, col - 1, row, col) == True:
                            return True
                        if col + 1 <= 5 and (board[row + 2][col + 1] == "[N]") and self.knight_valid_move(self.board, row + 2, col + 1, row, col) == True:
                            return True
                    # relative to knight - left
                    if (col - 2 >= 0):
                        if row - 1 >= 0 and (board[row - 1][col - 2] == "[N]") and self.knight_valid_move(self.board, row - 1, col - 2, row, col) == True:
                            return True
                        if row + 1 <= 5 and (board[row + 1][col - 2] == "[N]") and self.knight_valid_move(self.board, row + 1, col - 2, row, col) == True:
                            return True
                    # relative to knight - right
                    if (col + 2 <= 5):
                        if row - 1 >= 0 and (board[row - 1][col + 2] == "[N]") and self.knight_valid_move(self.board, row - 1, col + 2, row, col) == True:
                            return True
                        if row + 1 <= 5 and (board[row + 1][col + 2] == "[N]") and self.knight_valid_move(self.board, row + 1, col + 2, row, col) == True:
                            return True
        else:
            return False


    def checkMate(self, board):
        self.kings_deg_freedom = 0
        #self.board = copy.deepcopy(board)
        self.temp_board = copy.deepcopy(board)

        for row in range(6):
            for col in range(6):
                if self.temp_board[row][col] == "[K]":

                        if row - 1 >= 0:
                            # up

                            if self.temp_board[row - 1][col] == "[ ]" or self.temp_board[row - 1][col] == "[R]" or self.temp_board[row - 1][col] == "[B]" or self.temp_board[row - 1][col] == "[N]":
                                self.temp_board[row - 1][col] = self.temp_board[row][col]
                                self.temp_board[row][col] = "[ ]"
                                if self.check(self.temp_board) == False:
                                    self.kings_deg_freedom += 1
                                self.temp_board = copy.deepcopy(board)

                        if row + 1 <= 5:
                            # down

                            if self.temp_board[row + 1][col] == "[ ]" or self.temp_board[row + 1][col] == "[R]" or self.temp_board[row + 1][col] == "[B]" or self.temp_board[row + 1][col] == "[N]":
                                self.temp_board[row + 1][col] = self.temp_board[row][col]
                                self.temp_board[row][col] = "[ ]"
                                if self.check(self.temp_board) == False:
                                    self.kings_deg_freedom += 1
                                self.temp_board = copy.deepcopy(board)

                        if col - 1 >= 0:
                            # left

                            if self.temp_board[row][col - 1] == "[ ]" or self.temp_board[row][col - 1] == "[R]" or self.temp_board[row][col - 1] == "[B]" or self.temp_board[row][col - 1] == "[N]":
                                self.temp_board[row][col - 1] = self.temp_board[row][col]
                                self.temp_board[row][col] = "[ ]"
                                if self.check(self.temp_board) == False:
                                    self.kings_deg_freedom += 1
                                self.temp_board = copy.deepcopy(board)

                        if col + 1 <= 5:
                            # right

                            if self.temp_board[row][col + 1] == "[ ]" or self.temp_board[row][col + 1] == "[R]" or self.temp_board[row][col + 1] == "[B]" or self.temp_board[row][col + 1] == "[N]":
                                self.temp_board[row][col + 1] = self.temp_board[row][col]
                                self.temp_board[row][col] = "[ ]"
                                if self.check(self.temp_board) == False:
                                    self.kings_deg_freedom += 1
                                self.temp_board = copy.deepcopy(board)

                        if row - 1 >= 0 and col - 1 >= 0:
                            # upper left

                            if self.temp_board[row - 1][col - 1] == "[ ]" or self.temp_board[row - 1][col - 1] == "[R]" or self.temp_board[row - 1][col - 1] == "[B]" or self.temp_board[row - 1][col - 1] == "[N]":
                                self.temp_board[row - 1][col - 1] = self.temp_board[row][col]
                                self.temp_board[row][col] = "[ ]"
                                if self.check(self.temp_board) == False:
                                    self.kings_deg_freedom += 1
                                self.temp_board = copy.deepcopy(board)

                        if row - 1 >= 0 and col + 1 <= 5:
                            # upper right

                            if self.temp_board[row - 1][col + 1] == "[ ]" or self.temp_board[row - 1][col + 1] == "[R]" or self.temp_board[row - 1][col + 1] == "[B]" or self.temp_board[row - 1][col + 1] == "[N]":
                                self.temp_board[row - 1][col + 1] = self.temp_board[row][col]
                                self.temp_board[row][col] = "[ ]"
                                if self.check(self.temp_board) == False:
                                    self.kings_deg_freedom += 1
                                self.temp_board = copy.deepcopy(board)

                        if row + 1 <= 5 and col - 1 >= 0:
                            # lower left

                            if self.temp_board[row + 1][col - 1] == "[ ]" or self.temp_board[row + 1][col - 1] == "[R]" or self.temp_board[row + 1][col - 1] == "[B]" or self.temp_board[row + 1][col - 1] == "[N]":
                                self.temp_board[row + 1][col - 1] = self.temp_board[row][col]
                                self.temp_board[row][col] = "[ ]"
                                if self.check(self.temp_board) == False:
                                    self.kings_deg_freedom += 1
                                self.temp_board = copy.deepcopy(board)

                        if row + 1 <= 5 and col + 1 <= 5:
                            # lower right

                            if self.temp_board[row + 1][col + 1] == "[ ]" or self.temp_board[row + 1][col + 1] == "[R]" or self.temp_board[row + 1][col + 1] == "[B]" or self.temp_board[row + 1][col + 1] == "[N]":
                                self.temp_board[row + 1][col + 1] = self.temp_board[row][col]
                                self.temp_board[row][col] = "[ ]"
                                if self.check(self.temp_board) == False:
                                    self.kings_deg_freedom += 1
                                self.temp_board = copy.deepcopy(board)

        if self.kings_deg_freedom > 0:
            return False
        elif self.kings_deg_freedom == 0:
            return True



    # ------------ No More Rebels ---------------- Nobles Win Condition --------------
    def rebels_lost(self, board):
        self.rebel_num = 0
        for row in range(0,6):
            for col in range(0,6):
                if (board[row][col] == "[R]") or (board[row][col] == "[B]") or (board[row][col] == "[N]"):
                    self.rebel_num += 1
        if self.rebel_num > 0:
            return False
        elif self.rebel_num == 0:
            return True



    # ------------ Generating children for computer player's current board --------------
    def generate_comp_moves(self, board, team):
        self.comp_deque = collections.deque()
        self.board = copy.deepcopy(board)
        #print (self.board[0])
        #self.print_board(self.board)
        if team == 1:
            for row in range(6):
                for col in range(6):
                    if self.board[row][col] == "[Q]":

                        for move_row in range(6):
                            for move_col in range(6):
                                if self.board[move_row][move_col] != "[Q]" and  self.board[move_row][move_col] != "[K]" and self.queen_valid_move(self.board, row, col, move_row, move_col) == True:
                                    self.board[move_row][move_col] = self.board[row][col]
                                    self.board[row][col] = "[ ]"
                                    self.comp_deque.extend([self.board])
                                    self.board = copy.deepcopy(board)

                    if self.board[row][col] == "[K]":
                        for move_row in range(6):
                            for move_col in range(6):
                                if self.board[move_row][move_col] != "[Q]" and  self.board[move_row][move_col] != "[K]" and self.king_valid_move(self.board, row, col, move_row, move_col) == True:
                                    self.board[move_row][move_col] = self.board[row][col]
                                    self.board[row][col] = "[ ]"
                                    self.comp_deque.extend([self.board])
                                    self.board = copy.deepcopy(board)

        elif team == 2:
            for row in range(6):
                for col in range(6):

                    if self.board[row][col] == "[R]":
                        for move_row in range(6):
                            for move_col in range(6):
                                if self.board[move_row][move_col] != "[R]" and  self.board[move_row][move_col] != "[B]" and self.board[move_row][move_col] != "[N]" and self.rook_valid_move(self.board, row, col, move_row, move_col) == True:
                                    self.board[move_row][move_col] = self.board[row][col]
                                    self.board[row][col] = "[ ]"
                                    self.comp_deque.extend([self.board])
                                    self.board = copy.deepcopy(board)

                    if self.board[row][col] == "[B]":
                        for move_row in range(6):
                            for move_col in range(6):
                                if self.board[move_row][move_col] != "[R]" and  self.board[move_row][move_col] != "[B]" and self.board[move_row][move_col] != "[N]" and self.bishop_valid_move(self.board, row, col, move_row, move_col) == True:
                                    self.board[move_row][move_col] = self.board[row][col]
                                    self.board[row][col] = "[ ]"
                                    self.comp_deque.extend([self.board])
                                    self.board = copy.deepcopy(board)

                    if self.board[row][col] == "[N]":
                        for move_row in range(6):
                            for move_col in range(6):
                                if self.board[move_row][move_col] != "[R]" and  self.board[move_row][move_col] != "[B]" and self.board[move_row][move_col] != "[N]" and self.knight_valid_move(self.board, row, col, move_row, move_col) == True:
                                    self.board[move_row][move_col] = self.board[row][col]
                                    self.board[row][col] = "[ ]"
                                    self.comp_deque.extend([self.board])
                                    self.board = copy.deepcopy(board)

        return self.comp_deque



    # ----------- MiniMax with alpha-beta pruning ----------------
    def alpha_beta_search(self, board, team):
        print(".......................")
        print(" ~ Enemy made a move ~ ")
        print(".......................\n\n")
        self.team = team
        self.board = copy.deepcopy(board)
        self.board_action = copy.deepcopy(board)
        self.value = self.max_value(4, self.board, -1000, 1000, team)
        self.action_value = -1000

        for child in self.generate_comp_moves(self.board_action, self.team):
            # if child == self.board:
            #     continue
            #else:
            child[6][0] = self.eval_function(child, self.team)
            self.action_value = max(child[6][0],self.action_value)
            if self.action_value == child[6][0]:
                self.board_action = copy.deepcopy(child)
        return self.board_action


    def max_value(self, depth, board, alpha, beta, team):
        #print ("Calculating")
        self.board = copy.deepcopy(board)
        self.alpha = alpha
        self.beta = beta
        if depth == 0:
            board[6][0] = self.eval_function(board, team)
            return self.eval_function(board, team)

        self.value = -100000

        if (team == 1):
            self.team = 2
        elif (team == 2):
            self.team = 1

        for child in self.generate_comp_moves(board, team):
            self.value = max(self.value, self.min_value(depth - 1, child, self.alpha, self.beta, self.team))
            if self.value >= self.beta:
                return self.value
            self.alpha = max(self.alpha, self.value)
        return self.value


    def min_value(self, depth, board, alpha, beta, team):
        #print("Calculating")
        self.board = copy.deepcopy(board)
        self.alpha = alpha
        self.beta = beta
        if depth == 0:
            board[6][0] = self.eval_function(board, team)
            return self.eval_function(board, team)

        self.value = 100000

        if (team == 1):
            self.team = 2
        elif (team == 2):
            self.team = 1

        for child in self.generate_comp_moves(board, team):
            self.value = min(self.value, self.max_value(depth - 1, child, self.alpha, self.beta, self.team))
            if self.value <= self.alpha:
                return self.value
            self.beta = min(self.beta, self.value)
        return self.value

