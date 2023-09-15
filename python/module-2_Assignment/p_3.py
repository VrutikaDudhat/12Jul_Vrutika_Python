#  Write a Python program to get the Fibonacci series of given range.

b=int(input("Enter n:"))
b1,b2=0,1

print("Fibonacci Series:",b1,b2,end=" ")

for i in range(2,b):
    b3=b1+b2
    b1=b2
    b2=b3
    print(b3,end=" ")
