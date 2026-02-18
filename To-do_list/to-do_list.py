tasks=[]

while True:


    print("""=== TO-DO LIST ===
    1. Add Task
    2. View Tasks
    3. Mark Task as Complete
    4. Delete Task
    5. Exit""")

    user_option=input("\nchoose an option (1)(2)(3)(4)(5): ")
            
    if user_option=="1":
        number_tasks=int(input("How many tasks do you want to add? "))
        for i in range(1,number_tasks+1):
            adding_task=input("Enter the name of the task that you want to add to your to do list:")    
            tasks.append(adding_task)
            
    elif user_option=="2":
        print(f"here's your tasks list {tasks}")

    elif user_option=="3":
            print(tasks)
            done_tasks=input("Enter the name of the task that you've done:")
            if done_tasks in tasks:
                  
                tasks.remove(done_tasks)
                print(f"Here are your remaining tasks {tasks}")
            else:
                  print("task not found!")
    elif user_option=="4":
            print(tasks)
            deleting_tasks=input("Enter the name of the tasks that you want to delete:")
            if deleting_tasks in tasks : 
                tasks.remove(deleting_tasks)
                print(f"Here are your remainig tasks {tasks}")
            else :
                  print("task not found!")
        
    elif user_option=="5":
            print("Goodbye!")
            break
	
    else:
        print("Error!")



