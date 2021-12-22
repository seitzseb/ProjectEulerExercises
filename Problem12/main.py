import math

def gaussum(n):
    return (n**2+n)//2

def get_factors(n):
    #add the divisor and the times it fits in the trinumber and add all of these up
    return sum(2 for i in range(1,round(math.sqrt(n))) if not n%i)

#primes = load_primes("primes.txt")
i, solved = 0, False
maxlen = 0
while not solved:
    tri = gaussum(i) #number to check
    print("current number: ",tri)
    if get_factors(tri) > 499:
        solved = True
        print("SOLVED",tri)
    i+=1    