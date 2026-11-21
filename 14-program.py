#Program to check if a date is valid.

# Prompt the user to enter a date

day = int(input("Enter the day (1-31): "))
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

#Display the result
if (month >= 1 and month <= 12) and (day >= 1 and day <= 31):
    if month in [4, 6, 9, 11] and day <= 30:
        print(f"The date {day}/{month}/{year} is valid.")
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day <= 29:
                print(f"The date {day}/{month}/{year} is valid.")
            else:
                print("The date is invalid.")
        else:
            if day <= 28:
                print(f"The date {day}/{month}/{year} is valid.")
            else:
                print("The date is invalid.")
    else:
        print(f"The date {day}/{month}/{year} is valid.") 





