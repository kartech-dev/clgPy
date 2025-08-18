import math

a, b = 18, 32
lcm = (a * b) // math.gcd(a, b)
nearest = (1000 // lcm) * lcm

if nearest >= 1000:
    nearest -= lcm

print("The nearest number to 1000 (less than 1000) divisible by 18 and 32 is:", nearest)