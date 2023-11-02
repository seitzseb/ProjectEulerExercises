from sympy import isprime

possible = True
num = 1

while possible:
    num +=1
    possible = False
    if not isprime(num) and num%2 != 0 and num != 1:
        for quad in range(int((num/2)**0.5),0,-1):
            rest = num-2*(quad**2)
            if isprime(rest) and not possible:
                print(num,"=",num-2*(quad**2),"+ 2*",quad,"^2")
                possible = True
        if not possible:
            print(num,"is not possible")
    else:
        possible = True