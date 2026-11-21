# Prompt the user to enter the coordinates of the three vertices
x1, y1 = map(int, input("Enter the coordinates of the first vertex (x1 y1): ").split())
x2, y2 = map(int, input("Enter the coordinates of the second vertex (x2 y2): ").split())
x3, y3 = map(int, input("Enter the coordinates of the third vertex (x3 y3): ").split())

# Calculate the coordinates of the fourth vertex
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

# Display the coordinates of the fourth vertex
print(f"The coordinates of the fourth vertex are: ({x4}, {y4})") 