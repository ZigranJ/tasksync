from .models import Task
import os
import json

def is_valid_file_path(path):
    if not path or not isinstance(path, str):
        return False
    
    path = os.path.normpath(path)
    directory = os.path.dirname(path)
    filename = os.path.basename(path)

    if not filename or filename.endswith(os.sep):
        return False
    
    if directory == "":
        directory = "."

    return os.path.isdir(directory)

def task_to_dict(task):
    if not isinstance(task, Task):
        raise TypeError("task should be a Task.")

    return {
        "name": task.name,
        "project": task.project,
        "done": task.done
    }

def dict_to_task(taskDict):
    if not isinstance(taskDict, dict):
        raise TypeError("taskDict should be a dict.")

    return Task(taskDict["name"], taskDict["project"], taskDict["done"])

def load_data(filePath):
    if not isinstance(filePath, str):
        raise TypeError("filePath should be a string.")
    
    if not is_valid_file_path(filePath):
        raise ValueError("filePath should be a valid file path.")
    
    tasks_dict = []

    try:
        with open(filePath, "r") as file:
            tasks_dict = json.load(file)
    except FileNotFoundError as err:
        raise err
    except PermissionError as err:
        raise err
    except IsADirectoryError as err:
        raise err
    except OSError as err:
        raise err
    
    tasks = []

    for task_dict in tasks_dict:
        tasks.append(dict_to_task(task_dict))

    return tasks

def save_data(filePath, tasks):
    if not isinstance(filePath, str):
        raise TypeError("filePath should be a string.")
    
    if not isinstance(tasks, list):
        raise TypeError("tasks should be a list.")
    
    if len(tasks) != 0:
        if not isinstance(tasks[0], Task):
            raise TypeError("tasks should be a list of Tasks.")
        
    if not is_valid_file_path(filePath):
        raise ValueError("filePath should be a valid file path.")
    
    tasks_dicts = []
    for task in tasks:
        tasks_dicts.append(task_to_dict(task))

    try:
        with open(filePath, "w") as file:
            json.dump(tasks_dicts, file, indent = 2)
    except FileNotFoundError as err:
        raise err
    except PermissionError as err:
        raise err
    except IsADirectoryError as err:
        raise err
    except OSError as err:
        raise err