try:
    number = float(input("Enter a number: "))
    
except ValueError:
    print("Error: Please enter a valid number!")
    
else:
    square = number ** 2
    print(f"Square of {number} is {square}")