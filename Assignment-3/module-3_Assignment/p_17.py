# Write a Python program to check whether an element exists within a tuple.

tuple = (4, 6, 8, 11, 22, 43, 58, 99, 16)
print("Tuple Items = ", tuple)

number = int(input("Enter Tuple Item to Find = "))

if number in tuple:
    print(number, " is in the Tuple")
else:
    print("Sorry! We haven't found ", number, " in Tuple")