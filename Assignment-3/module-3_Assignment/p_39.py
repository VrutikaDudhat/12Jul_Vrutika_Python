# Write a Python function to calculate the factorial of a number (a nonnegative integer)

n=int(input("Enter number :"))
f=1
for i in range(n,1,-1):
    f=f*i
print(f)