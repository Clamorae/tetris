import numpy as np
import copy
import files.tetromino as tet
import files.display as dis
import files.gameLogic as gl

tetromino = [tet.i,tet.j,tet.l,tet.o,tet.s,tet.t,tet.z]
gameBoard,lockBoard = gl.createGB()

#test
for i in range(18,20):
    for j in range(2,10):
        gameBoard[i][j] = "@"
        lockBoard[i][j] = "@"
#end test

gameBoard = gl.spawnTetromino(gameBoard,tetromino)

stuck = False
while stuck==False:
    gameBoard,stuck = gl.frame(gameBoard,lockBoard)
    gl.left(gameBoard,lockBoard)
    dis.printGB(gameBoard)

gameBoard = gl.check_line(gameBoard)
lockBoard = copy.deepcopy(gameBoard)
dis.printGB(gameBoard)
