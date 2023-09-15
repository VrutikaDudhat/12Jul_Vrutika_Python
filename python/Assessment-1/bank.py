from func import *

print("Welcome To Python Bank Management System")
print(" ")
print("1) Banker")
print("2) Customer")
print("3) Exit")
print(" ")

display=input("Choose your Role :")
if display=='1':
    role()  

a=input("Enter operation which you want to perform :")
if a=='1':
    customer()
    xyz()

elif a=='2':
    print("View Customer...")
    view()

# ----------------------------------------------------- #

ch1='y'
while(ch1=='y'):
    print("1.Withdraw\n2.deposit\n4.View balance")
    ch=int(input("Select any operation :"))
    #if (ch==1):
       # creatAccount()
    if (ch==1):
        amnt=int(input("Enter Amount to Withdraw :"))
        withdraw(amnt)
    elif (ch==2):
        amnt=int(input("Enter Amount to Deposite :"))
        deposit(amnt)
    elif (ch==3):
        chckbalance()
    else:
        print("Please select any 4 options available above...")

    print("Do you want to perform more operation : press y for yes :")
    ch1=input()  



