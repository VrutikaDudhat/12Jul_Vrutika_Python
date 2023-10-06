# Write a Python program to select an item randomly from a list.
import random

li = [] 
n = int(input("Enter the number of elements in list : "))
for i in range(n): 
    x = int(input("\tEnter the elements : "))
    li.append(x) 
print(li)

print("Randomly selected item :",random.choice(li))
#random.shuffle(li)
print("New List of randomly generated :\n\t",li)
