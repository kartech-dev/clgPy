x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
def outer(add,sub,mul,div):
    return add(),sub(),mul(),div()
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print(outer(lambda:add(x,y),lambda:sub(x,y),lambda:mul(x,y),lambda:div(x,y)))
