import math

# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle using the formula: area = π * r^2
area = math.pi * radius ** 2

#display the area of the circle
print(f"The area of the circle with radius {radius} is: {area:.2f}")