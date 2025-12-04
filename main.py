import tasksync.manager

task_manager = tasksync.manager.TaskManager()

while True:
    cmd = input("> ")
    if cmd == "add":
        name = input("Task name: ")
        project = input("Project: ")
        try:
            task_manager.addTask(name, project)
            print("Task added!")
        except TypeError as err:
            print("Error:", err)
        except ValueError as err:
            print("Error:", err)
    elif cmd == "list":
        tasks = task_manager.getTasks()
        for task in tasks:
            doneMark = ' '
            projectSign = ""
            if task.done:
                doneMark = '✓'
            if len(task.project) != 0:
                projectSign = f" ({task.project})"
            print(f"[{doneMark}] {task.name}{projectSign}")
    elif cmd == "done":
        name = input("Task name: ")
        try:
            task_manager.markTaskDone(name)
        except TypeError as err:
            print("Error:", err)
        except LookupError as err:
            print("Error:", err)
    elif cmd == "delete":
        name = input("Task name: ")
        try:
            task_manager.deleteTask(name)
        except TypeError as err:
            print("Error:", err)
        except LookupError as err:
            print("Error:", err)
    elif cmd == "exit":
        break
    elif cmd == "help":
        print("All commands in tasksync:")
        print("add - adds a task")
        print("list - lists all tasks")
        print("done - mark a task as done")
        print("delete - delete a task")
        print("exit - exit the program")
        print("help - print this help screen")
        print("save - save tasks into a file")
        print("load - load tasks from a file")
    elif cmd == "save":
        filePath = input("File path: ")
        try:
            task_manager.saveTasks(filePath)
        except TypeError as err:
            print("Error:", err)
        except ValueError as err:
            print("Error:", err)
        except FileNotFoundError as err:
            print("Error:", err)
        except PermissionError as err:
            print("Error:", err)
        except IsADirectoryError as err:
            print("Error:", err)
        except OSError as err:
            print("Error:", err)
    elif cmd == "load":
        filePath = input("File path: ")
        try:
            task_manager.loadTasks(filePath)
        except TypeError as err:
            print("Error:", err)
        except ValueError as err:
            print("Error:", err)
        except FileNotFoundError as err:
            print("Error:", err)
        except PermissionError as err:
            print("Error:", err)
        except IsADirectoryError as err:
            print("Error:", err)
        except OSError as err:
            print("Error:", err)
    else:
        print("Invalid command.")
