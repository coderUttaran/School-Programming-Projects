tasks = []

def show_tasks():
    if not tasks:
        print("No Tasks found")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def add_task():
    task = input("\nEnter task to add: ")
    if task in tasks:
        print(f"\n{task} is already added")
    else:
        tasks.append(task)
        print("Task Added")
        show_tasks()

def remove_task():
    if tasks:
        show_tasks()
        ind = int(input("Enter task no. to delete: "))
        try:
            tasks.pop(ind-1)
            print("\nUpdated Tasks:")
            show_tasks()

        except (ValueError, IndexError):
            print("Invalid Input")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


while True:
    show_menu()
    
    try:
        choice = int(input("Enter Your choice (1, 2, 3, 4): "))
        if choice == 1:
            add_task()
        elif choice == 2:
            show_tasks()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid Input")
    except ValueError:
        print("Invalid Input")
