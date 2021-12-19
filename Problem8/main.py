#read input and construct 20x50 np array
with open("Problem8/input.txt","r") as f:
    inp = f.read()
    inp = inp.replace("\n","")

adjacentLength = 13
maxProd = 0

for i in range(0,len(inp)-adjacentLength):
    product = 1

    for j in range(i,i+adjacentLength):
        product *= int(inp[j:j+1])

        if product > maxProd:
            maxProd = product
print(maxProd)