#ATM Machine 
print("*----------Welcome To ATM----------*")

balance=5000
pin=1901

password=int(input("Enter your pin: "))

if password==pin:

    menu=("""    1. Balance Check
    2. Deposite Balance
    3. Withdrawal Balance 
    4. Exit""")
    while True:
        print(menu)
        user_input=input(f"Enter choice to continue: ")
        

        if user_input=="1":
            print("The available balance is= ",balance)
        elif user_input=="2":
            amount1=float(input("Enter amount to deposite: "))
            if amount1<=0:
                print("Please enter valid balance to deposite!!!")
            else:
                balance+=amount1
            print(f"The amount {amount1} has deposited succesfully.")
        elif user_input=="3":
            amount2=float(input("Enter amount to withdrawal: "))
            if amount2<=balance:
                print(f"The amount of {amount2} has been withrawal succesfully.")
                balance-=amount2
            elif amount2<=0:
                print("Enter valid value to withdrawal")
            else:
                print("Sorry! Insufficient balance..")
                print("The available balance is =",balance)
        elif user_input=="4":
            print("Thank you for visiting!!")
            break
        else:
            print("Enter valid Option(1 , 2 , 3 , 4): ")
else:
    print("Incorrect password! Try again.")