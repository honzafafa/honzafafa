import TTT_functions
import  numpy as np
import math

def evaluate(Board, robot_symbol, player_symbol,depth):
    if TTT_functions.win(robot_symbol, Board)== 1:
        return 10 - depth
    elif TTT_functions.win(player_symbol, Board) == 1:
        return -10 + depth
    else:
        return 0

def moves_left(Board, symbol1, symbol2):
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            if Board[row][column] != symbol1 and Board[row][column] != symbol2:
                return True
    return False

def minimax(Board, depth, is_max, robot_symbol, player_symbol, alpha, beta):
    score = evaluate(Board, robot_symbol, player_symbol, depth)

    if score > 0:
        return score
    elif score < 0:
        return score
    elif moves_left(Board, robot_symbol, player_symbol) == False:
        return 0


    if is_max:
        best = -1000

        for row in range(len(Board)):
            for column in range(len(Board[row])):
                if Board[row][column] != robot_symbol and Board[row][column] != player_symbol:
                    x = Board[row][column]
                    Board[row][column] = robot_symbol
                    max_move = minimax(Board, depth + 1, not is_max, robot_symbol, player_symbol, alpha, beta)
                    best = max(best, max_move)
                    Board[row][column] = x
                    alpha = max(alpha, best)
                    # Alpha Beta pruning
                    if beta <= alpha:
                        break

        return best

    else:
        best = 1000

        for row in range(len(Board)):
            for column in range(len(Board[row])):
                if Board[row][column] != robot_symbol and Board[row][column] != player_symbol:
                    x = Board[row][column]
                    Board[row][column] = player_symbol
                    max_move = minimax(Board, depth + 1, not is_max, robot_symbol, player_symbol, alpha, beta)
                    best = min(best, max_move)
                    Board[row][column] = x
                    beta = min(beta, best)
                    # Alpha Beta pruning
                    if beta <= alpha:
                        break
        # print(best)
        return best

def best_move(Board, robot_symbol, player_symbol):

    best_value = -10000
    best_move = (-1, -1)

    for row in range(len(Board)):
        for column in range(len(Board[row])):
            if Board[row][column] != robot_symbol and Board[row][column] != player_symbol:
                x = Board[row][column]
                Board[row][column] = robot_symbol
                move_value = minimax(Board, 0, False, robot_symbol, player_symbol, -1000, 1000)
                Board[row][column] = x
                if move_value > best_value:
                    best_move = (row, column)
                    best_value = move_value

    # print("Value of best move = " + str(best_value))
    # print(best_move)
    return(best_move)

def robot_move(Board, robot_symbol, player_symbol):
    move = best_move(Board, robot_symbol, player_symbol)
    for row in range(len(Board)):
        for column in range(len(Board[row])):
            if row == move[0] and column == move[1]:
                Board[row][column] = robot_symbol
    TTT_functions.view(Board)

def plr_robot_first(symbol_p, symbol_r, Board):
    while True:
            robot_move(Board, symbol_r, symbol_p)
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

def plr2_human_first(symbol_p, symbol_r, Board):
    while True:
            TTT_functions.move(symbol_p, symbol_r, Board)
            if TTT_functions.win(symbol_p, Board) == 1:
                print(symbol_p + " won!!")
                break
            elif TTT_functions.draw(Board, symbol_p, symbol_r) == 1:
                print("draw!!")
                break

            robot_move(Board, symbol_r, symbol_p)
            if TTT_functions.win(symbol_r, Board) == 1:
                print(symbol_r + " won!!")
                break
            elif TTT_functions.draw(Board, symbol_p, symbol_r) == 1:
                print("draw!!")
                break

def robot_fight(symbol_p, symbol_r, Board):
    while True:
        robot_move(Board, symbol_r, symbol_p)
        if TTT_functions.win(symbol_r, Board) == 1:
            print(symbol_r + " won!!")
            break
        elif TTT_functions.draw(Board, symbol_p, symbol_r) == 1:
            print("draw!!")
            break

        robot_move(Board, symbol_p, symbol_r)
        if TTT_functions.win(symbol_r, Board) == 1:
            print(symbol_r + " won!!")
            break
        elif TTT_functions.draw(Board, symbol_p, symbol_r) == 1:
            print("draw!!")
            break
