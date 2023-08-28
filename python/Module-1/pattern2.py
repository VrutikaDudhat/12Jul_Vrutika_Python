'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

for r in range(1,6):
    for c in range(r):
        print(c+1,end=" ") #column
    print(" ") #row break



'''def pattern(n):
      k = 2 * n - 2
      for i in range(0,n):
           for j in range(0,k):
               print(end=" ")
           k = k - 1
           for j in range(0, i+1):
                print("*", end=" ")
           print("\r")
 
pattern(5)'''

 
'''word="python"
x=""
for i in word:
    x += i
    print(x)'''






