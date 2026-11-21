#program to find roots of a quadratic equation

# Prompt the user to enter coefficients a, b, and c
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b ** 2 - 4 * a * c

# Check the nature of the roots based on the discriminant
if discriminant > 0:
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f"The roots are real and different: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"The roots are real and the same: {root}")
else:
    real_part = -b / (2 * a)
    imaginary_part = (abs(discriminant) ** 0.5) / (2 * a)
    print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

