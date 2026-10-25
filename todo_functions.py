import json
liste=[]
def todo_front():
    print("------TO DO LIST------")
    print("----------------------")
    print()
    print("chose what operation you want ")
    print()
    print("add for add task")
    print()
    print("View for View all tasks")
    print()
    print("change for changing priority of a task ")
    print()
    print("Delete for Delete a task")
    print()
    print("clear for delete all task ")
    print()
    print("Mark for Mark a task")
    print()
    print("unMark for unmark a task ")
    print()
    print("clear completed for delete completed tasks")
    print()
    print("edit for editing a task")
    print()
    print("search for search for a task by keyword ")
    print()
    print("stats for the statistics")
    print()

    print("Exit for Exit the program")
    print()
    operation=str(input("Enter the operation :")).lower()
    print("------------------------")
    return operation

def add_task(task):
    task = task.strip()
    if not task:
        print( "Error: Task can't be empty.")
        return
    new_task={"task":task,
              "completed":False,
              "priority":"Medium"}
    liste.append(new_task)
    print(f"'{task}' added successfully.")
    while True:
        question=str(input("Do you want to set a priority? (y/n) :")).lower().strip()
        if question =='y':
            break
        elif question=='n':
            print("operation has cansol")
            break
        else:
            print("inbut in valide")
    if question == 'y':
        while True:
            priority=str(input("Enter priority (High/Medium/Low):")).lower().strip()
            if priority =='high':
                new_task["priority"]="High"
                
                break
            elif priority =='medium':
                
                break
            elif priority =='low':
                new_task["priority"]="Low"
                break
            else:
                print("input invalid")
        print("priority has set successfully")
       
def view_tasks():
    print("---TASKS---")
    if not liste:
        print("No Task Found")
        return
    for index,task in enumerate(liste):
        if task["completed"]:
            state="[✓]"
        else:
            state="[ ]"
        print(f'{index+1}. {state} [{task["priority"]}] {task["task"]}')
    
def delete_task():
    
    try:
        if not liste:
            return "No tasks to Mark."
        x=int(input("enter number of tha Task to delete :"))
        index =x-1
        while index <0 or index >= len(liste):
            x=int(input("number of the task is not on the list please try again :"))
            index = x-1
        task=liste.pop(index)
        return  f"{task['task']} deleted successfully."

    except ValueError:
        return "Erorr : value is not a number "
    
def mark_task():
    try:
        if not liste:
            return "No tasks to delete."
        y=int(input("enter the number of the  task you complete :"))
        index = y-1
        while index <0 or index >= len(liste):
            y=int(input("number is not in the list please entre again the number of the  task you complete  :"))
            index = y-1
        if liste[index]["completed"]:
            return "Task alredy completed"
        
        liste[index]["completed"] = True
        
        return "Task has Mark "
        
    except ValueError:
        return "Error : value is not a number "

def unmark_task():
    x=int(input("enter the number of the task you want to unMark :"))
    index=x-1
    while index <0 or index >= len(liste):
        x=int(input("enter again numbre of the task is not en the list :"))
        index =x-1
    if liste[index]["completed"]:
        liste[index]["completed"]=False
        return "Task has unmark successfully."
    else:
        return "An incomplete task from the start." 

def load_tasks():
    try:
        global liste
        with open("tasks.json","r") as f:
            liste = json.load(f)
    except FileNotFoundError:
        pass

def save_tasks():
    with open ("tasks.json","w") as f:
        json.dump(liste, f)

def edit_task():
    
    try:
        if not liste:
            return "task list is empty."
        x=int(input("enter the number of the task you want to edit :"))
        index = x-1
        while index <0 or index >= len(liste):
            x=int(input("enter the number of the task you want to edit :"))
            index = x-1

        
        new_task=str(input("enter the editing task :"))
        
        new_task= new_task.strip()
        if not new_task:
            return "task is empty"
        
        liste[index]["task"]=new_task
        return f"{new_task} updated successfully."
    except ValueError:
        return "Error: Task number must be a number. "
    
def search_task():
    if not liste:
        print("Task list is empty.")
        return 
    search =str(input("enter the keyword :")).strip().lower()
    if not search:
        print("Error: keyword can't be empty.")
    found = False
    print("---Search Results---")
    for index,task in enumerate(liste):
        if search in task["task"].lower():
            if task["completed"]:
                state="[✓]"
            else :
                state ="[ ]"
            print(f'{index+1}. {state} {task["task"]}')
            found=True
    if not found:
        print("No matching tasks found.")

def clear_task():
   
    while True:
        x=str(input("do you want to clear task ? (y/n) :")).lower().strip()
        if x=="y":
            liste.clear()
            print("Liste has ben clear successfully.")
            break
        elif x=="n":
            print("operation has cancel")
            break
      
def delete_completed_tasks():
    counter=0
    if not liste:
        return "list is empty "
    while True:
        x=str(input("do you want to delete all completed  task ? (y/n) :")).lower().strip()
        if x=="y":
            for index in reversed(range(len(liste))):
                if liste[index]["completed"]:
                    liste.pop(index)
                    counter+=1
            if counter ==0:
                print("No completed task has found")
            else:
                print(f"{counter} has ben deleted successfully.")
            break
        elif x=="n":
            print("operation has cancel ")
            break
        else:
            print("input invalid")

def statistics():
    completed_tasks=0
    if not liste :
        print("No task found.")
        return
    total_tasks=len(liste)
    for task in liste:
        if task["completed"]:
            completed_tasks+=1
    pending_tasks = total_tasks - completed_tasks
    
    completion = (completed_tasks / total_tasks) * 100
    print("======Statistics======")
    print(f"{'Total tasks':12} : {total_tasks :5}")
    print(f"{'Completed':12} : {completed_tasks:5}")
    print(f"{'Pending':12} : {pending_tasks:5}")
    print(f"{'Completion':12} : {completion:5.2f}%")
    print("======================")

def Change_priority():
    x=int(input("enter the number of the task you want to unMark :"))
    index=x-1
    while index <0 or index >= len(liste):
        x=int(input("enter again numbre of the task is not en the list :"))
        index =x-1
    changing=str(input("enter the priority (High/Medium/Low) :")).lower().strip()
    if changing =="high":
        if liste[index]["priority"] == "high":
            return f"task is already [{changing}]"
        else:
            liste[index]["priority"]="high"
            return "changing  task priority has ben successfully."
    if changing =="medium":
        if liste[index]["priority"] == "medium":
            return f"task is already [{changing}]"
        else:
            liste[index]["priority"]="medium"
            return "changing  task priority has ben successfully."
    if changing =="low":
        if liste[index]["priority"] == "low":
            return f"task is already [{changing}]"
        else:
            liste[index]["priority"]="low"
            return "changing  task priority has ben successfully."