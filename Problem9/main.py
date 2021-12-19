# find the pythagorean triplet for which a+b+c = 1000
#a<b<c
#a**2+b**2 = c**2
#a+b<1000

import math

for a in range(1,1000):
    for b in range(1,1000-a):
        c = (math.sqrt((a**2)+(b**2)))
        if a+b+c == 1000:
            print(a,b,c,"solution: ",a*b*c)
            exit()

