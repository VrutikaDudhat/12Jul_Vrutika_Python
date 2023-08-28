 # creating a file..

"""open('test.txt','x') # x - mode for file creating

open('newfile.txt','w') # w - mode for file creating + write

open('hello.txt','a') # a - mode for file creating + append
"""


# ---------------------------------- #


import datetime
x=datetime.datetime.now()

n=open('newfile.txt','a')
a=int(input("Enter num : "))

for i in range(a):
    id=int(input("Enter id :"))
    nm=input("Enter nm :")
    ct=input("Enter city :")

    n.write(f"Id:{id}\nName:{nm}\nCity:{ct}\n{x}\n")