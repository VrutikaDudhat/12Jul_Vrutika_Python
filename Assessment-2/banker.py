class data():
    id=0
    name=""
    gender=""
    contact=0
    password=0
    
    def registration(self):
        print("-----Enter Bnaker register details-----")
        self.id=int(input("Enter id :"))
        self.name=input("Enter name :")
        self.gender=input("Enter gender :")
        self.contact=int(input("Enter contact no. :"))
        self.password=int(input("Enter password :"))
        f1=open('bank.txt','a')
        f1.write(f"Bankers List:\n\t{self.id}\n{self.name}\n{self.contact}\n{self.password}\n")

    def login(self):
        print("")
        print("-----Enter Bnaker login details-----")
        self.id=int(input("Enter id :"))
        self.name=input("Enter name :")
        self.password=int(input("Enter password :"))
        
class bank(data):
    def printdata(self):
            print("------Registration Details------")
            print("")
            print("Id :",self.id)
            print("Name :",self.name)
            print("Gender :",self.gender)
            print("Contact No.",self.contact)
            print("password :",self.password)
            print("")
            print("------Login Details------")
            print("")
            print("Id :",self.id)
            print("Name :",self.name)
            print("password :",self.password)
            
    def view(self):
      f1=open("bank.txt","r")
      print(f1.read())

b=bank()
b.registration()
b.login()
b.printdata()
b.view()




 

"""class customer():
    id=0
    name=''
    gender=''
    balance=''

    def getdata(self):
        self.id=int(input("Enter id :"))
        self.name=input("Enter name :")
        self.gender=input("Enter gender :")
        self.balance=int(input("Enter balance :"))
        print("")

class data(customer):
        def printdata(self):
            print("------Personal Details------")
            print("")
            print("Id :",self.id)
            print("Name :",self.name)
            print("Gender :",self.gender)
            print("Baance :",balance)
dt=data()
dt.getdata()
dt.printdata()"""

     