from decimal import *
import time

res = 0
for i in range(1,1001):
    num = (i**i)%int(1e10)
    print(num)
    res = res%int(1e10)
    res+=num
print(res)