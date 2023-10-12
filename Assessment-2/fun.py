from datatbl import * 

def banker():
    while True:
            print("\n\tBanker")
            ch=input("Enter your choice : \n\t1.Can Register \n\t2.Can Login \n\t3.Can Update All Customer \n\t4.Can View All Customer \n\t5.Can Delete All Customer \n\t6.Exit\n")
            if ch=="1":
                registration()
            elif ch=="2":
                login()
            elif ch=="3":
                update()
            elif ch=="4":
                view()
            elif ch=="5":
                delete()
            elif ch=="6":
                n=input("Do you want to more operation yes for y press no for n :").lower()
                if n=="y" :
                    choice()
                elif n=="n" :
                    exit()
                else :
                    print("\tType yes or no...")
            else:
                print("you existed..")
                exit()

def cust():
        while True:
            print("\n\tCustomer")
            ch=input("What operation are you perform:\n\t1.Register\n\t2.Login\n\t3.Withdraw Balance\n\t4.Deposit Balance\n\t5.View Balance\n\t6.Exit\n")

            if ch=="1":
                registration()
            elif ch=="2":
                login()
            elif ch=="3":
                print("------Withdraw Balance------")
                withdraw()
            elif ch=="4":
                print("------Deposite Balance------")
                deposite()
            elif ch=="5":
                print("------View Balance------")
                viewbalance()
            elif ch=="6":
                n=input("Do you want to more operation yes for y press no for n :").lower()
                if n=="y" :
                    choice()
                elif n=="n" :
                    exit()
                else :
                    print("\tType yes or no...")
            else:
                print("you existed..")
                exit()




def choice():
    x=input("Select your role :\n\t1.Banker \n\t2.Customer\n")

    if x=="1":         
        banker()
    elif x=="2":
        cust()
    else:
        print("Select any role...")

choice()