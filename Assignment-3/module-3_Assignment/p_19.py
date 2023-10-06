# Write a Python program to convert a list to a tuple.

data=[]
n=int(input("Enter number of data :"))

for i in range(n):
    x=input("\tEnter elements :")
    data.append(x)

print("Befor list :",data)   
print("Afer convert list to tuple :",tuple(data))
