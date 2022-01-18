import numpy as np

with open("Problem18/input.txt","r") as f:
    inp = f.readlines()

pyramid =  [(line.strip("\n").split(" ")) for line in inp]
pyramid.reverse()
#print(pyramid)

while len(pyramid)>1:
    topRow = pyramid[0]
    nextRow = pyramid[1]
    for pairNum in range(len(pyramid[0])-1):
        one = pyramid[0][pairNum]
        two = pyramid[0][pairNum+1]
        one = int(one)
        two = int(two)
        if one > two:
            nextRow[pairNum] = one+int(nextRow[pairNum])
        else:
            nextRow[pairNum] = two+int(nextRow[pairNum])
    pyramid = pyramid[1:]
    print(pyramid[0])