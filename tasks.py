def addTask(nameTask):
    if len(nameTask.strip()) == 0:
        return "Vous n'avez rien saisi."
    else:
        listTasks.append(nameTask.strip())
        return f"Tâche '{nameTask}' ajoutée."


def deleteTask(nameTask):
    if nameTask not in listTasks:
        return f"{nameTask} ne se trouve pas dans les tâches."
    else:
        listTasks.remove(nameTask)
        return f"Tâche '{nameTask}' supprimée."


def showTasks():
    if len(listTasks) == 0:
        return "Aucune tâche disponible."
    else:
        return ", ".join(listTasks)


def updateTask(nameTask, newTask):
    if nameTask not in listTasks:
        return f"{nameTask} ne se trouve pas dans les tâches."
    else:
        index = listTasks.index(nameTask)
        listTasks[index] = newTask
        return f"Tâche '{nameTask}' mise à jour en '{newTask}'."
