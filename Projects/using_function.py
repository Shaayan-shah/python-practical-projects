

def sum():
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    sum=num1+num2
    return sum

def subtraction():
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    subtraction=num1-num2
    return subtraction

def multiplication():
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    multiplication=num1*num2
    return multiplication

def division():
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    division=num1/num2
    return division
try:
    while True:
        user_input=input("Enter 'start' or 'exit': ")
        if user_input.lower()=="start":
            op=input("Enter operator(+ , - , * , /) :")
            if op=="+":
                sum=sum()
                print("The sum is =",sum)
            elif op=="-":
                sub=subtraction()
                print("The subtraction is =",sub)
            elif op=="*":
                mul=multiplication()
                print("The multiplication is =",mul)
            elif op=="/":
                div=division()
                print("The division is =",round(div,2))
            else:
                print("Enter valid operstor.")
        elif user_input.lower()=="exit":
            print("Bye! Have a nice day.")
        else:
            print("Enter Valid input.")
except ZeroDivisionError:
    print("The number should not be zero(0).")