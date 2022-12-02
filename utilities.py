## sieve to generate a list of primes
def sieve(n):
    b, p, ps = [True] * (n+1) ,2, []
    for p in range(2,n+1):
        if b[p]:
            ps.append(p)
            print(p)
            for i in range(p,n+1,p):
                b[i] = False
    return ps

if __name__ == "__main__":
    print(sieve(int(100))[-1])
