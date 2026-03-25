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
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added ")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        status = "✓" if task["completed"] else "X"
        print(f'{task["id"]}. {task["title"]} [{status}]')

def completed_tasks(tasks):
    task_id = int(input("Enter task id to complete: "))

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task Completed")
            return
        
    print("Task not found")

def delete_tasks(tasks):
    task_id = int(input("Enter task id to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted")
            return
        
    print("Task not found")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Tracker")
        print("1. View Task")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            completed_tasks(tasks)
        elif choice == "4":
            delete_tasks(tasks)
        elif choice == "5":
            break
        else: 
            print("Invalid choice")


if __name__ == "__main__":
        main()