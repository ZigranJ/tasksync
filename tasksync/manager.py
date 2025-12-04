from .models import Task
from . import storage

class TaskManager:

    def __init__(self):
        self.__tasks = []

    def getTasks(self):
        return self.__tasks

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

    def SortTasks(self):
        self.__tasks.sort(key=lambda t: t.name)
        pass

    def saveTasks(self, filePath):
        try:
            storage.save_data(filePath, self.__tasks)
        except Exception:
            raise

    def loadTasks(self, filePath):
        try:
            self.__tasks = storage.load_data(filePath)
        except Exception:
            raise