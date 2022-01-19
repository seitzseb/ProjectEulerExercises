import math

num = math.factorial(100)
num = str(num)
res = sum([int(x) for x  in num])
print(res)