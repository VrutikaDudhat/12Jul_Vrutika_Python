import pymysql
#import re


# create daatabase

try:
    dbcon=pymysql.connect(host='127.0.0.1',user='root',password='',database='application')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

#Table Create

create_tbl="create table register(id integer primary key auto_increment,name text,password text,email text)"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data

def registration():
     print("-----Enter registration details-----")
     nm=input("Enter your name :")
     password=(input("Enter password :"))
     email=input("Enter your email :")
    # ptn="^[a-z]+[\._][a-z 0-9]+[@]\w+[.]\w{2,3}$"
    # r=re.search(ptn,email)
     insert_data=f"insert into register(name,password,email)values('{nm}','{password}','{email}')"

     try:
       # if r:
            cr.execute(insert_data)
            dbcon.commit()
            print("\tRegistration succesfully...")
       # else:
           # print("Enter proper email...")
     except Exception as e:
            print(e)


def login():
    print("-----Enter Login details-----")
    nm=input("Enter nm :")
    password=input("Enter password :")
    query = f"select * from register where name='{nm}' and password='{password}'"
     
    try:
        cr.execute(query)
        myresult = cr.fetchall()
         
        for x in myresult:
            print(x)
        print("\tlogin successfully...")
         
    except:
        print("\tinvalid name or password...")
#login()

# Update data
def update():
    print("What do you want to update :")
    ch=input("\t1.username \n\t2.pasword \n\t3.email \n\t4.exit\n")

    if ch=="1":
        print("Username")
        username()
    elif ch=="2":
        print("Password")
        password()
    elif ch=="3":
        print("email")
        email()
    else :
        print("You exited...")
        exit()
        

def username():
    nm=input("Enter your old name :")
    cr.execute(f"select name from register where name='{nm}'")

    if cr.fetchone() is not None:
        newnm=input("Enter your updated name :")
        cr.execute("update register set name='{newnm}' where name='{nm}'")
        dbcon.commit()
        print("\tUpdated succesfull....")
    else:
        print("\tInvalid Username...")

def password():
    nm=input("Enter your Username :")
    cr.execute(f"select name from register where name='{nm}'")

    if cr.fetchone() is not None:
        newpass=input("Enter your new password :")
        cr.execute("update register set password='{newpass}' where name='{nm}'")
        dbcon.commit()
        print("\tUpdated succesfull....")
    else:
        print("\tInvalid Username...")

def email():
    nm=input("Enter your Username :")
    cr.execute(f"select name from register where name='{nm}'")

    if cr.fetchone() is not None:
        newemail=input("Enter your new Email :")
        cr.execute("update register set email='{newemail}' where name='{nm}'")
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
        print("Select any one operation...")


# ------------------------------------------ #

def banker(self):
    print("Banker")
    print("\tCan Register")
    print("\tCan Login")
    print("\tCan Update All Customer")
    print("\tCan View All Customer")
    print("\tCan Delete All Customer")

def cust():
    while True:
        print("select any opertion :")
        ch=input("\t1.register\n\t2.login\n\t3.update\n\t4.view\n\t5.delete\n\t6.Exit\n")
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
            print("You exited...")
            exit()
