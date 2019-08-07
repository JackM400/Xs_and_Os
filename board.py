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
player1 = ""
player2 = ""


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


def winCheck():
    return


def tieCheck():
    return


def changePlayer():
    return


def turnHandler(player):
    print("Input position [1 - 9]")
    position = input()
    position = int(position) - 1


def playGame():
    playerName()
    DisplayBoard()
    while gameHasNext:
        turnHandler(player)
        GameOverCheck()
        changePlayer()


playGame()
