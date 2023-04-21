PIN="1900" # user pin
BALANCE=250000  # user balance

print("please insert your card")
userinput= input("please enter your 4 digit secret number")
if PIN ==userinput:
    print("your PIN is correct")
    print("press 1 to check balance ")
    print("press 2 to withdraw")
    print("press 3 to transfer")
    print("Press 0 to cancel transaction")
    x= 1
    while x!= 0:
        x= int(input("Enter transaction"))
        if x == 1:
            print(f"Your account balance is {BALANCE}")
        if x==2:
            useramount=int(input("enter amount"))
            #subtract amount from balance
            BALANCE= BALANCE- useramount
            print("Please take your cash")




else:
    print("invalid PIN")
