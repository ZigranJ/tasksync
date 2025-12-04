from dataclasses import dataclass

@dataclass
class Task:
    name: str
    project: str = "" # optional
    done: bool = False

# Task as JSON:
"""
    {
        "name": "example_name",
        "project": "example_project",
        "done": false
    }
"""