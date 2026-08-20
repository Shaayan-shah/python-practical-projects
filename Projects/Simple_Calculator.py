#Simple Calculator 
'''What to build:
Input: two numbers + operator (+, -, *, /)
Perform calculation

Make it better:
Use loop so it runs continuously
Add functions for each operation

Challenge:
Handle division by zero'''
#Handle zero division error
try:
    #Using loop for countinivity 
    while True:
        #Taking input from user 
        num1=float(input("Enter First number: ")) 
        op=(input("Enter Operator(+ , - , * , /) : "))
        num2=float(input("Enter second number: "))
        #Checking conditions
        if op=="+":
            print("The sum is =",num1 + num2)
        elif op=="-":
            print("The substractoin is =",num1 - num2)
        elif op=="*":
            print("The multiplication is =",num1 * num2)
        elif op=="/":
            print("The division is =",num1 / num2)
        
        else:
            print("Enter valid Operator.")
    
except ZeroDivisionError:
    print("The number cannot be zero(0).")
    
    
    