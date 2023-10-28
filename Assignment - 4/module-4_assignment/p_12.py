# Write python program that user to enter only odd numbers, else will raise an exception. 

try:
   n=int(input("Enter Number :"))

   if n%2==0:
     raise ValueError
   print(n)

except ValueError:
   print("Enter only odd number:")