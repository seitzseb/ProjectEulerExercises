from itertools import permutations
import time

starts = []

for perm in permutations(list(range(10)),3):
    num = "".join([str(x) for x in perm])
    if int(num) % 2 == 0:
        starts.append(num)

print(starts)
for j,div in enumerate([3,5,7,11,13,17]):   
    newstarts = []
    for num in starts:
        for i in range(10):
            tempnum = num+str(i)
            if int(tempnum[j+1:])%div == 0 and len(set(tempnum)) == len(tempnum):
                newstarts.append(tempnum)

    starts = newstarts

res = []
for num in starts:
    diff = list(set([str(x) for x in range(10)])-set(num))[0]
    res.append(diff+num)

res = sum([int(x) for x in res])
print(res)