#Write a function power of(x) that returns another function to raise numbers to the power of x.
def power_of(x):
    return lambda y: y ** x
square = power_of(2)
cube = power_of(3)
print(square(5))
print(cube(5))