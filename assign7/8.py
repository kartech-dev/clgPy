def square(num):
    return num ** 2
numbers = []
for i in range(5):
    num = int(input("Enter number {}: ".format(i+1)))
    numbers.append(num)
squared_numbers = list(map(square, numbers))
print(squared_numbers)


