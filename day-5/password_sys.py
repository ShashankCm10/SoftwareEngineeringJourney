attempts=3
password=input("Enter your password: ")
while password!="1234" and attempts>0:
    print("Access denied,please try again")
    password=input("Enter your password: ")
    attempts=attempts-1
if password=="1234":
    print("Access granted")
else:
    print("Access denied. You have been locked out.")