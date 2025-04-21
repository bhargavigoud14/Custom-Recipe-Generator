# smart_todo.py

class SmartToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority=None):
        """
        Adds a new task with a description and optional priority.
        If no priority is provided, it defaults to 'Low'.
        """
        if not priority:
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
        self.tasks.append(task)
        print(f"\n✅ Task Added: '{description}' [Priority: {priority}]")

    def display_tasks(self):
        if not self.tasks:
            print("\n📭 No tasks added yet.")
            return

        sorted_tasks = sorted(self.tasks, key=lambda x: ["High", "Medium", "Low"].index(x["priority"]))

        print("\n📝 Smart To-Do List:")
        for i, task in enumerate(sorted_tasks, 1):
            status = "✅ Done" if task["done"] else "❌ Pending"
            print(f"{i}. [{task['priority']}] {task['description']} - {status}")

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            task = self.tasks[index - 1]
            task["done"] = True
            print(f"🎉 Task marked as completed: '{task['description']}'")
        else:
            print("⚠️ Invalid task number!")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"🗑️ Task deleted: '{removed['description']}'")
        else:
            print("⚠️ Invalid task number!")

    def run(self):
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
                self.add_task(desc, priority)

            elif choice == "2":
                self.display_tasks()

            elif choice == "3":
                if not self.tasks:
                    print("⚠️ No tasks to complete.")
                else:
                    try:
                        task_num = int(input("Enter task number to mark as complete: "))
                        self.complete_task(task_num)
                    except ValueError:
                        print("⚠️ Please enter a valid number.")

            elif choice == "4":
                if not self.tasks:
                    print("⚠️ No tasks to delete.")
                else:
                    try:
                        task_num = int(input("Enter task number to delete: "))
                        self.delete_task(task_num)
                    except ValueError:
                        print("⚠️ Please enter a valid number.")

            elif choice == "5":
                print("👋 Goodbye! Stay productive!")
                break

            else:
                print("⚠️ Invalid option. Please try again.")


# Run the application
if __name__ == "__main__":
    app = SmartToDoList()
    app.run()
