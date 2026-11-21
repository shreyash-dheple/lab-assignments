#program to delete characters at postion divided by 3 from a string

# Prompt the user to enter a string
user_string = input("Enter a string: ")

# create a new string by excluding characters at positions that are multiples of 3
new_string = ''.join([char for index, char in enumerate(user_string) if (index + 1) % 3 != 0])

# Display the new string
print(f"The new string after deleting characters at positions divisible by 3 is: {new_string}")