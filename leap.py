leap_year = int(input("Enter a year: "))

if(leap_year %4 == 0 and leap_year %100 != 0) or (leap_year %400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
