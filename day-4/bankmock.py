BALANCE=5000
pin=1234
PIN=int(input("enter your pin"))
if PIN==pin:
    amount=int(input("enter the amount to withdraw"))
    if amount<=0:
        print("invalid amount")
    elif amount>BALANCE:
        print("insufficient balance")
    else:
        print("please collect your cash")
        BALANCE=BALANCE-amount
        print("your remaining balance is",BALANCE)
else:
    print("invalid pin")            
    