days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednessday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

day_number = int(input("Enter the day number: "))

if 1<= day_number <= 7:
    print(days[day_number])
else:
    print("Invalid day number")