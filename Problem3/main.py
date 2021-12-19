#the prime factors of 13195 are 5,7,13, and 29
#what is the largest prime factor of 600851475143?

import math

num = 600851475143

def primes(n):
    nums = []
    
    #get rid of all 2s
    while n%2 == 0:
        nums.append(2)
        n = n//2
    
    #now the number has to be odd
    for i in range(3,int(math.sqrt(n))+1,2):

        while n%i == 0:
            nums.append(i)
            n = n//i
    
    if n > 2:
        nums.add(n)

    return nums
print(primes(num)[-1])