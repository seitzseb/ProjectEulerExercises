mins = []

for d in range(8):
    mind = 10000
    for x in range(10):
        for y in range(10):
            x2 = int(str(x)+str(2))
            y2 = int(str(y)+str(2))
            dy2 = d*y2
            calc = x2-dy2
            if calc < 0:
                pass
            if mind is None:
                mind = calc
                continue
            if calc < mind:
                print(f"mind for {x2}-{d}*{y}2 is {mind}")
                mind = calc
    mins.append(mind)
print(mins)