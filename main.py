from Logger.controller import Controller

logger_controller = Controller()

while True:
    print("""Please Select an option from below:
             1. View Records
             2. Create a new record
             3. Update a record
             4. Delete a record
             5. Exit """)
    
    user_option = int(input())

    match user_option:
        case 1:
            logger_controller.list_sessions()            
        case 2:
            logger_controller.create_new_session_record()            
        case 3:
            logger_controller.update_session()            
        case 4:
            logger_controller.delete_session()
        case 5:
            print("Thank you for using the Coding Logger, please have a nice day")
            break
        case _:
            print("Please enter a valid Option from the menu")
