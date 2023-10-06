# Write a Python program to check a list is empty or not.

a=[]
n=int(input("Enter number of elements :"))

for i in range(n):
    x=input("\tEnter values =")
    a.append(x)
print("Your list =",a)

if a==[]:
    print("List is empty....")
else:
    print("List is not empty....")
