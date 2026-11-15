listTasks = []


def saveTasks():
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(listTasks))


def addTasksToFile(newTask):
    if newTask not in listTasks:
        with (open('tasks.txt', 'a', encoding='utf-8') as file):
            file.write(f"{newTask}\n")

        listTasks.append(newTask)
        return "Tâche ajoutée avec succès"

    return f"{newTask} existe déjà"


def loadTasks():
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
