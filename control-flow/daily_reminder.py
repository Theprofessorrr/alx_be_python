# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Normalize input values before match/case
priority = priority.lower()
time_bound = time_bound.lower()

# Match Case on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' is a task of unspecified priority"

# Required format: if time_bound == ...
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Final output
print(reminder)
