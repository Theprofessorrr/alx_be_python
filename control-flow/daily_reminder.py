# Prompt for a Single Task
# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority
match priority.lower():
    case "high" | "medium" | "low":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
    case _:
        reminder = f"Reminder: '{task}' is a {priority} priority task"

# Check for time-bound
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"

# Print the reminder
print(reminder)

