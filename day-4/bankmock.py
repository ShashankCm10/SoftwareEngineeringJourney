BALANCE=5000
pin=1234
PIN=int(input("enter your pin"))
if PIN==pin:
    amount=int(input("enter the amount to withdraw"))
    if amount<=0:
        print("invalid amount")
    if amount>BALANCE:
        print("insufficient balance")
    else:
        print("please collect your cash")
else:
    print("invalid pin")            