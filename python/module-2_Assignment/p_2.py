#  Write a Python program to get the Factorial number of given number.


y=int(input("Enter Number:"))
f=1

for i in range(1,y+1):
    f=f*i
print(f)