import numpy as np

def getnext(x):
    if x%2 == 0:
        #even
        return x//2
    else:
        #odd
        return (3*x)+1

maxnum = int(1e6)
rows = [x for x in range(2,maxnum)]

calc = np.array((rows,[0 for i in rows]),dtype=np.int64)
vfunc = np.vectorize(getnext)
calc[1,:] = vfunc(calc[0,:])
print(calc)
# second term done
count = 2
while calc.shape[1] > 1:
    count +=1 
    calc[1,:] = vfunc(calc[1,:])
    toDelete = np.where(calc[1,:] == 1)[0]
    calc = np.delete(calc,toDelete,axis = 1)
    print(calc[1,:])
    print(max(calc[1,:]))
    print(calc.shape)
print(calc)
print(count)