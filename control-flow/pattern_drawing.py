# Ask the user for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
    exit()

# Initialize the row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print each row's asterisks
    for col in range(size):
        print("*", end="")  # Print * without moving to the next line
    print()  # Move to the next line after each row
    row += 1
