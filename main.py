import tasksync.manager
import tasksync.storage
import logging

logging.basicConfig(
    level = logging.ERROR,
    format="%(levelname)s - %(message)s"
)

tasksync.storage.init_db()
task_manager = tasksync.manager.TaskManager()

while True:
    cmd = input("> ")
    if cmd == "add":
        name = input("Task name: ")
        project = input("Project: ")
        try:
            task_manager.addTask(name, project)
            logging.info("Task added.")
        except TypeError as err:
            logging.error(err)
        except ValueError as err:
            logging.error(err)
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
            logging.error(err)
        except LookupError as err:
            logging.error(err)
    elif cmd == "delete":
        name = input("Task name: ")
        try:
            task_manager.deleteTask(name)
        except TypeError as err:
            logging.error(err)
        except LookupError as err:
            logging.error(err)
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
        print("sort - sorts tasks alphabetically")
    elif cmd == "sort":
        task_manager.SortTasks()
    else:
        logging.error(err)
