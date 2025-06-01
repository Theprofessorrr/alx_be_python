# Prompt for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Normalize input
priority = priority.lower()
time_bound = time_bound.lower()

# Match case for priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' is a task with unspecified priority"

# Append if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"

# ✅ Print must start with `print(f"Reminder:`
print(f"{message}")
