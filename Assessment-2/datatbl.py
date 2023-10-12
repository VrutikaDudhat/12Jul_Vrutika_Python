import pymysql
import re

# create daatabase

try:
    dbcon=pymysql.connect(host='127.0.0.1',user='root',password='',database='application')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

#Table Create

create_tbl="create table register(id integer primary key auto_increment,name text,password varchar(20),email varchar(20),balance integer)"
try:
    cr.execute(create_tbl)
    print("\tTable created!...")
except Exception as e:
    print(e)


#Insert Data

def registration():
        print("-----Enter registration details-----")
        nm=input("Enter your name :")
        pswd=input("Enter password :")
        email=input("Enter your email :")
        ptn="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        r=re.search(ptn,email)

        if r:
            insert_data=f"insert into register(name,password,email)values('{nm}','{pswd}','{email}')"
            cr.execute(insert_data)
            dbcon.commit()
            print("\tRegistration succesfully...")
        else:
            print("\tEnter proper email...")
            registration()


def login():
        print("-----Enter Login details-----")
        nm=input("Enter nm :")
        password=input("Enter password :")
        query = f"select * from register where name='{nm}' and password='{password}'"
        cr=dbcon.cursor()
        cr.execute(query)
        data=cr.fetchall()
        if data is not None:
            print("\tLogin succesfully...")
        else:
            print("\tInvalid username and password...")
            login()
        

# Update data

def update():
    print("What do you want to update :")
    ch=input("\t1.Username \n\t2.Password \n\t3.Email \n\t4.Exit\n")

    if ch=="1":
        print("Username")
        username()
    elif ch=="2":
        print("Password")
        password()
    elif ch=="3":
        print("Email")
        email()
    else :
        print("You exited...")
        exit()
        

def username():
    nm=input("Enter your old name :")
    cr.execute(f"select name from register where name='{nm}'")

    if cr.fetchone() is not None:
        new_nm=input("Enter your updated name :")
        cr.execute(f"update register set name='{new_nm}' where name='{nm}'")
        dbcon.commit()
        print("\tUpdated succesfull....")
    else:
        print("\tInvalid Username...")

def password():
    nm=input("Enter your Username :")
    cr.execute(f"select name from register where name='{nm}'")

    if cr.fetchone() is not None:
        newpass=input("Enter your new password :")
        cr.execute(f"update register set password='{newpass}' where name='{nm}'")
        dbcon.commit()
        print("\tUpdated succesfull....")
    else:
        print("\tInvalid Username...")

def email():
    nm=input("Enter your Username :")
    cr.execute(f"select name from register where name='{nm}'")

    if cr.fetchone() is not None:
        newemail=input("Enter your new Email :")
        cr.execute(f"update register set email='{newemail}' where name='{nm}'")
        dbcon.commit()
        print("\tUpdate succesfull....")
    else:
        print("\tInvalid Username...")

# View data

def view():
    print("-----View Record details-----")
    select="select name,password,email from register"
    try:
        if cr.execute(select):
            data=cr.fetchall()
            for i in data:
                print(i)
        else:
                print("\tNot any record available...")
    except Exception as e:
        print(e)

# delete record

def particulardelete():
    user=input("Which id that you want to delete :")
    delete=(f"delete from register where id='{user}'")
    try:
        cr.execute(delete)
        dbcon.commit()
        print("\tRecord deleted succesfully...")
    except Exception as e:
        print(e)

def alldelete():
    delete=("delete from register")
    try:
        cr.execute(delete)
        dbcon.commit()
        print("\tDelete all customer succesfully...")
    except Exception as e:
        print(e)

def delete():
    print("What do you want to perform :")
    ch=input("\t1.Delete particular customer \n\t2.Delete all customer\n")

    if ch=='1':
        particulardelete()
    elif ch=='2':
        alldelete()
    else:
        print("\tSelect any one operation...")


def withdraw():
    name=input("Enter username :")
    paswd=input("Enter password :")
    cr.execute(f"select * from register where name='{name}' and password='{paswd}'")
    data=cr.fetchone()

    if data is not None:
        amount=int(input("Enter amount that you want to withdraw :"))
        try:
            cr.execute(f"select balance from register where name='{name}'")
            bal=cr.fetchone()[0]

            if bal>amount :
                update=bal-amount
                cr.execute(f"update register set balance='{update}' where name='{name}'")
                dbcon.commit()
                print("\tWithdraw Succesfully...")
            else :
                print("\tInceffiecnt Balance...")
        except Exception as e:
            print(e)
    else :
        print("\tInvalid username and password...")
        print("\tPlease try again...")
        withdraw()
#withdraw()

"""def deposite():
    name=input("Enter username :")
    paswd=input("Enter password :")
    cr.execute(f"select * from register where name='{name}' and password='{paswd}'")
    data=cr.fetchone()

    if data is not None:
        amount=int(input("Enter amount that you want to deposite :"))
        try:
            cr.execute(f"select balance from register where name='{name}'")
            bal=cr.fetchone()[0]

            update=bal+amount
            cr.execute(f"update register set balance='{update}' where name='{name}'")
            dbcon.commit()
            print("\tDeposite Succesfully...")
       
        except Exception as e:
            print(e)
    else :
        print("\tInvalid username and password...")
        print("\tPlease try again...")
        deposite()"""

def deposite():
      name=input("Enter username:")
      pswd=input("Enter password:")

      cr.execute(f"select * from register where name='{name}' and password='{pswd}'")

      data=cr.fetchone()
      if data is not None:                      
          amount=int(input("Enter amount that you want to deposite:"))
          try:
                  cr.execute(f"select balance from register where name='{name}'")
                  balance=cr.fetchone()[0]
           
                  update=balance+amount
                  cr.execute(f"update register set balance='{update}' where name='{name}'")
                  dbcon.commit()
                  print("\tDeposite successfully.......")
            
          except Exception as e:
               print(e)  

      else :
        print("\tInvalid username and password...")
        print("\tPlease try again...")
        deposite()
#deposite()

def viewbalance():
    name=input("Enter username :")
    paswd=input("Enter password :")
    cr.execute(f"select * from register where name='{name}' and password='{paswd}'")
    data=cr.fetchall()

    if data is not None:
        try:
            showbal=(f"select * from register where balance ")
            cr.execute(showbal)
            cr.fetchall()

            for i in data :
                print(i)
           
        except Exception as e:
            print(e)
    else :
        print("\tInvalid username and password...")
        print("\tPlease try again...")
        viewbalance()
 
 #  --------------------------------------- #

#class banker():
"""def bank():
        print("\n\tBanker")
        ch=input("Enter your choice : \n\t1.Can Register \n\t2.Can Login \n\t3.Can Update All Customer \n\t4.Can View All Customer \n\t5.Can Delete All Customer \n\t6.Exit\n")
        if ch==1:
            registration()
        elif ch==2:
            login()
        elif ch==3:
            update()
        elif ch==4:
            view()
        elif ch==5:
            delete()
        elif ch==6:
            n=input("Do you want to more operation yes for y press no for n :").lower()
            if n=='y' :
                cust()
            elif n=='n' :
                exit()
            else :
                print("\tType yes or no...")
        else:
            #print("\tSelect any operation...")
            print("you existed..")
            exit()

#b=banker()


#class customer:
def cust():
        while True:
            print("\n\tCustomer")
            ch=input("What operation are you perform :\n\t1.register\n\t2.login\n\t3.update\n\t4.view\n\t5.delete\n\t6.Exit\n")
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
                #print("Select any operation...")
                print("you existed..")
                exit()"""
#c=customer()
