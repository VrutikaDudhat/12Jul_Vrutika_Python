fnm=input("Enter Firstname:")
lnm=input("Enter Lastname:")

#nested
if fnm.isupper() and lnm.isupper():

    email=input("Enter an email:")
    mobile=input("Enter a mobile number:")

    length=len(mobile)
    if len(mobile)==10:
     

     if email.islower() and mobile.isdigit():
            print("Firsname:",fnm)
            print("Lastname:",lnm)
            print("Email:",email)
            print("Mobile:",mobile)
     else:
        print("Error! Plz input valid email address or mobile")

    else:
         print("Not Valid, Please enter only 10 digit..")

else:
    print("Error!Plz input proper details!")


'''email = email.strip().lower()
        if not "@" in email:
            print("Invalid email")
            print()
            return
        elif not (".com" or ".org" or ".edu" or ".gov" or ".net") in email[-4:]:
            print("Invalid email")
            print()
            return
'''

