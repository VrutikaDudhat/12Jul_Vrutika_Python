# #WAP to genrate marksheet for 4 subject with total, PR and approprite result condition


s1=int(input("Enter Marks subject 1:"))
s2=int(input("Enter Marks subject 2:"))
s3=int(input("Enter Marks subject 3:"))
s4=int(input("Enter Marks subject 4:"))

if s1<=40 or s2<=40 or s3<=40 or s4<=40:
    print("fail..")
    
else:
    total=s1+s2+s3+s4
    print("Total:",total)

    pr=total/4
    print("PR:",pr)

    if pr>=70:
        print("Dist....")

    elif pr>=60:
        print("First class....")

    elif pr>=50:
        print("Second class....")

    elif pr>=40:
        print("Pass....")
