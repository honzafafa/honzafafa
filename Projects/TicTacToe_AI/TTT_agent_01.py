import random
import TTT_functions

def robot_move(symbol1, symbol2, Board):
        '''first version of robot will do just random moves
        '''
        list_Board = []
        for row in Board:
            for column in row:
                if column != symbol1 and column != symbol2:
                    list_Board.append(column)

        move = random.choice(list_Board)

        for row in range(len(Board)):
            for column in range(len(Board[row])):
                if Board[row][column] == move:
                    Board[row, column] = symbol1
        print("Robot-" + symbol1 + " choosed position " + str(move))
        TTT_functions.view(Board)
        return

def plr_human_first(symbol_p, symbol_r, Board):

    while True:
            TTT_functions.move(symbol_p, symbol_r, Board)
            if TTT_functions.win(symbol_p, Board) == 1:
                print(symbol_p + " won!!")
                break
            elif TTT_functions.draw(Board, symbol_p, symbol_r) == 1:
                print("draw!!")
                break

            robot_move(symbol_r, symbol_p, Board)
            if TTT_functions.win(symbol_r, Board) == 1:
                print(symbol_r + " won!!")
                break
            elif TTT_functions.draw(Board, symbol_p, symbol_r) == 1:
                print("draw!!")
                break
    return

def plr_robot_first(symbol_p, symbol_r, Board):

    while True:
            robot_move(symbol_r, symbol_p, Board)
            if TTT_functions.win(symbol_r, Board) == 1:
                print(symbol_r + " won!!")
                break
            elif TTT_functions.draw(Board, symbol_p, symbol_r) == 1:
                print("draw!!")
                break

            TTT_functions.move(symbol_p, symbol_r, Board)
            if TTT_functions.win(symbol_p, Board) == 1:
                print(symbol_p + " won!!")
                break
            elif TTT_functions.draw(Board, symbol_p, symbol_r) == 1:
                print("draw!!")
                break
    return
