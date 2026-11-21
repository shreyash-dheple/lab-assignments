# Prompt the user to enter the total number of cards (N)
N = int(input("Enter the total number of cards (N): "))

# Prompt the user to enter the numbers on the remaining cards
remaining_cards = list(map(int, input(f"Enter the numbers on the remaining {N - 1} cards (space-separated): ").split()))

# Calculate the expected sum of numbers from 1 to N
expected_sum = N * (N + 1) // 2

# Calculate the actual sum of the remaining cards
actual_sum = sum(remaining_cards)

# The lost card number is the difference between the expected sum and the actual sum
lost_card = expected_sum - actual_sum

# Display the number on the lost card
print(f"The number on the lost card is: {lost_card}")