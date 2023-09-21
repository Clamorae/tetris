import random as rand
import copy

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
                gameBoard[j][i] = ' '

                if j+2 == len(gameBoard) or lockBoard[j+2][i] == "@":
                    stuck = True

    return gameBoard,stuck

def spawnTetromino(gameBoard, tetromino):
    next = tetromino[3]#[rand.randint(0,6)]
    print(next.up)

    for i in range(0,4):
        for j in range(0,4):
            if gameBoard[j][i+3] == "@":
                print('game over')
            else:
                gameBoard[j][i+3] = next.up.item(j,i)
                print(next.up.item(j,i))
    
    return gameBoard

def right(gBoard,lBoard):

    save = copy.deepcopy(gBoard)

    for i in range(len(gBoard[0])-1,0,-1):
        for j in range(0,len(gBoard)):
            if gBoard[j][i] == "@" and lBoard[j][i]!= "@" :
                try:
                    gBoard[j][i+1] = "@"
                    gBoard[j][i] = ' '
                except:
                    return save

    return gBoard

def left(gBoard,lBoard):

    save = copy.deepcopy(gBoard)

    for i in range(0,len(gBoard[0])):
        for j in range(0,len(gBoard)):
            if gBoard[j][i] == "@" and lBoard[j][i]!= "@" :
                if i-1 >= 0:
                    gBoard[j][i-1] = "@"
                    gBoard[j][i] = ' '
                else:
                    return save

    return gBoard

def check_line(gBoard):
    to_remove = []
    for i in range(len(gBoard)):
        full = True
        for cell in gBoard[i]:
            if cell != "@":
                full = False
                break
        if full == True:
            to_remove.append(i)
    
    return removeLine(gBoard,to_remove)

def removeLine(gBoard,to_remove):
    
    bufferBoard = copy.deepcopy(gBoard)
    for value in to_remove:
        bufferBoard.remove(gBoard[value])
        bufferBoard = [[' ']*10] + bufferBoard

    return bufferBoard
    
