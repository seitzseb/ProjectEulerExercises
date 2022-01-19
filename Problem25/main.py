fib = [1,1]

def nextFib(a,b):
    return (a+b)

idx = 2
while len(str(fib[1]))<1000:
    idx +=1
    fib[0],fib[1] = fib[1],nextFib(fib[0],fib[1])
print(fib[1],idx)