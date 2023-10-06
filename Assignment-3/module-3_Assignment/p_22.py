# Write a Python program to find the repeated items of a tuple. 

tuple=(12,3,45,10,45,2,7,8,31,3)
print(tuple)

for i in tuple:
    if tuple.count(i)>1:
        print(i)
 