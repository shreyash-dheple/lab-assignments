# Input first timestamp
h1 = int(input("Enter hours: "))
m1 = int(input("Enter minutes: "))
s1 = int(input("Enter seconds: "))

# Input second timestamp
h2 = int(input("Enter hours: "))
m2 = int(input("Enter minutes: "))
s2 = int(input("Enter seconds: "))

# Convert both timestamps into seconds
t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

# Calculate difference
diff = abs(t1 - t2)

# Convert difference back into hours, minutes and seconds
h = diff // 3600
m = (diff % 3600) // 60
s = diff % 60

# Display result
print("Time difference:", h, "hours", m, "minutes", s, "seconds") 
