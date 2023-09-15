class data():
    id=0
    name=""
    gender=""
    contact=0
    password=0
    
    def registration(self):
        print("-----Enter customer register details-----")
        self.id=int(input("Enter id :"))
        self.name=input("Enter name :")
        self.gender=input("Enter gender :")
        self.contact=int(input("Enter contact no. :"))
        self.password=int(input("Enter password :"))

    def login(self):
        print("")
        print("-----Enter customer login details-----")
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
            

b=bank()
b.registration()
b.login()
b.printdata()
