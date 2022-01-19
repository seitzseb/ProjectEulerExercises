import math
import time
num = 10000

testnum = 220
def divisors (x):
    divs = []
    for i in range(1,int(math.sqrt(x)+1)):
        
        if x%i == 0:
            divs.append(i)
            if i is not x//i:
                divs.append(x//i)
    
    return sorted([div for div in divs if div<x])

def amicable(a):
    da = sum(divisors(a))
    db = sum(divisors(da))
    if db == a and a!=da:
        print(a,da,db)
        time.sleep(1)
        return da
    else:
        return 0


count = 0
for i in range(num):
    count += amicable(i)
    print(i)
print(count)