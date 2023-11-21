# divide and conquer
# split numbers into sections, e.g. first step 3/7 to 1
# track closest, only construct numbers between closest and 3/7
# if number is closer, then assign new closest
# how do you construct numbers of certain value range as fraction?
# move in from top side
# try: if number is too low, then increase the numerator until it is higher
# if number is too high, increase the denominator until its lower

val = 3/7
den = 7
num = 3

while den<1e6:
    if val>=3/7:
        den+=1
    else:
        num+=1
    val = num/den

print(f"found solution, {num,den} computes to {val} while 3/7 is {3/7}")