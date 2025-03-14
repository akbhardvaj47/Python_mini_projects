all_students={'Amit':800}
def add_student(name,grade):
    all_students[name]=grade
    print(all_students)
    print(f'Student {name} is added successfully')
# add_student()

def update_student(name):
    if name in all_students:
        old_student=all_students.pop(name)
        new_student=input('Enter new student name to update : ')
        grade=int(input('Enter grade : '))
        all_students[new_student]=grade
        print(f'{name} is updated by {new_student} is successfully...')
# update_student() 

def delete_student(name):
    del all_students[name]
    print(f'Student {name} is deleted successfully')
# delete_student() 

def display_students():
    if all_students:
        for name,grade in all_students.items():
            print(f'{name} {grade}')
# display_students()

def exit_app():
    print(f'You are exiting, Goodbye!')
    
def body():
    while True:
        print('1. Add a student')
        print('2. update a student')
        print('3. Delete a student')
        print('4. Display all students')
        print('5. Exit / Stop')
        choice=int(input('Enter your choice : '))
        if choice==1:
            name=input('Enter name :')
            grade=int(input('Enter grade :'))
            add_student(name,grade)
        elif choice==3:
            name=input('Enter student name to delete : ')
            delete_student(name)
        elif choice==2:
            name=input('Enter student name that you want to update : ')
            update_student(name)
        elif choice==4:
            display_students()
        elif choice==5:
            exit_app()
            break
        else:
            print('Invalid choice')        
           

body()        