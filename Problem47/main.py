from sympy import  isprime


def getPrimeFactors (x):
    factors = []

    while x%2 == 0:
        x = x//2
        factors.append(2)
    
    for i in range(3,int(x**0.5)+1,2):

        while x%i == 0:
            factors.append(i)
            if not isprime(x//i):
                getPrimeFactors(x//i)
            else:
                factors.append(x//i)
            x = x//i
    

    return factors
    
found = False   
i = 10
while not found:
    i+=1
    nums = [i+j for j in range(4)]
    found = True
    for num in nums:
        facs = getPrimeFactors(num)
        if len(set(facs)) == 4:
            print(num," has the following primefactors: ", facs)
        else:
            found = False
    if found:
        print("The first 4 numbers are: ",nums)