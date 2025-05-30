task = input("Enter your task: ")
priority = input("Enter task priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Process priority using match-case
match priority:
    case "high":
        priority_message = "This is a HIGH priority task"
    case "medium":
        priority_message = "This is a MEDIUM priority task"
    case "low":
        priority_message = "This is a LOW priority task"
    case _:
        priority_message = "Priority level not specified"

# Add time sensitivity message
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "that can be scheduled as needed."

# Print the complete reminder
print(f"\nREMINDER: {priority_message} - {task} {time_message}") 