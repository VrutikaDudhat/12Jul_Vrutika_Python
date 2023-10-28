# Write a Python program to read last n lines of a file.

f=open("my_file.txt","r")
n=int(input("Enter Lines To Read:"))
print(f.readlines()[0:n])
