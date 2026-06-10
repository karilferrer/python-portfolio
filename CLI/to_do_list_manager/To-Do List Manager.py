tasks = []

def add_task():
    task = input("Enter task: ")

    tasks.append({
        'task' : task,
        'completed' : False
    })

    print("Task added successfully!")

def view_task():
    if len(tasks) == 0:
        print("No tasks found.")
        return
    
    print("==== TASKS ====")
    
    for index, task in enumerate(tasks, start=1):
        if task['completed'] == False:
            print(f"{index}. {task['task']} [Pending]")
        else:
            print(f"{index}. {task['task']} [Completed]")

def mark_task():
    try:
        task_number = int(input("Enter task number: "))
    except ValueError:
        print("Invalid choice.")
        return

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print("Task marked as completed!")
    else:
        print("Task not found.")

def edit_task():
    try:
        number = int(input("Enter task number: "))
    except ValueError:
        print("Invalid choice. Please try again.")
        return

    for index, task in enumerate(tasks, start=1):
        if index == number:
            new_task = input("Enter new task: ")
            task['task'] = new_task
            print("Task updated successfully!")
            return

def delete_task():
    try:
        number = int(input("Enter task number: "))
    except ValueError:
        print("Invalid choice.")
        return

    if 1 <= number <= len(tasks):
        del tasks[number - 1]
        print("Task deleted successfully!")
    else:
        print("Task not found.")

while True:
    print("==== TO-DO LIST MANAGER ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()

    elif choice == '2':
        view_task()

    elif choice == '3':
        mark_task()

    elif choice == '4':
        edit_task()

    elif choice == '5':
        delete_task()

    elif choice == '6':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")