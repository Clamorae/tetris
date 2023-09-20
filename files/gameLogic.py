import random as rand

def createGB():
    gameBoard = [[' ']*10 for x in range(0,20)]
    lockBoard = [[' ']*10 for x in range(0,20)]
    return gameBoard,lockBoard

def frame(gameBoard,lockBoard):
    stuck = False
    
    for i in range(len(gameBoard[0])-1,-1,-1):
        for j in range(len(gameBoard)-1,-1,-1):
            if gameBoard[j][i] == "@" and lockBoard[j][i]!= "@":
                gameBoard[j+1][i] = "@"
                print(j)
                gameBoard[j][i] = ' '

                if j+2 == len(gameBoard) or lockBoard[j+2][i] == "@":
                    stuck = True

    return gameBoard,stuck

def spawnTetromino(gameBoard, tetromino):
    next = tetromino[rand.randint(0,6)]
    print(next.up)

    for i in range(0,4):
        for j in range(0,4):
            if gameBoard[j][i+3] == "@":
                print('game over')
            else:
                gameBoard[j][i+3] = next.up.item(j,i)
                print(next.up.item(j,i))
    
    return gameBoard
