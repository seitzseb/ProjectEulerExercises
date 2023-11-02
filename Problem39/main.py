# a**2 + b**2 = c**2
#a+b<c
#b+c<a
#c+a<b
#a+b+c = p

import time
import math

maxposs = 0
maxP = 0

for p in range(1001):
    poss = 0
    if p == 120:
        print("HERE COMES THE TESTCASE")
        time.sleep(1)
    for a in range(1,p//2):
        for b in range(a,p-a):
            c =  math.sqrt((a**2)+(b**2))
            if c%1 == 0 and a+b+c == p:
                c = int(c)
                print(a,b,c,"\t",p)
                poss += 1
                time.sleep(.01)
    if poss > maxposs:
        maxposs = poss
        maxP = p
        print(maxP," has ",maxposs," possibilities")

print(maxP," has ",maxposs," possibilities, which is the solution")