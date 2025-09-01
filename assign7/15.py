def outer(inner):
    return inner()
def inner():
    return "Hello"
print(outer(inner))