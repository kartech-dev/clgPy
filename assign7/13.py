print("Enter the length of the list:")
n = int(input())
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
