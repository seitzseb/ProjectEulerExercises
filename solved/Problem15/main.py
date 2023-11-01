import numpy as np
gridsize = 20

grid = np.zeros((gridsize+1,gridsize+1))

grid[0,:] = 1
grid[:,0] = 1

toFill = np.where(grid==0)

for i in range(len(toFill[0])):
    xPos = toFill[0][i]
    yPos = toFill[1][i]
    grid[xPos,yPos] = grid[xPos-1,yPos]+grid[xPos,yPos-1]

print(int(grid[-1,-1]))