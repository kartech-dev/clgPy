num = input("Enter a number: ")

if all(d == num[0] for d in num):
    print(num, "has all equal digits")
else:
    print(num, "does not have all equal digits")