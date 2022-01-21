from ftplib import MAXLINE
from primes import sieve

def quadraticFormula(a,b,n):
    return int(((n**2)+a*n+b))

primeNums = sieve(int(1e6))
primesUnder1k = [x for x in primeNums if x < 1001]
negPrimesUnder1k = [-x for x in primesUnder1k]
toCheckPrimes = primesUnder1k
[toCheckPrimes.append(x) for x in negPrimesUnder1k]

maxLen = 0
for a in toCheckPrimes:
    for b in toCheckPrimes:
        n = 0
        isPrime = True
        while isPrime:
            checkNum = quadraticFormula(a,b,n)
            if checkNum > 0:
                if checkNum in primeNums:
                    n+=1
                else:
                    isPrime = False
            else:
                isPrime = False
        if n > maxLen:
            maxLen = n 
            print(maxLen," for a:",a," b: ",b)
