import numpy as np

import files.tetromino as tet

gameBoard = np.zeros((20,10))
for i in range (20):
    for j in range (10):
        if gameBoard[i,j]==0:
            gameBoard[i,j]=1
print(tet.j.up)

