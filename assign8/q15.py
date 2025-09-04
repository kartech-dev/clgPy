#Write a program that writes user input to a le. Handle cases where the le cannot be opened (e.g., invalid le path).
try:
    file_path = input("Enter the file path to write to: ")
    user_input = input("Enter the text you want to write to the file: ")
    
    with open("new.txt", 'w') as file:
        file.write(user_input)
    print("Text written to the file successfully.")
except IOError:
    print("Error: Could not open or write to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution Completed")
    
    