# Write a Python function to check whether a number is perfect or not. 

number=int(input("enter number: !"))
sum=0
for i in range(1,number):
    if number%i==0:
        sum=sum+i
if sum==number:
    print("yess.. The entered number is perfect  ")
else:
    print("nooo... The entered number is not perfect")




while True:
   n = int(input("enter a number between 0 and 100: "))
   if 0 <= n <= 100:
      print("yesss")
      break
   print("nooo")
   print('try again...')