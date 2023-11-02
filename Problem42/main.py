import string
import time

with open("Problem42/input.txt","r") as f:
    inp = f.read().split(",")

inp = [x.strip("\"") for x in inp]

s = string.ascii_uppercase
s = list(s)
print(s.index("A"))

maxVal = 0

#0.5n*(n+1) <= 200
#0.5n**2+0.5n <= 200
#n ~ 20
tri = [int((0.5*x**2)+(0.5*x)) for x in range(1,21)]
print(tri)

count = 0
for word in inp:
    value = sum([s.index(x)+1 for x in word])
    if value  in tri:
        count +=1

print(count)