# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

a=input("Enter the String :")

a_not=a.find("not") # use find or index
a_poor=a.find("poor")

  #if a_poor > a_not:

if a_poor > a_not and a_not>0 and a_poor>0:
    a=a.replace(a[a_not:a_poor+4],"good")
    print(a)

else:
    print(a)
    

