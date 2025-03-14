# Initialize the Phonebook
phonebook = {}

# User Interface and CRUD Operations without functions
while True:
    # Display menu
    print("\n--- Phonebook Menu ---")
    print("1. Add a New Contact")
    print("2. Search for a Contact")
    print("3. update a Contact")
    print("4. Delete a Contact")
    print("5. List All Contacts")
    print("6. Exit")
    
    # Get user choice
    choice = input("Enter your choice: ")

    # Add a New Contact
    if choice == '1':
        name = input("Enter the contact name: ")
        if name in phonebook:
            print(f"{name} already exists in the phonebook.")
        else:
            number = input(f"Enter {name}'s phone number: ")
            phonebook[name] = number
            print(f"{name} has been added to the phonebook.")
    
    # Search for a Contact
    elif choice == '2':
        name = input("Enter the name to search: ")
        if name in phonebook:
            print(f"{name}'s phone number is {phonebook[name]}.")
        else:
            print(f"{name} not found in the phonebook.")
    
    elif choice=='3':
        update_name=input('Enter number to update : ')
        if update_name in phonebook:
            new_name=input('Enter new name : ')
            new_number=input('Enter new number')            
            phonebook[new_name]=phonebook.pop(update_name)
            phonebook[new_name]=new_number
            print(f'{update_name} is updated by {new_name} and {new_number}')
        else:
            print('User not found!')   
    # Delete a Contact
    elif choice == '4':
        name = input("Enter the name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"{name} has been deleted from the phonebook.")
        else:
            print(f"{name} not found in the phonebook.")
    
    # List All Contacts
    elif choice == '5':
        if phonebook:
            print("\n--- List of Contacts ---")
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        else:
            print("No contacts in the phonebook.")
    
    # Exit the Program
    elif choice == '6':
        print("Exiting the phonebook application. Goodbye!")
        break
    
    # Invalid choice
    else:
        print("Invalid choice. Please try again.")
