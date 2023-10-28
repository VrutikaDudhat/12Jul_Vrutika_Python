# Write a Python program to read a file line by line and store it into a list

f=open("my_file.txt","r")
lines = []
for i in f:
        lines.append(i)
        print(lines)
        