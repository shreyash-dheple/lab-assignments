# Accept the number of pins and balls
N = int(input())
K = int(input())

# Initially, all pins are standing
pins = ['I'] * N

# Process each ball
for _ in range(K):
    start, stop = map(int, input().split())

    # Mark all pins knocked down by this ball
    for i in range(start - 1, stop):
        pins[i] = '.'

# Display the final arrangement of pins
print(''.join(pins)) 
