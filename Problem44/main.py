notFound = True
i = 1

def isPentagonal(x):
    if (1+(24*x+1)**0.5)%6 == 0:
        return True
    else:
        return False

while notFound:
    i+=1
    n = i*(3*i-1)/2
    for j in range(i-1,0,-1):
        m = j*(3*j-1)/2
        if isPentagonal(n-m) and isPentagonal(m+n):
            result = int(n-m)
            notFound = False
            break

print(result)