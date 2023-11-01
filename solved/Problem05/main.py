#what is the smalles positive number that is evenly divisible by all of the numbers from 1 to 20

import math

endnum = 20

for i in range(endnum,math.factorial(endnum),endnum):
    if sum([i%x for x in range(1,endnum+1)]) == 0:
        print(i)
        break