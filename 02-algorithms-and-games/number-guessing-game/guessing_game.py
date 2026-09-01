#Random Number guess game 
import random

#Starting attempts
attempts=0
#Maximum attempts
attempt=5
#Computer taking random number
num=random.randint(1,10)


#Using loop until attempts end or guess right one

while attempts<attempt:
    print("+"*35)
    #Taking user input (guessed number)
    user_input=int(input("Guess number (1-100): "))
    print("+"*35)
                
    #Checking different conditions
    if user_input>100 or user_input<0:
        print("invalid input!!! Guess between (1-100)")
        
    elif user_input>num:
        print("Number is too high! guess low.")
        
        print("You have attempts left:",attempt)
    elif user_input<num:
        print("Number is too low! Guess high.")
        
        print("You have attempts left:",attempt)
    elif user_input==num:
        print("Congratulation! 🎉 You guess right one",num)
        

        print("You guess in attempts=",attempts)
        break

    #Checking attempts left        
    attempts+=1
    print("attempt left =",attempt-attempts)
else:
    print("You have no attempts left.")
        # 4. Number Guessing Game (Advanced Version)
        # What to build:
        # Random number (1–100)
        # User keeps guessing
        # Add:
        # Attempt counter
        # Limit attempts
        # Give hints (Too High / Too Low)
        # Challenge:
        # Add difficulty levels