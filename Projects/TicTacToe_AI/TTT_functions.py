import numpy as np

def view(Board):
    print("-------------------\n|  "
    + "   |     |     |     \n|  "
    + Board[0][0] + "  |  " + Board[0][1] + "  |  " + Board[0][2] +
    "  |\n|     |     |     |  " +
    "\n|-----|-----|-----|\n|  "
    + "   |     |     |     \n|  "
    + Board[1][0] + "  |  " + Board[1][1] + "  |  " + Board[1][2] +
    "  |\n|     |     |     |  " +
    "\n|-----|-----|-----|\n|  "
    + "   |     |     |     \n|  "
    + Board[2][0] + "  |  " + Board[2][1] + "  |  " + Board[2][2] +
    "  |\n|     |     |     " +
    "|\n-------------------")

def move(symbol, symbol2, Board):
    '''adds symbol to Board and prits current view
    symbol ... string
    len(symbol1) == len(symbol2)
    '''
    list_Board = []
    for row in Board:
        for column in row:
            list_Board.append(column)

    place = input("place "+ symbol + " (number(0-9))")
    #checks input for ilegal characters
    while True:
           if place in list_Board and place != symbol and place != symbol2:
               break
           else:
              print("illegal move")
              place = input("place "+ symbol + " (number(0-9))")

    for row in range(len(Board)):
        for column in range(len(Board[row])):
            if Board[row][column] == place:
                Board[row, column] = symbol

    view(Board)

def win(symbol, Board):
    global Win
    Win = 0

    for row in Board:
        if np.array_equal(row, [symbol, symbol, symbol]):
            Win += 1
    for column in range(len(Board[0])):
        if np.array_equal(Board[:, column], [symbol, symbol, symbol]):
            Win += 1
    if np.array_equal(Board.diagonal(), [symbol, symbol, symbol]):
        Win += 1
    if np.array_equal(np.fliplr(Board).diagonal(), [symbol, symbol, symbol]):
        Win += 1

    return Win


def draw(Board,symbol1, symbol2):
    global Draw
    Draw = 0
    count = 0
    list_Board = []
    for row in Board:
        for column in row:
            if column != symbol1 and column != symbol2:
                list_Board.append((int(column)))

    # if "_" not in list_Board:
    #     Draw = 1

    for x in range(1,10):
        if x not in list_Board:
            count += 1
    if count == 9:
        Draw = 1

    return Draw
