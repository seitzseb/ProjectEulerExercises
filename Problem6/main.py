#find the largerst palindrome nuber made from the product of two 3-digit numbers
import numpy as np

def checkPalin (n):
    n = np.array(list(str(n)),dtype=int)
    revn = np.flip(n)
    return np.allclose(n,revn)

startnum = 999
endnum = 100
interval = range(startnum,endnum,-1)

palin = 0
#!nested list super slow, maybe improve in the future
for i in interval:
    for j in interval:
        if checkPalin(i*j):
            if palin<(i*j):
                palin = i*j

print(palin)