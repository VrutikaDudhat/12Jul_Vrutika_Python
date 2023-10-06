# Write a Python program to find the length of a tuple.

data=[]
n=int(input("Enter number of data :"))

for i in range(n):
    x=input("\tEnter elements :")
    data.append(x)
    
print(tuple(data))
print("Length is :",len(data))
