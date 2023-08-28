import random


def getuser(nm,sub,ct):
    x=random.randint(1,100)

    print("Id:",x)
    print("Name:",nm)
    print("Sub:",sub)
    print("City:",ct)

getuser('vrutika','python','rajkot')

d=[]
n=int(input("Entre num of staff details :"))

def getstaff():
    x=random.randint(1,100)
    nm=input("Enter nm :")
    sub=input("Enter sub :")
    city=input("Enter city :")
   # d1=[nm,sub,city]
   # d.append(d1)


    print("ID:",x)
    print("Name:",nm)
    print("Sub:",sub)
    print("city:",city)


for i in range(n):
   getstaff()
   # d.append(getstaff)

#d=getstaff.copy()
print(d)


