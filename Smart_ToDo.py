# smart_todo.py

# List to store all tasks
tasks = []


# Function to add a new task
def add_task(description, priority=None):
    """
    Adds a new task with a description and optional priority.
    If no priority is provided, it defaults to 'Low'.
    """
    if not priority:  # if user doesn't enter anything
        priority = "Low"
    else:
        priority = priority.capitalize()

    if priority not in ["High", "Medium", "Low"]:
        print("⚠️ Invalid priority. Setting it to 'Low' by default.")
        priority = "Low"

    task = {
        "description": description,
        "priority": priority,
        "done": False
    }
    tasks.append(task)
    print(f"\n✅ Task Added: '{description}' [Priority: {priority}]")


# Function to display all tasks
def display_tasks():
    if not tasks:
        print("\n📭 No tasks added yet.")
        return

    # Sort tasks by priority order
    sorted_tasks = sorted(tasks, key=lambda x: ["High", "Medium", "Low"].index(x["priority"]))

    print("\n📝 Smart To-Do List:")
    for i, task in enumerate(sorted_tasks, 1):
        status = "✅ Done" if task["done"] else "❌ Pending"
        print(f"{i}. [{task['priority']}] {task['description']} - {status}")


# Function to mark task as completed
# Function to mark task as completed
def complete_task(index):
    if 0 < index <= len(tasks):
        task = tasks[index - 1]
        task["done"] = True
        print(f"🎉 Task marked as completed: '{task['description']}'")
    else:
        print("⚠️ Invalid task number!")


# Function to delete task
def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"🗑️ Task deleted: '{removed['description']}'")
    else:
        print("⚠️ Invalid task number!")


# Main loop
def main():
    while True:
        print("\n--- Smart To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            desc = input("Enter task description: ").strip()
            priority = input("Enter priority (High / Medium / Low) [Press Enter to set as Low]: ").strip()
            add_task(desc, priority)

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            if not tasks:
                print("⚠️ No tasks to complete.")
            else:
                try:
                    task_num = int(input("Enter task number to mark as complete: "))
                    complete_task(task_num)
                except ValueError:
                    print("⚠️ Please enter a valid number.")

        elif choice == "4":
            if not tasks:
                print("⚠️ No tasks to delete.")
            else:
                try:
                    task_num = int(input("Enter task number to delete: "))
                    delete_task(task_num)
                except ValueError:
                    print("⚠️ Please enter a valid number.")

        elif choice == "5":
            print("👋 Goodbye! Stay productive!")
            break

        else:
            print("⚠️ Invalid option. Please try again.")


# Run the application
if __name__ == "__main__":
    main()
