#generate fibonacci numbers 

def genFib(end):
    fibs = [1,2]
    while True:
        newfib = fibs[-1]+fibs[-2]
        if newfib < end:
            fibs.append(newfib)
        else:
            return fibs

fibNums = genFib(4e6)

res = sum([x for x in fibNums if x%2 == 0])
print(res)