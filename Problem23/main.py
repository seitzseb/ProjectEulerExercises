import math

limit = 28123
def getDivisors (x):
    divs = []
    
    for i in range(1,int(math.sqrt(x)+1)):
        if x%i == 0:
            divs.append(i)
            if i!= x//i:
                divs.append(x//i)
    return sorted(divs)[:-1]

def abundant(x):
    if x<sum(getDivisors(x)):
        return True
    

abundants = []
for i in range(limit+1):
    if abundant(i):
        abundants.append(i)

abundantpairs = []
for one in abundants:
    for two in abundants:
        abundantpairs.append(one+two)
print("abundantpairs done")
abundantpairs = list(set(abundantpairs))

count = sum([x for x  in range(limit) if x not in abundantpairs])
print(count)