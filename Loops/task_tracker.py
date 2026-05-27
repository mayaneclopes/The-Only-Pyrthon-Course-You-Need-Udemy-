# Instructions
# You’re building a simple task tracker for a to-do app. Whenever a user completes tasks, your app should mark them as done.
# Tasks:
# Define a function mark_completed_tasks that accepts a list of task names.
# Iterate through the list using a for loop, and update the format like "Completed:  {task}".
# Return a new list with the updated task strings.

def mark_completed_tasks(tasks: list[str]) -> list[str]:
    completed = []
    for task in tasks:
        completed.append(f"Completed: {task}")
    return completed
