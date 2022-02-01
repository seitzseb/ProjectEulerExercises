from itertools import permutations
from sympy import isprime


for i in range(1000,int(1e4)):
    num2 = i+3330
    num3 = num2+3330
    if isprime(i) and isprime(num2) and isprime(num3):
        perm = list(permutations(str(i)))
        perm = ["".join(prm) for prm in perm]
        if str(num2) in perm and str(num3) in perm:
            print(str(i)+str(num2)+str(num3))