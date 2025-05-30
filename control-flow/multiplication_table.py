# Ask the user to enter a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Print the multiplication table from 1 to 10
print(f"\n📘 Multiplication Table for {number}:\n")

for i in range(1, 11):  # Loop from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")
