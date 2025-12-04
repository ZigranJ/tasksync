from .models import Task
from . import storage

class TaskManager:

    def __init__(self):
        self.__tasks = storage.load_data()

    def getTasks(self):
        return list(self.__tasks)

    def addTask(self, name, project):
        if not isinstance(name, str):
            raise TypeError("Task name should be a string.")
        if not isinstance(project, str) and project is not None:
            raise TypeError("Task project should either be None or a string.")
        
        if len(name) == 0:
            raise ValueError("Task name should have a length.")

        for task in self.__tasks:
            if task.name == name:
                raise ValueError("Another task with the same name already exists.")

        self.__tasks.append(Task(name, project, False))

        conn = storage.get_connection()
        db = conn.cursor()

        db.execute(
            "INSERT INTO tasks (name, project, done) VALUES (?, ?, ?)",
            (name, project, 0)
        )

        conn.commit()
        conn.close()
    
    def markTaskDone(self, name):
        if not isinstance(name, str):
            raise TypeError("Task name should be a string.")
        
        found = False
        
        for task in self.__tasks:
            if task.name == name:
                task.done = True
                found = True

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

    def deleteTask(self, name):
        if not isinstance(name, str):
            raise TypeError("Task name should be a string.")
        
        found = False

        for i, task in enumerate(self.__tasks):
            if task.name == name:
                found = True
                self.__tasks.pop(i)
                break
                
        if not found:
            raise LookupError("Task not found.")
        
        conn = storage.get_connection()
        db = conn.cursor()

        db.execute("DELETE FROM tasks WHERE name=?", (name,))

        conn.commit()
        conn.close()

    def SortTasks(self):
        self.__tasks.sort(key=lambda t: t.name)
        pass
