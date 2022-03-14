import numpy as np
import TTT_agent_01
import TTT_functions
import TTT_agent_02

Board = np.array([["1","2","3"],
                  ["4","5","6"],
                  ["7","8","9"]])

def play_human():
    '''starts game of tic-tac-toe
    '''
    symbol1 = "X"
    symbol2 = "O"

    while True:
            TTT_functions.move(symbol1, symbol2, Board)
            if TTT_functions.win(symbol1, Board) == 1:
                print(symbol1 + " won!!")
                break
            elif TTT_functions.draw(Board, symbol1, symbol2) == 1:
                print("draw!!")
                break

            TTT_functions.move(symbol2, symbol1, Board)
            if TTT_functions.win(symbol2, Board) == 1:
                print(symbol2 + " won!!")
                break
            elif TTT_functions.draw(Board, symbol1, symbol2) == 1:
                print("draw!!")
                break
    return

def play_robot_easy():

    ask = input("Choose a symbol(X/O)\nX starts and O playes second")

    if ask == "X":
        symbol_p = "X"
        symbol_r = "O"
        print("human starts!!")
        TTT_agent_01.plr_human_first(symbol_p, symbol_r, Board)
    elif ask == "O":
        symbol_p = "O"
        symbol_r = "X"
        print("robot starts!!")
        TTT_agent_01.plr_robot_first(symbol_p, symbol_r, Board)
    else:
        print("wrong choice")

def play_robot_hard():

    ask = input("Choose a symbol(X/O)\nX starts and O playes second")

    if ask == "X":
        symbol_p = "X"
        symbol_r = "O"
        print("human starts!!")
        TTT_agent_02.plr2_human_first(symbol_p, symbol_r, Board)
    elif ask == "O":
        symbol_p = "O"
        symbol_r = "X"
        print("robot starts!!")
        TTT_agent_02.plr_robot_first(symbol_p, symbol_r, Board)
    else:
        print("wrong choice")

#var  = input("Do you want to play Tic-Tac-Toe?(y/n)")
#start = [var]

start = []
start.append(input("Do you want to play Tic-Tac-Toe?(y/n)"))

while start[0] == "y":
    questinon = input("Do you want to play human or robot?(h/r)")
    if questinon == "h":
        print("X starts")
        TTT_functions.view(Board)
        play_human()
    elif questinon == "r":
        questinon = input("Do you want to play easy or  hard robot?(e/h)")
        if questinon == "e":
            TTT_functions.view(Board)
            play_robot_easy()
        elif questinon == "h":
            TTT_functions.view(Board)
            play_robot_hard()
    else: print("wrong choice")
    start[0] = input("Do you want to play another game of Tic-Tac-Toe?(y/n)")
    while start[0] != "y" and start[0] != "n":
        print("wrong choice")
        start[0] = input("CHANGE YOUR ANSWER!(y/n)\n(Question: Do you want to play another game of Tic-Tac-Toe?(y/n))")
print("Ok, goodbye")
