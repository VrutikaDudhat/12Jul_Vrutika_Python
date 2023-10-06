# Write a Python program to replace last value of tuples in a list.

l=[]
n=int(input("Enter number of data  in list:"))

for i in range(n):
    x=input("\tEnter elements :")
    l.append(x)
print("old list :",l)
l[:-1] = "Python"
print("New list :",l)

# ---------------- #

"""x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)"""
    
 