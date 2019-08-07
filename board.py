# JackM400
# jack.millar400@gmail.com


# holds game board state
GameBoard = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]
gameHasNext = True
player1 = ""
player2 = ""
gameWinner = None
turnPlayer = "X"


# main function
def playGame():
    getPlayerName()
    playerDeclaration()  # print players
    DisplayBoard()
    # loop until game end state reached
    while gameHasNext:
        turnHandler(turnPlayer)
        GameOverCheck()
        changePlayer()
    gameEnd()


def getPlayerName():
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
    # checks across table for same character
    row_1 = GameBoard[0] == GameBoard[1] == GameBoard[2] != "_"
    row_2 = GameBoard[3] == GameBoard[4] == GameBoard[5] != "_"
    row_3 = GameBoard[6] == GameBoard[7] == GameBoard[8] != "_"
    # return winner
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
    # checks down table for same character
    col_1 = GameBoard[0] == GameBoard[3] == GameBoard[6] != "_"
    col_2 = GameBoard[1] == GameBoard[4] == GameBoard[7] != "_"
    col_3 = GameBoard[2] == GameBoard[5] == GameBoard[8] != "_"
    # return winner
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
    # checks across table for same character
    dia_1 = GameBoard[0] == GameBoard[4] == GameBoard[8] != "_"
    dia_2 = GameBoard[2] == GameBoard[4] == GameBoard[6] != "_"
    # return winner
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
    # get winner
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
    # if all slots used , no win possible
    if "_" not in GameBoard:
        gameHasNext = False
        return True
    # no tie
    else:
        return False


def changePlayer():
    global turnPlayer
    if turnPlayer == "X":
        turnPlayer = "O"
    else:
        turnPlayer = "X"
    return


# change player
def turnHandler(player):
    isValid = False

    # get initial input
    print("current turn : " + player)
    print("Input position [1 - 9]")
    position = input()

    while not isValid:
        # check if valid move
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid move: Not a move")
            print("Input position [1 - 9]")
            position = input()

        position = int(position) - 1
        # check if position taken
        if GameBoard[position] == "_":
            isValid = True
        else:
            print("Invalid move: Taken position")
    # insert player token into position
    GameBoard[position] = player
    # show updated board
    DisplayBoard()


def gameEnd():
    print("Game Over:")
    if gameWinner == "X" or gameWinner == "O":
        print("Winner is " + gameWinner)
    if tieCheck():
        print("Tie")


# run game
playGame()
