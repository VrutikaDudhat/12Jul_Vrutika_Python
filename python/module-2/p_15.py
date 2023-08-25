# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

a=input("Enter String :")

if a.endswith('ing') or len(a)==0:
    print(a+'ly')

elif len(a)>=3:
    print(a)

"""else:
    print(" ")"""