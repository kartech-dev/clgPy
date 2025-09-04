#Create a text le with multiple lines. Write a program to read the le and print its content line by line.
fo=open("notes.txt","r")
print(fo.read())
fo.close()