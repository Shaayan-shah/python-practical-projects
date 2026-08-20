#Check that the number is palindrom or not

user_input=list(input("Enter string or number: "))


palindrome=user_input.copy()
palindrome.reverse()


if user_input==palindrome:
    print("The given input is palindrome.")
else:
    print("Not palindrom")

print(str(user_input))
print(str(palindrome))


#The simplist way 

n=input("Enter string: ")

reverse=n[::-1]

if n.lower()==reverse.lower():
    print("Palindrome")
else:
    print("Not palindrome")


