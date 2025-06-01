# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority.lower():
    case "high":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
    case _:
        reminder = f"Reminder: '{task}' is a {priority} priority task"

# Check for time-bound
if time_bound.lower() == "yes":
    reminder += " That requires immediate attention today!"

# Provide the customized reminder
print(reminder)


# Create reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"

