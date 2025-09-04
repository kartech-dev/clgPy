#Write a program to count the number of lines in a le.
fo = open("notes.txt", "r")
lines = fo.readlines()
num_lines = len(lines)
print("Number of lines:", num_lines)
fo.close()
                    