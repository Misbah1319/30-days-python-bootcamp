# Daily Task Checklist
# This program helps track completed and incomplete tasks
# Created as part of a 30-day Python bootcamp

# List to store all tasks
checklist = []

print("Enter your daily tasks.")
print("Type 'done' when you finish adding tasks.\n")

# Loop to add tasks
while True:
    task = input("Add task: ")

    # Stop taking input if user types 'done'
    if task.lower() == "done":
        break

    checklist.append(task)

# Lists to store completed and incomplete tasks
completed_tasks = []
incomplete_tasks = []

print("\nNow mark each task as completed or not.\n")

# Loop through each task
for task in checklist:
    status = input(f"Did you complete '{task}'? (yes/no): ")

    if status.lower() == "yes":
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

# Display the result
print("\n----- Daily Task Summary -----")

print("\nCompleted Tasks:")
if completed_tasks:
    for task in completed_tasks:
        print("-", task)
else:
    print("No tasks completed.")

print("\nIncomplete Tasks:")
if incomplete_tasks:
    for task in incomplete_tasks:
        print("-", task)
else:
    print("No incomplete tasks.")

