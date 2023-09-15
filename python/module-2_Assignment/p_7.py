# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
c=int(input("Enter Number 3:"))

sum=0

if a==b or b==c or c==a:
    print("sum is :",sum)

else:
    total=a+b+c
    print("The sum is :",total)

# -------------------------------- #

"""a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))

if a==b or b==c or c==a:
    print("sum is",0)

else:
    print("sum is",a+b+c)"""