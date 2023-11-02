#what is the 10 001st prime number

import math
import numpy as np

numcount = 10001
testnum = 6
primes = []
i = 2
while len(primes)<numcount:
    truncnum = math.floor(math.sqrt(i))
    toCheck = [x for x in primes if x<= truncnum]
    isPrime = True
    for prime in toCheck:
        if i%prime== 0:
            isPrime = False
    if isPrime:
        primes.append(i)
            
    i+=1
    print(len(primes))

#since prime numbers are a recurring theme in these problems save it as a txt file
def save_primes(primes):
    primes = np.array(primes)
    np.savetxt("primes.txt",primes)

save_primes(primes)
print(primes[-1])