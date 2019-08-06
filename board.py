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


def DisplayBoard():
    print(GameBoard)
    for i in GameBoard:
        print(i)


DisplayBoard()
