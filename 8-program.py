import math
# Prompt the user to enter the number of students in each of the three classes
class_1 = int(input("Enter the number of students in the first class: "))
class_2 = int(input("Enter the number of students in the second class: "))
class_3 = int(input("Enter the number of students in the third class: "))

# Calculate the number of desks needed for each class and use math.ceil to round up to the nearest whole number
desks_class_1 = math.ceil(class_1 / 2)
desks_class_2 = math.ceil(class_2 / 2)
desks_class_3 = math.ceil(class_3 / 2)

# Calculate the total number of desks needed
total_desks = desks_class_1 + desks_class_2 + desks_class_3

# Display the total number of desks needed
print(f"The total number of desks needed for the three classes is: {total_desks}") 