print('-------Welcome to Task Management App-------')
'''
user can add a task
user can update a task
user can delete a task
user can see all the task
exit
'''
# Initialize an empty list to store the task
tasks=[]
limit=int(input('Enter how many tasks you wants to add = '))
for i in range(1,limit+1):
    task_name=input(f'Enter your {i} task : ')
    tasks_list=tasks.append(task_name)

while True:
    choice=int(input('Enter your choice...\n1. Add task\n2. update task\n3. Delete task\n4. View all task\n5.Exit\n'))
    print(f'Your choice is {choice} ')   
    # Adding tasks 
    if choice==1:
        task_name=input(f'Enter your new task : ')
        tasks_list=tasks.append(task_name)
    # Updating / Edit task from the app
    elif choice==2:
        update_task=input('Enter task that you want to delete : ')
        if update_task in tasks:
            new_task=input('Enter new task to update : ')
            task_index=tasks.index(task_name)
            tasks[task_index]=new_task
            print(f'Task {update_task} is updated by new task {new_task} successfully')
        else:
            print(f'{update_task} is not found')    
    # Deleting task from the app
    elif choice==3:
        task_name=input('Enter task to delete : ')
        task_index=tasks.index(task_name)
        del tasks[task_index]
        print(f'Your task {task_name} deleted successfully...')

    # Display List of user Tasks    
    elif choice==4:
        if len(tasks)>0:
            print(f"Your today's tasks are\n{tasks}")
        else:
            print('There is no tasks yet!')    
    # Exiting from the app
    elif choice==5:
        print('Exiting the program...')
        break
    # if user enters an invalid choice
    else:
        print('Invalid choice')    