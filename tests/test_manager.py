from tasksync.manager import TaskManager
import unittest

class testManager(unittest.TestCase):
    def testDeleteTask(self):
        self.manager = TaskManager()
        tasks = self.manager.getTasks()
        for task in tasks:
            self.manager.deleteTask(task.name)
        tasks = self.manager.getTasks()

        self.assertEqual(len(tasks), 0)
        self.assertRaises(TypeError, self.manager.deleteTask, 123)
        self.assertRaises(LookupError, self.manager.deleteTask, "TaskThatDoesntExist")

    def testAddTask(self):
        self.manager = TaskManager()
        self.manager.addTask("ExampleName", None)
        tasks = self.manager.getTasks()

        found = False
        for task in tasks:
            if task.name == "ExampleName":
                found = True
                break

        self.assertTrue(found)
        self.assertRaises(TypeError, self.manager.addTask, 123, None)
        self.assertRaises(TypeError, self.manager.addTask, "ExampleName", 123)
        self.assertRaises(ValueError, self.manager.addTask, "", None)
        self.assertRaises(ValueError, self.manager.addTask, "ExampleName", None)

    def testMarkTaskAsDone(self):
        self.manager = TaskManager()
        self.manager.addTask("ExampleName", None)
        self.manager.markTaskDone("ExampleName")
        tasks = self.manager.getTasks()

        found = False
        for task in tasks:
            if task.name == "ExampleName" and task.done:
                found = True
                break

        self.assertTrue(found)
        self.assertRaises(TypeError, self.manager.markTaskDone, 123)
        self.assertRaises(LookupError, self.manager.markTaskDone, "TaskThatDoesntExist")

    def testSortTasks(self):
        self.manager = TaskManager()
        tasks = self.manager.getTasks()
        for task in tasks:
            self.manager.deleteTask(task.name)
        
        self.manager.addTask("a", None)
        self.manager.addTask("c", None)
        self.manager.addTask("b", None)

        self.manager.SortTasks()

        tasks = self.manager.getTasks()
        nameList = []
        for task in tasks:
            nameList.append(task.name)

        sortedNameList = nameList
        sortedNameList.sort()

        self.assertEqual(nameList, sortedNameList)
