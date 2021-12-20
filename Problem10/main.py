def sieve(n):
    b, p, ps = [True] * (n+1) ,2, []
    for p in range(2,n+1):
        if b[p]:
            ps.append(p)
            print(p)
            for i in range(p,n+1,p):
                b[i] = False
    return ps

print(sum(sieve(int(2e6))))