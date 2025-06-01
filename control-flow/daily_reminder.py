# Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the task’s priority (high, medium, low): ")
time_bound = input("Is the task time-bound (yes or no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority.lower():
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is of LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

# Check for time-bound
if time_bound.lower() == "yes":
    reminder += " That requires immediate attention today!"

# Provide the customized reminder
print(reminder)
