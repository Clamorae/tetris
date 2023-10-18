import numpy as np
from getkey import getkey,keys 
import time
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



    

def beforeDrop(sec):
    time.sleep(sec)
    print("aled")
    

timer = Thread(target=beforeDrop,args=(5,))
timer.start()

key = getkey()
buffer = []
while timer.is_alive():
    if key == keys.LEFT:
        gameBoard = gl.left(gameBoard,lockBoard)
        key = getkey()
        dis.printGB(gameBoard)
    elif key == keys.RIGHT:
        gameBoard = gl.right(gameBoard,lockBoard)
        dis.printGB(gameBoard)
        key = getkey()
    else:
        print("wrong key")

gameBoard,stuck = gl.frame(gameBoard,lockBoard)
dis.printGB(gameBoard)

