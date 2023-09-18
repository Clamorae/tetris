import random as rand

def createGB():
    gameBoard = [[' ']*10 for x in range(0,20)]
    lockBoard = [[' ']*10 for x in range(0,20)]
    return gameBoard,lockBoard

def frame(gameBoard,lockBoard):
    stuck = False
    
    for i in range(len(gameBoard[0])-1,0,-1):
        for j in range(len(gameBoard)-1,0,-1):
            if gameBoard[j][i] == "@" and lockBoard[j][i]!= "@":
                gameBoard[j+1][i] = "@"
                gameBoard[j][i] = ' '

                if j+2 == len(gameBoard) or lockBoard[j+2][i] == "@":
                    stuck = True

    return gameBoard,stuck

