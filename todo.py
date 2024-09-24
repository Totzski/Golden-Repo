import os
import json

class ToDoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()
        print(f"Added task: {task}")

    def remove_task(self, index):
        try:
            task = self.tasks.pop(index)
            self.save_tasks()
            print(f"Removed task: {task['task']}")
        except IndexError:
            print("Task not found.")

    def complete_task(self, index):
        try:
            self.tasks[index]['done'] = True
            self.save_tasks()
            print(f"Completed task: {self.tasks[index]['task']}")
        except IndexError:
            print("Task not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "✔️" if task['done'] else "❌"
                print(f"{i + 1}. {task['task']} [{status}]")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Complete a task")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            todo_list.list_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
