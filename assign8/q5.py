# Write a program that writes a list of numbers [10, 20, 30, 40, 50] to a le (one per line), then reads the le and prints the numbers as a list.
fo = open("numbers.txt", "w")
numbers = [10, 20, 30, 40, 50]
for number in numbers:
    fo.write(f"{number}\n")
fo.close()
fo = open("numbers.txt", "r")
lines = fo.readlines()
num_list = [int(line.strip()) for line in lines]
print(num_list)
fo.close()