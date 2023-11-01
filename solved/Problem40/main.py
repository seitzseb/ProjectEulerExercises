limit = 1e6
fractionalPart = list(range(int(limit)))
fraction = "".join([str(x) for x in fractionalPart])

sol = 1
for i in range(1,7):
    sol *=int(fraction[int(10**i)])
    print(int(fraction[int(10**i)]),i)
print(sol)