# Write a Python program to read a random line from a file. 

import random

f=open("my_file.txt",'r')
lines=f.readlines()
print(random.choices(lines))