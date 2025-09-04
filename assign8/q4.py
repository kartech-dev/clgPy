#Write a program that asks the user for a word and searches for it in a text le, printing the line numbers where it appears. 
fo=open("notes.txt","r")
word=input("Enter the word to search: ")
lines=fo.readlines()
found=False
for i,line in enumerate(lines):
    if word in line:
        print(f"Word found in line {i+1}: {line.strip()}")
        found=True
if not found:
    print("Word not found in the file.")
fo.close()
