#  Write python program that swap two number with temp variable and without temp variable.

'''a=20
b=50

print("A:",a)
print("B:",b)

"""c=a #34
a=b #50
b=c #20"""


a,b=b,a

print("A:",a)
print("B:",b)
'''

#  ---------------------------------------------------------------  #

  # without temp variable

x=int(input("Enter Number x:")) 
y=int(input("Enter Number y:")) 

x,y=y,x

print("After swapping...")

print("x:",x) 
print("y:",y) 

#  --------------------------------------------------------------  #

  # Using temp variable

'''x=int(input("Enter Number x:")) 
y=int(input("Enter Number y:")) 

temp=x
x=y
y=temp

print("After swapping...")

print("x:",x) 
print("y",y) 
'''