#Write a program to divide two numbers given by the user. Handle the case when the denominator is 0 using try-except and display a friendly message.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    