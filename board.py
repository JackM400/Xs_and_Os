# TODO
#  Generate Board ,
#  display ,
#  start up ,
#  handler ,
#  scan board ,
#  no-winner check ,
#  change player


GameBoard = [
    [" _ ", " _ ", " _ "],
    [" _ ", " _ ", " _ "],
    [" _ ", " _ ", " _ "]
]
player1: str = ""
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
    for i in GameBoard:
        print(i)
    print('Player 1: ' + player1 + " is X")
    print('Player 2: ' + player2 + " is O")


def turnHandler():
    print("Input position.\n")
    position = input()


def playGame():
    playerName()
    DisplayBoard()
    turnHandler()


playGame()
