#Write a program that writes a list of numbers [10, 20, 30, 40, 50] to a le (one per line), then reads the le and prints the numbers as a list.
def write_and_read_numbers(file_path):
    numbers = [10, 20, 30, 40, 50]
    try:
        with open(file_path, 'w') as file:
            for number in numbers:
                file.write(f"{number}\n")
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
            read_numbers = [int(line.strip()) for line in lines]
            return read_numbers
    except Exception as e:
        return str(e)
    