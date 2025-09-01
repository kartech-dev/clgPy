#Write a function make multiplier(n) that returns another function to multiply numbers by n
def make_multiplier(n):
    return lambda x: x * n
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  
print(triple(5))  