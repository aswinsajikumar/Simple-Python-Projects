print("📝 Simple To-Do List")

tasks = []

while True:
    print("\nOptions:")
    print("1 - Add task")
    print("2 - View tasks")
    print("3 - Mark task as done")
    print("4 - Exit")

    choice = input("Enter option (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                status = "✅" if t["done"] else "❌"
                print(f"{i}. {t['task']} [{status}]")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark done.")
        else:
            for i, t in enumerate(tasks, 1):
                status = "✅" if t["done"] else "❌"
                print(f"{i}. {t['task']} [{status}]")
            task_num = int(input("Enter task number to mark done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
                print(f"Task {task_num} marked as done!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
