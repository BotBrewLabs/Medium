import json
import os
from datetime import datetime

# File to store task data
task_file = 'daily_tasks.json'

def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            stored_data = json.load(file)
            if stored_data.get("date") == datetime.now().strftime("%Y-%m-%d"):
                return stored_data.get("tasks")
    return {
        "Brush Teeth": False,
        "Read a Book": False,
        "Clean Room": False,
        "Clean Coup": False, 
        "Clean pool": False, 
        "Clean dog poop": False, 
        "Feed cats": False, 
        "Feed Dogs": False,
        "Feed animals":  False, 
        "Laundry": False,
        "Clean Dishes": False,
        "Exercise": False,
        "Cut Grasss": False
    }

def save_tasks(tasks):
    with open(task_file, 'w') as file:
        json.dump({"date": datetime.now().strftime("%Y-%m-%d"), "tasks": tasks}, file)

def display_tasks(tasks):
    print("\nToday's Tasks:")
    for task, completed in tasks.items():
        status = "Done" if completed else "Not Done"
        print(f"{task}: {status}")
    print()

def print_report(tasks):
    completed_tasks = [task for task, done in tasks.items() if done]
    pending_tasks = [task for task, done in tasks.items() if not done]
    print("\nTask Report:")
    print("Completed Tasks:")
    for task in completed_tasks:
        print(f"- {task}")
    print("\nPending Tasks:")
    for task in pending_tasks:
        print(f"- {task}")
    print()

def update_task(tasks):
    print("Select a task to mark as completed:")
    task_names = list(tasks.keys())
    for i, task in enumerate(task_names, start=1):
        print(f"{i}. {task}")

    choice = int(input("Enter the task number: ")) - 1
    if 0 <= choice < len(task_names):
        tasks[task_names[choice]] = True
        save_tasks(tasks)
        print(f"Task '{task_names[choice]}' marked as completed!")
    else:
        print("Invalid task number.")

def add_task(tasks):
    new_task = input("Enter the name of the new task: ")
    if new_task not in tasks:
        tasks[new_task] = False
        save_tasks(tasks)
        print(f"Task '{new_task}' added.")
    else:
        print("Task already exists.")

def remove_task(tasks):
    print("Select a task to remove:")
    task_names = list(tasks.keys())
    for i, task in enumerate(task_names, start=1):
        print(f"{i}. {task}")

    choice = int(input("Enter the task number: ")) - 1
    if 0 <= choice < len(task_names):
        del tasks[task_names[choice]]
        save_tasks(tasks)
        print(f"Task '{task_names[choice]}' removed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        display_tasks(tasks)
        print("Options:")
        print("1. Mark a task as completed")
        print("2. Add a new task")
        print("3. Remove a task")
        print("4. Exit and Print Report")
        choice = input("What would you like to do? ")

        if choice == '1':
            update_task(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

    print_report(tasks)

if __name__ == "__main__":
    main()
