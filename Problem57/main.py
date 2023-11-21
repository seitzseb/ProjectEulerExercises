from dataclasses import dataclass

@dataclass
class fraction:
    numerator: int
    denominator: int

sol = 0
fractions = [fraction(3,2)]
for i in range(1000):
    num = fractions[-1].numerator+fractions[-1].denominator*2
    den = fractions[-1].numerator+fractions[-1].denominator
    fractions.append(fraction(num,den))
    if len(str(num))>len(str(den)):
        sol+=1
print(sol)