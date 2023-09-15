# Write a Python program to count the number of characters (character frequency) in a string

# Using dictionary with list...

n=input("Enter the String: ")
     #n=input("Enter the String: ").lower()
s={} #character frequency

for i in n:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print("Charcter Frequency...")

for key,value in s.items():
    print(key,":",value)
