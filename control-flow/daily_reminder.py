# Ask the user for task details
task = input("Enter your task: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Base reminder message
reminder = f"Task: {task}\nPriority: {priority.capitalize()}"

# Use match-case to handle different priority levels
match priority:
    case "high":
        reminder += "\nThis is a high-priority task!"
    case "medium":
        reminder += "\nThis task has medium priority."
    case "low":
        reminder += "\nThis is a low-priority task."
    case _:
        reminder += "\nUnknown priority level."

# Use if-statement to handle time sensitivity
if time_bound == "yes":
    reminder += "It requires immediate attention today!"

# Print the final reminder
print("\n" + reminder)
