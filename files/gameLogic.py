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
    next = tetromino[rand.randint(0,6)]

    for i in range(0,4):
        for j in range(0,4):
            if gameBoard[j][i+3] == "@":
                print('game over')
            else:
                if (next.up[0] == j and next.up[1] == i) or (next.up[2] == j and next.up[3] == i) or (next.up[4] == j and next.up[5] == i) or (next.up[6] == j and next.up[7] == i):
                    gameBoard[j][i+3] = "@"
                    #gameBoard[j][i+3] = next.up.item(j,i)
    
    return gameBoard,next

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
    
def rotate(tetromino,gBoard,lBoard,isLeft):

    searchBoard = [[],[]]
    for i in range(0,len(gBoard)):
        for j in range(0,len(gBoard[0])):
            if gBoard[i][j] == "@" and lBoard[i][j]!= "@" :
                searchBoard[0].append(i)
                searchBoard[1].append(j)

    min_i = min(searchBoard[0])   
    min_j = min(searchBoard[1])
    saveBoard = copy.deepcopy(searchBoard)  
    for i in range(0,min_i+1):
        for j in range(0,min_j+1):
            searchBoard = copy.deepcopy(saveBoard)
            checkTet = []
            for k in range(4):
                searchBoard[0][k] -= i
                searchBoard[1][k] -= j
                checkTet.append(searchBoard[0][k])
                checkTet.append(searchBoard[1][k])

            if checkTet == tetromino.up:
                
                gBoard[checkTet[0]+i][checkTet[1]+j] = " "
                gBoard[checkTet[2]+i][checkTet[3]+j] = " "
                gBoard[checkTet[4]+i][checkTet[5]+j] = " "
                gBoard[checkTet[6]+i][checkTet[7]+j] = " "

                if isLeft:
                    gBoard[tetromino.left[0]+i][tetromino.left[1]+j] = "@"
                    gBoard[tetromino.left[2]+i][tetromino.left[3]+j] = "@"
                    gBoard[tetromino.left[4]+i][tetromino.left[5]+j] = "@"
                    gBoard[tetromino.left[6]+i][tetromino.left[7]+j] = "@"
                else:
                    gBoard[tetromino.right[0]+i][tetromino.right[1]+j] = "@"
                    gBoard[tetromino.right[2]+i][tetromino.right[3]+j] = "@"
                    gBoard[tetromino.right[4]+i][tetromino.right[5]+j] = "@"
                    gBoard[tetromino.right[6]+i][tetromino.right[7]+j] = "@"

                return(gBoard)
            
            elif checkTet == tetromino.left:
                
                gBoard[checkTet[0]+i][checkTet[1]+j] = " "
                gBoard[checkTet[2]+i][checkTet[3]+j] = " "
                gBoard[checkTet[4]+i][checkTet[5]+j] = " "
                gBoard[checkTet[6]+i][checkTet[7]+j] = " "

                if isLeft:
                    gBoard[tetromino.down[0]+i][tetromino.down[1]+j] = "@"
                    gBoard[tetromino.down[2]+i][tetromino.down[3]+j] = "@"
                    gBoard[tetromino.down[4]+i][tetromino.down[5]+j] = "@"
                    gBoard[tetromino.down[6]+i][tetromino.down[7]+j] = "@"
                else:
                    gBoard[tetromino.up[0]+i][tetromino.up[1]+j] = "@"
                    gBoard[tetromino.up[2]+i][tetromino.up[3]+j] = "@"
                    gBoard[tetromino.up[4]+i][tetromino.up[5]+j] = "@"
                    gBoard[tetromino.up[6]+i][tetromino.up[7]+j] = "@"
                
                return(gBoard)

            elif checkTet == tetromino.down:
                
                gBoard[checkTet[0]+i][checkTet[1]+j] = " "
                gBoard[checkTet[2]+i][checkTet[3]+j] = " "
                gBoard[checkTet[4]+i][checkTet[5]+j] = " "
                gBoard[checkTet[6]+i][checkTet[7]+j] = " "

                if isLeft == 0:
                    gBoard[tetromino.left[0]+i][tetromino.left[1]+j] = "@"
                    gBoard[tetromino.left[2]+i][tetromino.left[3]+j] = "@"
                    gBoard[tetromino.left[4]+i][tetromino.left[5]+j] = "@"
                    gBoard[tetromino.left[6]+i][tetromino.left[7]+j] = "@"

                else:
                    gBoard[tetromino.right[0]+i][tetromino.right[1]+j] = "@"
                    gBoard[tetromino.right[2]+i][tetromino.right[3]+j] = "@"
                    gBoard[tetromino.right[4]+i][tetromino.right[5]+j] = "@"
                    gBoard[tetromino.right[6]+i][tetromino.right[7]+j] = "@"

                return(gBoard)

            elif checkTet == tetromino.right:

                gBoard[checkTet[0]+i][checkTet[1]+j] = " "
                gBoard[checkTet[2]+i][checkTet[3]+j] = " "
                gBoard[checkTet[4]+i][checkTet[5]+j] = " "
                gBoard[checkTet[6]+i][checkTet[7]+j] = " "

                if isLeft == 0:
                    gBoard[tetromino.down[0]+i][tetromino.down[1]+j] = "@"
                    gBoard[tetromino.down[2]+i][tetromino.down[3]+j] = "@"
                    gBoard[tetromino.down[4]+i][tetromino.down[5]+j] = "@"
                    gBoard[tetromino.down[6]+i][tetromino.down[7]+j] = "@"
                else:
                    gBoard[tetromino.up[0]+i][tetromino.up[1]+j] = "@"
                    gBoard[tetromino.up[2]+i][tetromino.up[3]+j] = "@"
                    gBoard[tetromino.up[4]+i][tetromino.up[5]+j] = "@"
                    gBoard[tetromino.up[6]+i][tetromino.up[7]+j] = "@"
                
                return(gBoard)

    return gBoard
            
            