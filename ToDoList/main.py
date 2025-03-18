import os
import sys
import datetime

filename = "./ToDoList/tasks.txt"

# Uses the datetime library to get current Month/Day/Year Hour:Minute
def get_current_time():
    return str(datetime.datetime.now().strftime("%D %H:%M"))

# Adds a new task to the tasks.txt file
def add_task(task):
    with open(filename, "a") as file:
        file.write(get_current_time() + ": " + task +"\n")

# Removes a task from the tasks.txt file
def remove_task(task):
    with open(filename, "r") as file:
        tasks = file.readlines()
    # Rewrites the tasks file removing the selected task
    with open(filename, "w") as file:
        for t in tasks:
            if t.strip() != task:
                # Write the task if it's different from the task selected
                file.write(t)

# Lists all tasks from the file printing them in the console.
def list_tasks():
    with open(filename, "r") as file:
        tasks = file.readlines()
    print("\n-== To Do List ==-\n")
    for i, t in enumerate(tasks):
        print(f"{i + 1}. {t.strip()}")
    print("\n")

# Clear all tasks from the tasks file
def clear_tasks():
    with open(filename, "w") as file:
        file.write("")

def main():
    # Shows the menu with the command options
    print("\nWelcome to the To-Do List!")
    print("Enter 'add' to add a task.")
    print("Enter 'remove' to remove a task.")
    print("Enter 'list' to list all tasks.")
    print("Enter 'clear' to clear all tasks.")
    print("Enter 'exit' to exit.")
    while True:
        # Gets a command from the user
        command = input("Enter a command: ")
        
        # If the command is equal to "add"
        # Ask the user for a task to insert in the file
        # Calls the add_tasks function to insert user's task
        if command == "add":
            task = input("Enter a task: ")
            add_task(task)
        
        # If the command is equal to "remove"
        # Ask the user for what task he wants to remove
        # Calls the remove_task function to remove an user's task
        elif command == "remove":
            task = input("Enter a task: ")
            remove_task(task)

        # If the command is equal to "list"
        # Lists all the tasks in the tasks file    
        elif command == "list":
            list_tasks()
        
        # If the command is equal to "clear"
        # Clears the task file removing all tasks
        elif command == "clear":
            clear_tasks()

        # If the command is equal to "exit"
        # Closes the program
        elif command == "exit":
            sys.exit()
        else:
            print("Invalid command.")
if __name__ == "__main__":
    if(open(filename, "r")):
        list_tasks()
    main()