# Write a Python program to write a list to a file. 

items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('items.txt','w')

for i in items:
	file.write(i+"\n")
print()

# --------------------------- #

"""l=[10,20,30,40,50]

f=open("items.txt","w")
f.write(f"{l}")
print("write sucessfull..")"""