import math

num = int(input("Enter a number: "))

root = int(math.sqrt(num))

if root * root == num:
    print(num, "is a Perfect Square")
else:
    print(num, "is not a Perfect Square")