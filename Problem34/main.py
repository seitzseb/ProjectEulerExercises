import math

upperBound = 5


for i in range(3,10**upperBound):
    digits = [math.factorial(int(x)) for x in str(i)]
    if max(digits) > i:
        continue
    elif sum(digits) == i:
        print(i)