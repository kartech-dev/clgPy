num = int(input("Enter a number: "))
n = int(input("Enter the digit position from right: "))

digit = (num // 10**(n-1)) % 10

print(f"The {n}th digit from the right in {num} is: {digit}")