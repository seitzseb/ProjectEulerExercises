#find the difference between the sum of the squares if the first one hundred natural numbers and the square of the sum

def squaresum(n):
    return sum(range(n+1))**2

def sumsquare(n):
    return sum([x**2 for x in range(n+1)])

def diff(n):
    return (squaresum(n)-sumsquare(n))

print(diff(100))