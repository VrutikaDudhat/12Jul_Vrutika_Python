class stud_1:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter stud_1's ID :")
        self.nsub=input("Enter stud_1's Subject :")

class stud_2:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter stud_2's ID :")
        self.asub=input("Enter stud_2's Subject :")

class tops(stud_1,stud_2):
    def printdata(self):
        print("---------stud_1's Data---------")
        print("stud_1's ID:",self.nid)
        print("stud_1's Subject:",self.nsub)
        print("---------stud_2's Data---------")
        print("stud_2's ID:",self.aid)
        print("stud_2's Subject:",self.asub)

tp=tops()
tp.n_getdata()    
tp.a_getdata()
tp.printdata()