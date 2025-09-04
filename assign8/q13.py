#Write a program to open a le, read its contents, and handle FileNotFoundError. Ensure that a message like File operation complete is printed using nally.
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    print("Operation Completed")
