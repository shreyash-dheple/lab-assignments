#program to convert kilometers to miles

# Prompt the user to enter a distance in kilometers
kilometers = float(input("Enter the distance in kilometers: "))

# Conversion factor from kilometers to miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor

# Display the converted distance in miles
print(f"{kilometers} kilometers is equal to {miles:.2f} miles")