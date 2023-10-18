import numpy as np
from getkey import getkey,keys 
import time
from threading import Thread
import copy
import files.tetromino as tet
import files.display as dis
import files.gameLogic as gl

#TODO - full down func
#TODO - better frame down
#TODO - GUI

def beforeDrop(sec):
    time.sleep(sec)
#===================SETUP AT START===============================
tetromino = [tet.i,tet.j,tet.l,tet.o,tet.s,tet.t,tet.z]
gameBoard,lockBoard = gl.createGB()
score = 0
level = [1,0]
   
#===================MAIN LOOP===================================
while 1:  
    gameBoard,current = gl.spawnTetromino(gameBoard,tetromino)
    if gameBoard == 0:
        break
    
    stuck = False
    while stuck == False:    
        timer = Thread(target=beforeDrop,args=(0.5,))
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

            elif key == keys.A:
                gameBoard = gl.rotate(current,gameBoard,lockBoard,True)
                dis.printGB(gameBoard)
                key = getkey()

            elif key == keys.Z:
                gameBoard = gl.rotate(current,gameBoard,lockBoard,False)
                dis.printGB(gameBoard)
                key = getkey()

            elif key == keys.DOWN:
                gameBoard,stuck = gl.fullDown(gameBoard,lockBoard,stuck)
                dis.printGB(gameBoard)
                key = getkey()  

            else:
                print("wrong key")
                key = getkey()

        if stuck == False:
            gameBoard,stuck = gl.frame(gameBoard,lockBoard)

        dis.printGB(gameBoard)


    gameBoard,bscore,level = gl.check_line(gameBoard,level)
    lockBoard = copy.deepcopy(gameBoard)
    score += bscore
print(f"game over your score is {score}")