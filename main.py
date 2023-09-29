import numpy as np
import copy
import files.tetromino as tet
import files.display as dis
import files.gameLogic as gl

#TODO - 
#TODO - turning pieces
#TODO - input
#TODO - Score computation

tetromino = [tet.i,tet.j,tet.l,tet.o,tet.s,tet.t,tet.z]
gameBoard,lockBoard = gl.createGB()

gameBoard,current = gl.spawnTetromino(gameBoard,tetromino)
gameBoard = gl.findTet(current,gameBoard,lockBoard)
dis.printGB(gameBoard)

stuck = False
while stuck==False:
    gameBoard,stuck = gl.frame(gameBoard,lockBoard)
    #dis.printGB(gameBoard)

gameBoard = gl.check_line(gameBoard)
lockBoard = copy.deepcopy(gameBoard)
#dis.printGB(gameBoard)
