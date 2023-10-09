from customer import * 

print("\t1.Banker")
print("\t2.Customer")
x=input("Enter your Choice:")

if x=="1":
    banker()
elif x=="2":
    cust()
else:
    print("Exit")