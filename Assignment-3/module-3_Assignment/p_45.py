# Write a Python program to calculate the area of a trapezoid

# formula t=1/2(a+b)*h

a = float(input('Enter the First Base of a Trapezoid : '))
b = float(input('Enter the Second Base of a Trapezoid : '))

Height= float(input('Enter the Height of a Trapezoid :'))

area = 0.5 * (a + b) * Height
print("The Area of a trapezoid ",area)