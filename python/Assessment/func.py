import datetime
x=datetime.datetime.now()

def role():
        print("Welcome To Banker's App...")
        print(" ")
        print("1) Add Customer")
        print("2) View Customer")     
        print("3) Search Customer")
        print("4) view all customer")
        print("5) Total amounts in bank")
        print(" ")            

def customer():
    d={}
    keys=["Account No. ","Customer Name","Balance"]

    for i in range(len(keys)):
          value=input(f"Enter{keys[i]}:")
          d[keys[i]]=value
    f1=open('customer.txt','a')
    f1.write(f"Customers List:\n\t{d}\n\t{x}\n")

def view():
      f1=open("customer.txt","r")
      print(f1.read())

def xyz(): #open file
       select=input("Do you want to perform more operation : press y for yes and n for no :")
       if select=='y':
            customer()            
       else:
             exit()















# -------------------------------------------------------------------- #
            
accountno=0
customer=" "
bal=0

"""def creatAccount():
    global bal
    accountno=int(input("Enter account no. : "))
    cuustomer=input("Enter customer name :")
    bal=int(input("Enter Balance :"))"""

def showAccountDetails():
    print("Account No. :",accountno)
    print("Customer Name :",customer)
    print("Balance :",bal) 

def deposit(amount):
    global bal
    bal=bal+amount
    chckbalance()

def withdraw(amount):
    global bal
    bal=bal-amount
    chckbalance()

def chckbalance(): #(balance)
    #bal=balance
    print("Current Balance :",bal)

  # --Main-- #
"""ch1='y'
while(ch1=='y'):
    print("1.Creat Account\n2.Withdraw\n3.deposit\n4.cheak balance")
    ch=int(input("Select any operation :"))
    #if (ch==1):
        #creatAccount()
    elif (ch==2):
        amnt=int(input("Enter Amount to Withdraw :"))
        withdraw(amnt)
    elif (ch==3):
        amnt=int(input("Enter Amount to Deposite :"))
        deposit(amnt)
    elif (ch==4):
        chckbalance()
    else:
        print("Please select any 4 options available above...")

    print("Do you want to perform more operation : press y for yes :")
    ch1=input()  """