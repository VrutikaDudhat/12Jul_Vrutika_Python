# Write a Python program to remove an empty tuple(s) from a list of tuples. 

def remove(tuples):
    for i in tuples:
        if (len(i)==0):
            tuples.remove(i)
    return tuples

tuples=[(1,23,5,4),(),(9,0,3,54),(),(1,2,3,4,5)]
print(remove(tuples))