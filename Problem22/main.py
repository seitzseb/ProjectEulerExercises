from string import ascii_uppercase

with open("Problem22/input.txt","r") as f:
    inp = f.read().split(",")

values = ascii_uppercase

inp = [x.strip("\"") for x in inp]
inp = sorted(inp)

count = 0
for idx,name in enumerate(inp):
    
    value = sum([values.index(letter)+1 for letter in name])
    count += value*(idx+1)

print(count)