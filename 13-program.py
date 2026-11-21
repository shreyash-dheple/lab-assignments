#program to determine if the year is a leap year or not

# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year and display the result
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")

