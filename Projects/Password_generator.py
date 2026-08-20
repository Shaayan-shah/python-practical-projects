# Generate random strong password
import random
import string

lenght = int(input("Enter the length of password: "))
password = string.ascii_letters + string.digits + string.punctuation
# print(password)

password_generator = ""
for i in range(lenght):
    password_generator += random.choice(password)

print("Your random password =", password_generator)
