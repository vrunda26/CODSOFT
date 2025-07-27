todo_list = []
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. [{status}] {task['title']}")

def add_task():
    title = input("Enter the task: ")
    todo_list.append({"title": title, "completed": False})
    print("Task added successfully.")

def complete_task():
    view_tasks()
    try:
        task_no = int(input("Enter the task number to mark complete: ")) - 1
        if 0 <= task_no < len(todo_list):
            todo_list[task_no]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_no < len(todo_list):
            todo_list.pop(task_no)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
