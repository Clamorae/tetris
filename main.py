import numpy as np
from getkey import getkey,keys 
from time import sleep
from threading import Thread
import copy
import files.tetromino as tet
import files.display as dis
import files.gameLogic as gl


#TODO - input
#TODO - full down func
#TODO - GUI

tetromino = [tet.i,tet.j,tet.l,tet.o,tet.s,tet.t,tet.z]
gameBoard,lockBoard = gl.createGB()
level = [1,0]

gameBoard,current = gl.spawnTetromino(gameBoard,tetromino)

# def timer(time):
#     sleep(time)
#     gameBoard,stuck = gl.frame(gameBoard,lockBoard)
#     timer(time)

# myThread = Thread(target=timer, args=(1,))
# myThread.start()

# while 1:
#     key = getkey()
#     buffer = []
#     if key == keys.LEFT:
#         gameBoard = gl.left(gameBoard,lockBoard)
#     elif key == keys.RIGHT:
#         gameBoard = gl.right(gameBoard,lockBoard)
#     else:
#         print("wrong key")

