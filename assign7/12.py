
from functools import reduce
strings = ["Hello", " ", "World", "!"]
result = reduce(lambda x, y: x + y, strings)
print(result)