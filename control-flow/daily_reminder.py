# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Base reminder message
reminder = f"Task: {task}\nPriority: {priority.capitalize()}"

# Use match-case to handle different priority levels
match priority:
    case "high":
        reminder += "\nThis is a high-priority task!"
    case "medium":
        reminder += "\nThis task has medium priority"
    case "low":
        reminder += "\nThis is a low-priority task"
    case _:
        reminder += "\nUnknown priority level"

# Use if-statement to handle time sensitivity
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "Consider completing it when you have free time."

# Print the final reminder
print("\n" + reminder)
