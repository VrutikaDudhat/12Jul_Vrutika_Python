'''
*
* *
* * *
* * * *
* * * * *
'''

'''for r in range(1,6):
    for c in range(r):
        print("*",end=" ") #column
    print(" ") #row break'''







size=5

m=(2*size)-2
for i in range(0,size):
    for j in range(0,m):
        print(end=" ") 
    m=m-1
    for j in range(0, i + 1):
        print("@",end=' ')
    print(" ")
