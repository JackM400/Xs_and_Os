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
    gameHasNext = False
    return True


def columnChecks():
    return


def diagonalChecks():
    return


def winCheck():
    global gameWinner
    rowwinner = rowChecks()
    colwinner = columnChecks()
    diawinner = diagonalChecks()
    if rowwinner or colwinner or diawinner:
    # winner this turn
    # TODO winner assign
    elif
    # no winner this turn
    winner = None
    return


def tieCheck():
    return


def changePlayer():
    return


def turnHandler(player):
    print("Input position [1 - 9]")
    position = input()
    position = int(position) - 1


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
