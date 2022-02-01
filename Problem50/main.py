from sympy import isprime, primerange

primes = list(primerange(1e6))

maxJ = 0
maxPrime = 0
length = 0
lastj = len(primes)

for i in range(len(primes)):
    for j in range(i+length,lastj):
        sol = sum(primes[i:j])
        if sol < 1e6:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break

print(largest)