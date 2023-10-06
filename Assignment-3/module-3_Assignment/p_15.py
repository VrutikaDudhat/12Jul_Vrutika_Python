# Write a Python program to create a tuple with numbers.

data=[]
n=int(input("Enter number of elements :"))

for i in range(n):
    x=input("\tEnter elements :")
    data.append(x)
print(tuple(data))

# find the index..
for i in data:
    print(f"\tIndex[{data.index(i)}] = {i}")
print(tuple(data))
