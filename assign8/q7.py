#Write a program to search for the line numbers that contain a given word. 
def search_word_in_file(file_path, word):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_numbers = [index + 1 for index, line in enumerate(lines) if word in line]
            return line_numbers
    except FileNotFoundError:
        return "File not found."