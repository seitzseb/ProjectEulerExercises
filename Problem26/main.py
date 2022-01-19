#NOTE:NOT SOLVED

from decimal import Decimal,getcontext

getcontext().prec = 1000

limit = 1000

nums = [str(Decimal(1)/Decimal(i)) for i in range(2,limit)]
nums = [x for x in nums if len(x) >100]

print(nums[-1])
exit()
cyclelength = 0
while len(nums)>1:
    cyclelength+=1
