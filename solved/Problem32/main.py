from itertools import permutations
import time
res = []

for i in permutations(list(range(1,10))):
    i = "".join([str(x) for x in list(i)])
    for alen in range(1,3):
        for blen in range(alen+1,9):
            a = int(i[:alen])
            b = int(i[alen:blen])
            c = int(i[blen:])
            if a*b ==c:
                print(a,"*",b,"=",c)
                abList = sorted([a,b])
                abList.append(c)
                if c not in [x[2] for x in res]:
                    res.append(abList)

print(res)
print(sum([x[2] for x in res]))