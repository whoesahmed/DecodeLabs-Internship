def add_task(tasks):
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def main():
    tasks = []
    print("======= Welcome to your To-Do List =======\n")

    while True:
        choice = input("Choose an option (1: Add, 2: View, 3: Quit): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye! Your tasks are cleared from memory.")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()