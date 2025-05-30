# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build the base reminder message
reminder = f"Reminder: '{task}' is a"

# Use match-case to handle priority level
match priority:
    case "high":
        reminder += " high priority task"
    case "medium":
        reminder += " medium priority task"
    case "low":
        reminder += " low priority task"
    case _:
        reminder += " task with unknown priority"

# Add time-bound message if applicable
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
# Print the final reminder
print("\n" + reminder)

