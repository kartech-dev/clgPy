try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ValueError:
    print("Error: Please enter valid numbers!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")