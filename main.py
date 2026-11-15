import tasks
from database import loadTasks
loadTasks()

def menu():
    print("1. Ajouter une tâche")
    print("2. Modifier une tâche")
    print("3. Supprimer une tâche")
    print("4. afficher les tâches")
    print("0. Quitter")

choice = -1

while choice != 0:
    menu()
    choice = int(input("Choisissez une chiffre pour votre tache (1.ajouter,2.modifier,3.supprimer ,0.quitter):)"))
    if choice == 1:
        tache = input("saisi le tache: ").lower().strip()
        tasks.addTask(tache)
    elif choice == 2:
        tacheEcient = input("saisi la tache a modifier : ").lower().strip()
        newTask = input("saisi la nouvelle tache  : ").lower().strip()
        tasks.updateTask(tacheEcient, newTask)
    elif choice == 3:
        taskDele = input("saisi la tache a supprimer : ").lower().strip()
        tasks.deleteTask(taskDele)
    elif choice == 4:
        print(tasks.showTasks())
    elif choice == 0:
        print("Thank You")
    else:
        print("choice invallide")
        choice = int(input("Choisissez une chiffre pour votre tache (1.ajouter,2.modifier,3.supprimer ,0.quitter):)"))


print(tasks.showTasks())