
maxPan = 0

for i in range(1,10000):

    num = ""

    ct = 1

    while len(num) <9 :
        num += str(i*ct)
        ct+=1
        
    if len(num) == 9 and len(set(num))==9 and "0" not in num:
        if int(num) > maxPan:
            maxPan = int(num)
        
print(maxPan)