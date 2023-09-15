# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

n1=input("Enter string 1 :")
n2=input("Enter string 2 :")

print("Before swap string :",n1,n2)

a1=n2[:2]+n1[2:]
a2=n1[:2]+n2[2:]

print("After swap string :",a1,a2)
