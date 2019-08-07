# TODO
#  Generate Board ,
#  display ,
#  start up ,
#  handler ,
#  scan board ,
#  no-winner check ,
#  change player


GameBoard = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]
gameHasNext = True
player1 = ""
player2 = ""
gameWinner = None
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
    print(GameBoard[0] + " | " + GameBoard[1] + " | " + GameBoard[2])
    print(GameBoard[3] + " | " + GameBoard[4] + " | " + GameBoard[5])
    print(GameBoard[6] + " | " + GameBoard[7] + " | " + GameBoard[8])


def playerDeclaration():
    print('Player 1: ' + player1 + " is X")
    print('Player 2: ' + player2 + " is O")


def GameOverCheck():
    winCheck()
    tieCheck()


def rowChecks():
    global gameHasNext
    row_1 = GameBoard[0] == GameBoard[1] == GameBoard[2] != "_"
    row_2 = GameBoard[3] == GameBoard[4] == GameBoard[5] != "_"
    row_3 = GameBoard[6] == GameBoard[7] == GameBoard[8] != "_"
    if row_1 or row_2 or row_3:
        gameHasNext = False
    if row_1:
        return GameBoard[0]
    elif row_2:
        return GameBoard[3]
    elif row_3:
        return GameBoard[6]
    else:
        return None


def columnChecks():
    global gameHasNext
    col_1 = GameBoard[0] == GameBoard[3] == GameBoard[6] != "_"
    col_2 = GameBoard[1] == GameBoard[4] == GameBoard[7] != "_"
    col_3 = GameBoard[2] == GameBoard[5] == GameBoard[8] != "_"
    if col_1 or col_2 or col_3:
        gameHasNext = False
    if col_1:
        return GameBoard[0]
    elif col_2:
        return GameBoard[1]
    elif col_3:
        return GameBoard[2]
    else:
        return None


def diagonalChecks():
    global gameHasNext
    dia_1 = GameBoard[0] == GameBoard[4] == GameBoard[8] != "_"
    dia_2 = GameBoard[2] == GameBoard[4] == GameBoard[6] != "_"
    if dia_1 or dia_2:
        gameHasNext = False
    if dia_1:
        return GameBoard[0]
    elif dia_2:
        return GameBoard[1]
    else:
        return None


def winCheck():
    global gameWinner
    rowwinner = rowChecks()
    colwinner = columnChecks()
    diawinner = diagonalChecks()
    if rowwinner:
        gameWinner = rowwinner
    elif colwinner:
        gameWinner = colwinner
    elif diawinner:
        gameWinner = diawinner
    else:
        gameWinner = None


def tieCheck():
    global gameHasNext
    if "_" not in GameBoard:
        gameHasNext = False
        return True
    else:
        return False


def changePlayer():
    global turnPlayer
    if turnPlayer == "X":
        turnPlayer = "O"
    else:
        turnPlayer = "X"
    return


def turnHandler(player):
    isValid = False

    print("current turn : " + player)
    print("Input position [1 - 9]")
    position = input()

    while not isValid:
        while position != 1 or position != 2 or position != 3 or position != 4 or position != 5 or \
                position != 6 or position != 7 or position != 8 or position != 9:
            print("Invalid move:")
            print("Input position [1 - 9]")
            position = input()
            position = int(position) - 1

            if GameBoard[position] == "_":
                isValid = True
            else:
                print("Invalid move:")

    GameBoard[position] = player
    DisplayBoard()


def gameEnd():
    print("Game Over.")
    if gameWinner == "X" or gameWinner == "O":
        print("winner is " + gameWinner)
    if tieCheck():
        print("Tie")


def playGame():
    playerName()
    playerDeclaration()
    DisplayBoard()
    while gameHasNext:
        turnHandler(turnPlayer)
        GameOverCheck()
        changePlayer()
    gameEnd()


playGame()
