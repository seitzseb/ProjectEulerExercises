from primes import sieve
import time 
from sympy import isprime
from itertools import permutations

maxnum = 0

for i in range(3,11):
    digits = set(range(1,i))
    for perm in permutations(digits):
        num = int("".join([str(x) for x in perm]))
        if isprime(num) and num > maxnum:
            maxnum = num
            print(maxnum,"neue maxnum")