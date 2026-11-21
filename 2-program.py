#swapping of two numbers

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

a = num1
b = num2
temp = a

# Swap the values of a and b
a = b
b = temp

# Display the swapped values
print(f"After swapping: First number = {a}, Second number = {b}")