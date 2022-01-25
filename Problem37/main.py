from primes import sieve
import time


primeNums = sieve(int(1e6))
resTrunc = []


def truncat(num):
    truncNums = []
    #forward:
    for i in range(1,len(num)):
        truncNums.append(int(num[i:]))
        truncNums.append(int(num[:-i]))
    return truncNums

for i,prime in enumerate(primeNums):
    if i%500 == 0:
        print(round((i/len(primeNums)*100),2),"% done")

    toCheck = set(truncat(str(prime)))

    if toCheck.issubset(primeNums) and prime>10:
        resTrunc.append(prime)
        print(len(resTrunc)," truncable primes found")
        print(resTrunc)
        time.sleep(1)

print(sum(resTrunc))