import time

max_digit_sum = 0

for a in range(100,0,-1):
    for b in range(100,0,-1):
        digit_sum = sum(int(i) for i in str(a**b))
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
            print(f"new max found, {a**b} has a digit sum of {digit_sum}")
            time.sleep(2)

print(max_digit_sum)