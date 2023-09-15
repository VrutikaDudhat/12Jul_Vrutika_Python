# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string

s=input("Enter String :")

if len(s)>=2:
     print(s[0:2]+s[-2:])
    
else:
     print(" ") 
   
    





















"""n=input("Enter String :")
l=len(n)
newstring=""

for i in range(0,len(n)):
    if l<3:
        break
    else:
        if i in (0,1,l-2,l-1):
            newstring=newstring+n[i]
        else:
            continue

print("Enter String :",n)
print("New String :",newstring)"""