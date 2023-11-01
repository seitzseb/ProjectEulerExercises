spiral = [1]

for i in range(1,1001,2):
    for j in range(4):
        spiral.append(spiral[-1]+i+1)
print(sum(spiral))