# Write a Python program to count the frequency of words in a file. 

f=open("newfile.txt","r")
x=f.read()

count=0
for i in x.split():
     count+=1
print(count)