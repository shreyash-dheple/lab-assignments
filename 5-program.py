#program to find maximum of two numbers

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers and find the maximum
if num1 > num2:
    maximum = num1
else:
    maximum = num2

# Display the maximum number
print(f"The maximum of {num1} and {num2} is: {maximum}") 