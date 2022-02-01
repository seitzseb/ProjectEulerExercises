notFound = True

def isPentagonal(x):
    if (1+(24*x+1)**0.5) %6 == 0:
        return True
    else:
        return False

def isHexagonal(x):
    if ((8*x+1)**0.5 +1) % 4 == 0:
        return True
    else:
        return False 

i = 1
while notFound:
    i+=1
    tri = i*(i+1)/2
    if isPentagonal(tri) and isHexagonal(tri) and tri != 40755:
        notFound = False
        result = tri
        print("found")
print(int(result))