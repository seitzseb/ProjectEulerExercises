# generate all numbers:

def tri(n):
    return n*(n+1)/2

def square(n):
    return n**2

def penta(n):
    return n*(3*n-1)/2

def hexa(n):
    return n*(2*n-1)

def hepta(n):
    return n*(5*n-3)/2

def octa(n):
    return n*(3*n-2)

funclist = [tri, square, penta, hexa, hepta, octa]
nums = {}

for func in funclist:
    i = 1
    vals = []
    while(func(i)< 1000):
        i+=1
    while(func(i)<10000):
        vals.append(str(int(func(i))))
        i+=1
    nums[func.__name__] = vals

print("all nums generated")

[print(len(nums[x])) for x in nums]
# octagonal numbers are the smallest

