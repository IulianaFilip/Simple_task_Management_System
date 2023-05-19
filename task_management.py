import json


TASKS_FILE = "tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)


def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = input("Enter task status: ")
    due_date = input("Enter task due date: ")

    task = {
        "title": title,
        "description": description,
        "status": status,
        "due_date": due_date
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task created successfully!")


def view_all_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} ({task['status']})")


def view_task_details():
    title = input("Enter task title: ")
    task = find_task_by_title(title)
    if task:
        print("Task Details:")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Due Date: {task['due_date']}")
    else:
        print("Task not found.")


def update_task():
    title = input("Enter task title: ")
    task = find_task_by_title(title)
    if task:
        print("Update Task:")
        print("1. Update status")
        print("2. Update due date")
        choice = input("Enter your choice: ")
        if choice == "1":
            new_status = input("Enter new status: ")
            task["status"] = new_status
            save_tasks(tasks)
            print("Task updated successfully!")
        elif choice == "2":
            new_due_date = input("Enter new due date: ")
            task["due_date"] = new_due_date
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid choice.")
    else:
        print("Task not found.")


def delete_task():
    title = input("Enter task title: ")
    task = find_task_by_title(title)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Task not found.")


def find_task_by_title(title):
    for task in tasks:
        if task["title"] == title:
            return task
    return None

