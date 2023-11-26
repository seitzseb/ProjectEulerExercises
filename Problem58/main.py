# Spiraling Primes
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# when is a number on a diagonal ?
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 0, 0, 1, 0, 1, 0, 1, 0, 1, 0

# 2x2:
# 4 3
# 1 2

# 3x3
# 5 4 3
# 6 1 2
# 7 8 9

# 1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49
# -, 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 6

from utilities import isprime

num = 1
diagnums = 0
diagprimes = 0
for dim in range(1,100000):
    for i in range(4):
        num+=dim*2
        if isprime(num):
            diagprimes +=1
        diagnums +=1
        

    ratio = diagprimes/diagnums
    print(f"the Ratio for edgelength of {1+(dim*2)} is {ratio}, max diagnum: {num}")
    #print(diagnums)
    if diagnums> diagprimes*10:
        exit()