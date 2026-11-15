from database import listTasks , saveTasks


def addTask(nameTask):
    nameTask = nameTask.strip()

    if not nameTask:
        return "Vous n'avez rien saisi."

    if nameTask in listTasks:
        return "Cette tâche existe déjà."

    listTasks.append(nameTask)
    saveTasks()
    return f"Tâche '{nameTask}' ajoutée."


def deleteTask(nameTask):
    if nameTask not in listTasks:
        return f"{nameTask} ne se trouve pas dans les tâches."
    else:
        listTasks.remove(nameTask)
        saveTasks()
        return f"Tâche '{nameTask}' supprimée."


def showTasks():
    if len(listTasks) == 0:
        return "Aucune tâche disponible."
    else:
        return ", ".join(listTasks)


def updateTask(nameTask, newTask):
    newTask = newTask.strip()

    if not newTask:
        return "Le nouveau nom ne peut pas être vide."

    if nameTask not in listTasks:
        return f"{nameTask} ne se trouve pas dans les tâches."
    else:
        index = listTasks.index(nameTask)
        listTasks[index] = newTask
        saveTasks()
        return f"Tâche '{nameTask}' mise à jour en '{newTask}'."
