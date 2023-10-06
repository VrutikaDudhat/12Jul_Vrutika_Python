# Write a Python program to create a tuple with different data types. 

data=[]
n=int(input("Enter number of elements:")) #n=5

for i in range(n):
    x=input("\tEnter an elements:") # enter diff. datatypes
    data.append(x)

print("Length of :",len(data))
print(tuple(data))