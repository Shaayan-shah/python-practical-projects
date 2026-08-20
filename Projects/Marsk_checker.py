# input user marks (5 subject)
#Calc total , average , grades

sub1=int(input("Enter marks for sub_1: "))
sub2=int(input("Enter marks for sub_2: "))
sub3=int(input("Enter marks for sub_3: "))
sub4=int(input("Enter marks for sub_4: "))
sub5=int(input("Enter marks for sub_5: "))

total=sub1 + sub2 + sub3 + sub4 + sub5
average=(total/500)*100

print("Total marks = ",total)
print("Average marks = ",average)

if average>=90:
    print("Pass ! Grade A1.")
elif average<90 and average>80:
    print("Grade B")
elif average <80 and average >75:
    print("Grade C.")
elif average <75 and average >65:
    print("Grade D.")
elif average <65 and average >40:
    print("Grade E.")
elif average > 100 and average < 0:
    print("Enter Valid input.")
else:
    print("Fail! Try next year.")
