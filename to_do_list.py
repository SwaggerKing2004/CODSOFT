
task_list = [] #create empty task list

#add task function
def addTask():
  task = input("Please enter a task: ")
  task_list.append(task)
  print(f"Task '{task}' added to the list.")

#list task function
def listTasks():
  if not task_list:
    print("There are no tasks currently.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(task_list,start=1): #start the list from index 1
      print(f"Task #{index}. {task}")

#delete task function
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 1 and taskToDelete <= len(task_list): 
            task_list.pop(taskToDelete - 1)  # Adjusted index by subtracting 1
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

if __name__ == "__main__":
  ### Create a loop to run the app
  print("Welcome to the to do list app :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. ADD A NEW TASK")
    print("2. LIST TASKS")
    print("3. DELETE TASKS")
    print("4. EXIT")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      listTasks()
    elif (choice == "3"):
      deleteTask()
    elif (choice == "4"):
      break
    else:
      print("Invalid input. Please try again.")

  print("Goodbye 👋👋")
