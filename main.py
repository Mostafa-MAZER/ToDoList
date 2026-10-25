import todo_functions as functions

functions.load_tasks()

while True:
    operation = functions.todo_front()
    

    if operation == "add":
        task=str(input("entre your task :"))
        functions.add_task(task)
        functions.save_tasks()
    elif operation =="view":
        functions.view_tasks()
    elif operation =="delete":
        print(functions.delete_task())
        functions.save_tasks()
    elif operation =="mark":
        print(functions.mark_task())
        functions.save_tasks()
    elif operation =="unmark":
        print(functions.unmark_task())
        functions.save_tasks()
    elif operation =="change":
        print(functions.Change_priority())
        functions.save_tasks()
    elif operation == "edit":
        print(functions.edit_task())
        functions.save_tasks()
    elif operation =="search":
        functions.search_task()
    elif operation =="clear":
        functions.clear_task()
        functions.save_tasks()
    elif operation =="clear completed":
        functions.delete_completed_tasks()
        functions.save_tasks()
    elif operation =="stats":
        functions.statistics()
    elif operation =="exit":
        print("Goodbye") 
        break  
    else:
        print("Invalid operation. Please try again.") 

