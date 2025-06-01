# Prompt for task details
Task = input("Enter the task description: ")
Priority = input("Enter the task's priority (high, medium, low): ").lower()
Time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task using match-case (Python 3.10+)
match priority:
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is of LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

# Add time-bound urgency if applicable
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Output the reminder
print(reminder)
