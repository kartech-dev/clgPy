
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
def func(funcc,x,y):
    return funcc(x,y)
def funcc(x,y):
    return x+y
print(func(funcc,x,y))


