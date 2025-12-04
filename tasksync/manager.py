from .models import Task
from . import storage
import logging

class TaskManager:

    def __init__(self):
        logging.info("Initializing task manager.")
        self.__tasks = storage.load_data()

    def getTasks(self):
        return list(self.__tasks)

    def addTask(self, name, project):
        logging.info("Adding task.")
        if not isinstance(name, str):
            raise TypeError("Task name should be a string.")
        if not isinstance(project, str) and project is not None:
            raise TypeError("Task project should either be None or a string.")
        
        if len(name) == 0:
            raise ValueError("Task name should have a length.")

        for task in self.__tasks:
            if task.name == name:
                raise ValueError("Another task with the same name already exists.")

        logging.info("Task added to local list variable.")
        self.__tasks.append(Task(name, project, False))

        conn = storage.get_connection()
        db = conn.cursor()

        db.execute(
            "INSERT INTO tasks (name, project, done) VALUES (?, ?, ?)",
            (name, project, 0)
        )

        conn.commit()
        conn.close()

        logging.info("Task added to the database.")
    
    def markTaskDone(self, name):
        logging.info("Marking task as done.")
        if not isinstance(name, str):
            raise TypeError("Task name should be a string.")
        
        found = False
        
        for task in self.__tasks:
            if task.name == name:
                task.done = True
                found = True
                logging.info("Task marked as done in local list variable.")
                break

        if not found:
            raise LookupError("Task not found.")
        
        conn = storage.get_connection()
        db = conn.cursor()

        db.execute(
            "UPDATE tasks SET done=1 WHERE name=?",
            (name,)
        )

        conn.commit()
        conn.close()

        logging.info("Task marked as done in the database.")

    def deleteTask(self, name):
        if not isinstance(name, str):
            raise TypeError("Task name should be a string.")
        
        found = False

        for i, task in enumerate(self.__tasks):
            if task.name == name:
                found = True
                self.__tasks.pop(i)
                logging.info("Task deleted from local list variable.")
                break
                
        if not found:
            raise LookupError("Task not found.")
        
        conn = storage.get_connection()
        db = conn.cursor()

        db.execute("DELETE FROM tasks WHERE name=?", (name,))

        conn.commit()
        conn.close()

        logging.info("Task deleted from the database.")

    def SortTasks(self):
        logging.info("Sorting tasks.")

        self.__tasks.sort(key=lambda t: t.name)
        logging.info("Tasks sorted in local list variable.")

        conn = storage.get_connection()
        db = conn.cursor()

        db.execute("SELECT name, project, done FROM tasks ORDER BY name ASC;")

        conn.commit()
        conn.close()

        logging.info("Tasks sorted in the database.")
