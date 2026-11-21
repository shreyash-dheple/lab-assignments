#program to check if integer is positive or negative or zero

# Prompt the user to enter an integer
number = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero and display the result
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number is zero.") 