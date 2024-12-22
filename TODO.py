
def show_menu():
    print("\nMENU")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("The task has been added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"The task '{removed_task}' has been deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def main():
    tasks = []  # List to store tasks
    while True:
        choice = show_menu()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting the program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
