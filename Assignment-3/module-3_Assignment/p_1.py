# Write a Python function to get the largest number, smallest num and sum of all from a list.

li = []
num = int(input("How many numbers you want to enter : "))
for n in range(num):
    numbers = int(input("\tEnter number :"))
    li.append(numbers)
print("Maximum element in the list is :", max(li), "\nMinimum element in the list is :", min(li))

print(li)
sum_result=sum(li)
print("Sum of list is :",sum_result)
