lower = True
i = 2
finsum = 0

while lower:
    lower = len(str(i*9**5))>i
    print(str(i*9**5),i)
    i+=1
upperBound = i
i = 2
lower = True

while lower:
    sum = 0
    i = str(i)
    lower = len(i)<upperBound
    for digit in range(len(i)):
        sum+= int(i[digit])**5
    i = int(i)
    if i == sum:
        print(i)
        finsum+=sum
    i+=1

print(finsum)