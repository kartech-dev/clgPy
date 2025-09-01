x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
def comp(comp_func, a, b):
    if comp_func(a, b):
        return a
    else:
        return b
def comp_func(a, b):
    return a > b
larger_number = comp(comp_func, x, y)
print("The larger number is:", larger_number)