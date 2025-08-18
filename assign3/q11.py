def digit_sum(n):
    return sum(int(d) for d in str(n))

print("Numbers divisible by the sum of their digits (1 to 10000):")

for num in range(1, 10001):
    if num % digit_sum(num) == 0:
        print(num, end=" ")