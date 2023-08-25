# Write a Python program to count the occurrences of each word in a given sentence

a=input("Enter the string :")
a=a.split()
x={}

for i in a:
        if i in x:
                x[i]+=1
        else:
                x[i]=1

for i,j in x.items():
        print(f"{i}:{j}")        




# ------------------------------------- #


        """string = input("Enter String :")
substring = input("Enter the count string :")

count = string.count(substring)

print("The count of string :", count)
"""         
    