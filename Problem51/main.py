import math
import utilities

def is_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

for i in range(10):
    print(is_prime(i))

primes = utilities.sieve(1e6)
print("primes generated")



for i in primes:
    if len(set(str(i))) < len(str(i)):
        pass