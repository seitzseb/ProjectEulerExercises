## sieve to generate a list of primes
def sieve(n):
    print("generating primes")
    n = int(n)
    b, p, ps = [True] * (n+1) ,2, []
    for p in range(2,n+1):
        if b[p]:
            ps.append(p)
            #print(p)
            for i in range(p,n+1,p):
                b[i] = False
    return ps

def isprime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    print(sieve(int(10000))[-1])
    for prime in sieve(1000):
        if not isprime(prime):
            print("da ging was schief")
