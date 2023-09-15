#How will you remove last object from a list?Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

city=[]

n=int(input("Enter number of city:"))
for i in range(n):
    x=input("Enter your city:")
    city.append(x)
    city.sort()

print(city)
city.pop()
print(city)