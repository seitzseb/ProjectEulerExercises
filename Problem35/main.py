from primes import sieve
import time 

primeNums = sieve(int(1e6))

circularPrimes = []

for prime in primeNums:
    primeDigits = [x for x in str(prime)]
    toCheck = []
    for i in range(len(primeDigits)):
        tempPrimeDigits = [primeDigits[-i+j] for j in range(len(primeDigits))]
        toCheck.append(int("".join(tempPrimeDigits)))

    if set(toCheck).issubset(primeNums):
        print(toCheck)
        [circularPrimes.append(x) for x in toCheck]
        circularPrimes = list(set(circularPrimes))
        print (len(circularPrimes))

print(sorted(circularPrimes))