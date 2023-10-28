# Write a python program to find the longest words.

f=open("sample.txt","r")
x=f.read()
print(x)
x=x.split()

s=sorted(x,key=len)
print("longest word is :",s[-1])