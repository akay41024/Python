sub1 = int(input("Enter the marks of the first subject: "))
sub2 = int(input("Enter the marks of the second subject: "))
sub3 = int(input("Enter the marks of the third subject: "))
sub4 = int(input("Enter the marks of the fourth subject: "))
sub5 = int(input("Enter the marks of the fifth subject: "))

total = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total / 500) * 100

if 90 <= percentage <= 100:
    print("Grade A")
elif 80 <= percentage < 90:
    print("Grade B")
elif 60 <= percentage < 80:
    print("Grade C")
elif 50 <= percentage < 60:
    print("Grade D")
elif 40 <= percentage < 50:
    print("Grade E")
elif percentage < 40:
    print("Grade F")
else:
    print("Invalid Percentage")


print("Total Marks: ", total)
print("Percentage: ", percentage)
