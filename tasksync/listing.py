from .models import Task

def printTasks(tasks):
    headers = ["Done", "Name", "Project"]
    stops = [0, 0, 0]
    lineLength = 0

    if stops[0] < len(headers[0]) + 4:
        stops[0] = len(headers[0]) + 4
        
    if stops[1] < len(headers[1]) + 4:
        stops[1] = len(headers[1]) + 4

    if stops[2] < len(headers[2]) + 4:
        stops[2] = len(headers[2]) + 4

    for task in tasks:
        if stops[0] < 5:
            stops[0] = 5
        
        if stops[1] < len(task.name) + 4:
            stops[1] = len(task.name) + 4

        if stops[2] < len(task.project or "") + 4:
            stops[2] = len(task.project or "") + 4

    lineLength = stops[0] + stops[1] + stops[2]
    line = ""

    for i in range(1, lineLength + 1):
        if i == 1 or i == lineLength or i == stops[0] or i == stops[0] + stops[1] or i == stops[0] + stops[1] + stops[2]:
            line += '+'
        else:
            line += '-'

    print(line)
    
    headerLine = "| "
    headerLine += headers[0]
    while (len(headerLine) < stops[0] - 1):
        headerLine += ' '
    headerLine += '|'
    headerLine += ' '
    headerLine += headers[1]
    while (len(headerLine) < stops[0] + stops[1] - 1):
        headerLine += ' '
    headerLine += '|'
    headerLine += ' '
    headerLine += headers[2]
    while (len(headerLine) < stops[0] + stops[1] + stops[2] - 1):
        headerLine += ' '
    headerLine += '|'

    print(headerLine)


    print(line)

    for task in tasks:
        currLine = "| "

        if task.done:
            currLine += '✓'
        else:
            currLine += '✖'
        
        while (len(currLine) < stops[0] - 1):
            currLine += ' '
        currLine += '|'

        currLine += ' '
        currLine += task.name
        
        while (len(currLine) < stops[0] + stops[1] - 1):
            currLine += ' '
        currLine += '|'

        currLine += ' '
        currLine += task.project or ""

        while (len(currLine) < stops[0] + stops[1] + stops[2] - 1):
            currLine += ' '
        currLine += '|'

        print(currLine)

    print(line)
