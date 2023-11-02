import math
fractions = []

for i in range(10,100):
    for j in range(10,100):
        strI,strJ = str(i),str(j)
        if "0" in strI or "0" in strJ:
            continue
        if strI[0] in strJ or strI [1] in strJ:
            if strI[0] in strJ:
                common = strI[0]
            elif strI[1] in strJ:
                common = strI[1]
            if common*2 == strJ or common*2 == strI:
                continue
            numerator = [x for x  in strI if x is not common][0]
            denominator = [x for x  in strJ if x is not common][0]
            if i/j == int(numerator)/int(denominator) and i/j != 1:
                print(i,"/",j,"is the same as ",numerator,"/",denominator)
                i,j = sorted([i,j])
                numerator,denominator = sorted([numerator,denominator])
                if [numerator,denominator] not in fractions:
                    fractions.append([numerator,denominator])


print(fractions)
nums = math.prod([int(x[0]) for x  in fractions])
denoms = math.prod([int(x[1]) for x in fractions])
fraction = [nums/8,denoms/8]

print(fraction)