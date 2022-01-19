from itertools import permutations

nums = list(range(10))
nums = [str(x) for x in nums]
print(nums)

perms = ["".join(p) for p in permutations(nums)]

print(sorted(perms)[int(1e6)-1])