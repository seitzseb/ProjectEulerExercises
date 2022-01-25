limit = int(1e6)

def reverse(num):
    return num[::-1]

palindromes = []

for num in range(limit):
    binNum = str(bin(num))[2:]

    if str(binNum) == reverse(str(binNum)) and str(num) == reverse(str(num)):
        palindromes.append(num)
        print(num,reverse(str(num)),binNum,reverse(binNum))

print(sum(palindromes))