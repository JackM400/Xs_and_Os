# TODO
#  Generate Board ,
#  display ,
#  start up ,
#  handler ,
#  scan board ,
#  no-winner check ,
#  change player


GameBoard = [" _ ", " _ ", " _ ",
             " _ ", " _ ", " _ ",
             " _ ", " _ ", " _ "]
gameHasNext = True
player1 = ""
player2 = ""
gameWinner = "no winner"
turnPlayer = "X"


def playerName():
    print("Player 1 input name:")
    global player1
    player1 = input()
    print("Player 2 input name:")
    global player2
    player2 = input()
    return player1, player2


def DisplayBoard():
    # print(GameBoard)
    print(GameBoard[0] + "| " + GameBoard[1] + "| " + GameBoard[2])
    print(GameBoard[3] + "| " + GameBoard[4] + "| " + GameBoard[5])
    print(GameBoard[6] + "| " + GameBoard[7] + "| " + GameBoard[8])

    print('Player 1: ' + player1 + " is X")
    print('Player 2: ' + player2 + " is O")


def GameOverCheck():
    winCheck()
    tieCheck()


def rowChecks():
    global gameHasNext
    row_1 = GameBoard[0] == GameBoard[1] == GameBoard[2] != "-"
    row_2 = GameBoard[3] == GameBoard[4] == GameBoard[5] != "-"
    row_3 = GameBoard[6] == GameBoard[7] == GameBoard[8] != "-"
    if row_1 or row_2 or row_3:
        gameHasNext = False
    elif row_1:
        return GameBoard[0]
    elif row_2:
        return GameBoard[3]
    elif row_3:
        return GameBoard[6]
    return


def columnChecks():
    global gameHasNext
    col_1 = GameBoard[0] == GameBoard[3] == GameBoard[6] != "-"
    col_2 = GameBoard[1] == GameBoard[4] == GameBoard[7] != "-"
    col_3 = GameBoard[2] == GameBoard[5] == GameBoard[8] != "-"
    if col_1 or col_2 or col_3:
        gameHasNext = False
    elif col_1:
        return GameBoard[0]
    elif col_2:
        return GameBoard[1]
    elif col_3:
        return GameBoard[2]
    return


def diagonalChecks():
    global gameHasNext
    dia_1 = GameBoard[0] == GameBoard[4] == GameBoard[8] != "-"
    dia_2 = GameBoard[2] == GameBoard[4] == GameBoard[6] != "-"
    if dia_1 or dia_2:
        gameHasNext = False
    elif dia_1:
        return GameBoard[0]
    elif dia_2:
        return GameBoard[1]
    return


def winCheck():
    global gameWinner
    rowwinner = rowChecks
    colwinner = columnChecks
    diawinner = diagonalChecks
    if rowwinner or colwinner or diawinner:
        # winner this turn
        # TODO winner assign
    else:
        # no winner this turn
        gameWinner = None
    return


def tieCheck():
    global gameHasNext
    if "-" not in GameBoard:
        gameHasNext = False
    return


def changePlayer():
    global turnPlayer
    if turnPlayer == "X":
        turnPlayer = "O"
    else:
        turnPlayer = "X"
    return


def turnHandler(player):
    print("Input position [1 - 9]")
    position = input()
    position = int(position) - 1
    GameBoard[position] = player


def gameEnd():
    print("Game Over.")
    if tieCheck():
        print("Tie " + gameWinner)
    elif gameWinner == "X" or gameWinner == "O":
        print("winner is " + gameWinner)


def playGame():
    playerName()
    DisplayBoard()
    while gameHasNext:
        turnHandler()
        GameOverCheck()
        changePlayer()
    gameEnd()


playGame()
