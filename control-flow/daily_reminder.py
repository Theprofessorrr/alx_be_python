# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority
match priority.lower():
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' is a task of unspecified priority"

# Use if statement to modify the reminder if the task is time-bound
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"

# Provide a Customized Reminder
print(reminder)
