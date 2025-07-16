class Task:
    def __init__(self, id, title, description, priority, status):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description, priority, status):
        task = Task(self.next_id, title, description, priority, status)
        self.tasks.append(task)
        self.next_id += 1
        print("Task added successfully!")

    def edit_task(self, id, title, description, priority, status):
        task = self.get_task_by_id(id)
        if task:
            task.title = title
            task.description = description
            task.priority = priority
            task.status = status
            print("Task updated successfully!")
        else:
            print("Task not found!")

    def delete_task(self, id):
        task = self.get_task_by_id(id)
        if task:
            self.tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Task not found!")

    def get_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = [task for task in self.tasks if task.priority == priority]
        if not filtered_tasks:
            print(f"No tasks with priority {priority}.")
        else:
            for task in filtered_tasks:
                print(task)


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            status = input("Enter task status (Pending/In Progress/Completed): ")
            task_manager.add_task(title, description, priority, status)
        elif choice == '2':
            try:
                id = int(input("Enter task ID to edit: "))
                title = input("Enter new task title: ")
                description = input("Enter new task description: ")
                priority = input("Enter new task priority (High/Medium/Low): ")
                status = input("Enter new task status (Pending/In Progress/Completed): ")
                task_manager.edit_task(id, title, description, priority, status)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '3':
            try:
                id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '4':
            task_manager.view_all_tasks()
        elif choice == '5':
            priority = input("Enter priority to filter by (High/Medium/Low): ")
            task_manager.filter_tasks_by_priority(priority)
        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()


# Explanation:
# Task Class: Represents a task with attributes id, title, description, priority, and status. The __str__ method provides a string representation of the task.
# TaskManager Class: Manages a list of tasks. It includes methods to add, edit, delete, view, and filter tasks. The next_id attribute ensures unique task IDs.
# Main Function: Provides a command-line interface for user interaction. It presents a menu with options to add, edit, delete, view, and filter tasks. It handles user input and calls the appropriate methods from the TaskManager class.
# Error Handling: Checks for invalid task IDs and ensures priority and status values are correct. Provides feedback for invalid inputs.
