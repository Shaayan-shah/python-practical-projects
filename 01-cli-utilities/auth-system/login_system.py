#LOG IN SYSTEM

user_name="admin"
password="1234"

attempts=3

while attempts > 0:
    user_input=input("Enter user name: ")
    p_word=input("Enter password: ")

    if user_input==user_input and password==p_word:
        print("Access granted successfully.")
        break
    else:
        print("Wrong user name or password.")
        attempts-=1
        print("Try agian in ",attempts)

else:
    print("Acount locked due to too many attempts.")