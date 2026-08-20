#Make a to do list 

task=[]
while True:
    def menu():

        user_input=input(""" 1. Add Task \n 2. View Task \n 3. Delete Task \n 4. Exit \n""")
        if user_input=="1":
            add_task()
        elif user_input=="2":
            view_task()
        elif user_input=="3":
            delete_task()
        elif user_input=="4":
            exit()

    def add_task():
        
            tasks=input("Enter task to add: ")
            if tasks in task:
                 print("Tasks already exist.")
            else:
                task.append(tasks)
                print("Task added successfully.")
            menu()

    def view_task():
        
            print("Your tasks are:",task)
            menu()

    def delete_task():
        
            delete=input("Enter task to delete: ")
            if delete in task:
                task.remove(delete)
                print("Task delete successfully.")
                menu()
            else:
                print("Task not found.")
                menu()
    def exit():
        
            print("Good bye! Thanks for using.")
            
    break

menu()



