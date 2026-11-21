# Prompt the user to enter hours, minutes, and seconds
hours = int(input("Enter hours (0-11): "))
minutes = int(input("Enter minutes (0-59): "))
seconds = int(input("Enter seconds (0-59): "))

# Calculate the angle of the hour hand
angle = (hours * 30) + (minutes * 0.5) + (seconds * (0.5 / 60))

# Display the angle of the hour hand
print(f"The angle of the hour hand is: {angle:.2f} degrees") 
 