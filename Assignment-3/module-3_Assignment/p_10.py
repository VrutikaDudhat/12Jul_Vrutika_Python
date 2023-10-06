# Write a Python program to find the second smallest number in a list.

li = [] 
n = int(input("Enter the number of elements in list : "))
for i in range(n): 
    x = int(input("\tEnter the elements : ")) 
    li.append(x) 
li.sort() 

print("The sorted list : ", li) 
print("The second smallest value of this list : ",li[1]) 