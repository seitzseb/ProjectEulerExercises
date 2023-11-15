# How many
# n-digit positive integers exist which are also an nth power?
# how many nth powers exist whith the base as a natural number
# which have n digits ?

# test cases
x1 = 16807 #5
x2 = 134217728 #9

counter = 0

for i in range(1,10): # iterate bases
    base = i
    exponent = 1
    while (len(str(i**exponent)) == exponent):
        print(f"{i}**{exponent} = {i**exponent}")
        counter +=1
        exponent+=1

print(counter)
