# 📌 PYTHON ZERO TO AI — POST 15 OF 30

"""Yesterday: List comprehensions
Today: Mini project — To-Do list app

We've learned: variables, lists, loops, input, if/else, functions, files.

Let's BUILD something real.

💻 FULL APP (copy to Colab):"""

tasks = []

def show_menu():
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks yet")
        return
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def delete_task():
    view_tasks()
    num = int(input("Number to delete: "))
    removed = tasks.pop(num-1)
    print(f"Deleted: {removed}")

# Main loop
while True:
    show_menu()
    choice = input("Choose: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

"""🧠 WHAT THIS USES:

Variables     → store tasks list
Functions     → menu, add, view, delete
Loops         → while True (keeps running)
If/elif/else  → menu choices
Input         → user choices
Lists         → tasks storage

🎯 UPGRADE IDEAS:

• Save tasks to file (Post #13)
• Add due dates
• Mark tasks complete
• Edit existing tasks

👇 YOUR TURN:

Run the code. Add 3 tasks. View them. Delete one.

Tomorrow: We start the next level — DATA ANALYSIS with pandas!

#PythonProject #ToDoApp #BuildWithPython #LearnPython"""