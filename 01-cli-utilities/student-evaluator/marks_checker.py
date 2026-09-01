'''What to build:
Input marks of 3–5 subjects
Calculate:
Total
Percentage
Grade (A/B/C/Fail)
Concepts:
Variables
Conditionals
Functions (later)
Challenge:
Add rule: if any subject < 40 → Fail'''

marks=0

phy=int(input("Enter marks for phy: "))
marks+=phy
chem=int(input("Enter marks for chem: "))
marks+=chem
bio=int(input("Enter marks for bio: "))
marks+=bio
total=marks
average=(marks/300)*100
print("Total =",total)
print("Average =",round(average,2))

if phy<35 or chem <35 or bio<35:
    print("You are fail in single subject!")
elif average<40:
    print("Sorry! Yor are fail.")
else:
    print("Yor are pass.Congratulation🎉")
