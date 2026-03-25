import json

def load_tasks():
    with open("tasks.json", "r") as file:
        data = json.load(file)
        return data["tasks"]
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump({"tasks": tasks}, file, indent=4) #this write to the json file, takes tasks list from py and put it in a dictionary, convert it into json format, write it into tasks.json, indent it used for formatting

def add_tasks(tasks):
    title = input("Enter title of taks: ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "status": "pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added ")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        # status = "✓" if task["completed"] else "X"
        print(f'{task["id"]}. {task["title"]} [{task["status"]}]')

# def completed_tasks(tasks):
#     task_id = int(input("Enter task id to complete: "))

#     for task in tasks:
#         if task["id"] == task_id:
#             task["completed"] = True
#             save_tasks(tasks)
#             print("Task Completed")
#             return
        
#     print("Task not found")

def delete_tasks(tasks):
    task_id = int(input("Enter task id to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted")
            return
        
    print("Task not found")

def update_tasks(tasks):
    task_id = int(input("Enter task id to update: "))

    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter new title: ")
            task["title"] = new_title
            save_tasks(tasks)
            print("Task updated")
            return
    
    print("Task not found")

def change_status(tasks):
    task_id = int(input("Enter task id: "))

    for task in tasks:
        if task["id"] == task_id:
            print("1. Pending")
            print("2. Completed")
            print("3. In Progress")

        choice = input("Choose status: ")

        if choice == "1":
            task["status"] = "Pending"
        elif choice == "2":
            task["status"] = "Completed"
        elif choice == "3":
            task["status"] = "In Progress"
        else:
            print("Invalid choice")
            return
        
        save_tasks(tasks)
        print("Status updated!")
        return
    

    print("Task not found")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Tracker")
        print("1. View Task")
        print("2. Add Task")
        print("3. Update Status")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")

        choice = input("Enter your option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            change_status(tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            update_tasks(tasks)
        elif choice == "6":
            break
        else: 
            print("Invalid choice")


if __name__ == "__main__":
        main()