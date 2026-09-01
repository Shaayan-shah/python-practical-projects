#Check that use can vote or not 

age=int(input("Enter your age: "))
citizen=input("Citizen (yes/no): ")

if age>=18 and citizen.lower()=="yes":
    print("You are eligible for voting.")
elif age<18:
    print("You are underage. Not eligible.")
else:
    print("Not eligible.")