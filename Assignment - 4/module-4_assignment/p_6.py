# Write a Python program to read a file line by line store it into a variable. 

def file_read():
        with open ("r") as my_file:
                data=my_file.readlines()
                print(data)
file_read()