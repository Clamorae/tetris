import numpy as np
import copy
import files.tetromino as tet
import files.display as dis
import files.gameLogic as gl

gameBoard,lockBoard = gl.createGB()
dis.printGB(gameBoard)

stuck = False
while stuck==False:
    gameBoard,stuck = gl.frame(gameBoard,lockBoard)
    dis.printGB(gameBoard)
lockBoard = copy.deepcopy(gameBoard)

