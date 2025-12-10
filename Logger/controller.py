from .database import DatabaseManager
from .input import InputHandler

class Controller():
    """An class to interface with a database controller  

        Allows user to create, update and delete Coding sessions.    
    """
    def __init__(self):
        """Initialise a new Coding Session Controller and attach database controller instance

            db_manager      DatabaseController
            input_handler   InputHandler 
        """

        self.db_manager = DatabaseManager()
        self.input_handler = InputHandler()

    def create_new_session_record(self):
        """Accept and validate user data and send to DatabaseController to create new record"""
        dt_check = False
        message = "Please enter user name: "
        user_name = self.input_handler.input_string(message, 5, 20)

        message = "Please enter coding lanaguage used: "
        user_language = self.input_handler.input_string(message, 1, 15)
                
        while dt_check == False:
            message = "Please enter the start date/time using format 'dd/mm/yyyy hh:mm:ss'"
            user_start_date = self.input_handler.input_date(message)

            message = "Please enter the end date/time using format 'dd/mm/yyyy hh:mm:ss'"
            user_end_date = self.input_handler.input_date(message)

            dt_check = self.input_handler.validate_date(user_start_date, user_end_date)

        self.db_manager.create_session(user_name, user_language, user_start_date, user_end_date)

    def list_sessions(self):
        """Get a list of records from the DatabaseController and display on screen"""
        coding_sessions = self.db_manager.get_session()
        if len(coding_sessions) == 0:
            print("There are no sessions stored")
        for session in coding_sessions:
            print(f"""ID: {session.id},
                   User: {session.user_name},
                   Language: {session.coding_language},
                   Start: {session.start_time.strftime('%d/%m/%Y %H:%M:%S')},
                   End: {session.end_time.strftime('%d/%m/%Y %H:%M:%S')},
                   Duration: {session.duration_minutes} minutes""")

    def delete_session(self):
        """Display list of records, and accept ID of record to delete"""
        message = "Please enter ID number of record to delete or 'q' to exit back to main menu: "
        record_count = self.db_manager.count_sessions()
        if record_count == 0:
            print("There are no records to delete")
            return
        self.list_sessions()
        id_number = self.input_handler.input_int(message, record_count)
        if id_number == -1:
            return
        else:
            self.db_manager.delete_session(id_number)

    def update_session(self):
        """Request list of records from DatabaseController, display to screen, update selected record with entered data"""
        message = "Please enter ID number of record to update or 'q' to exit back to main menu: "
        record_count = self.db_manager.count_sessions()
        if record_count == 0:
            print("There are no records to delete")
            return
        self.list_sessions()
        id_number = self.input_handler.input_int(message, record_count)
        if id_number == -1:
            return
        else:
            dt_check = False
            message = "Please enter user name: "
            user_name = self.input_handler.input_string(message, 5, 20)

            message = "Please enter coding lanaguage used: "
            user_language = self.input_handler.input_string(message, 1, 15)
                
            while dt_check == False:
                message = "Please enter the start date/time using format 'dd/mm/yyyy hh:mm:ss'"
                user_start_date = self.input_handler.input_date(message)

                message = "Please enter the end date/time using format 'dd/mm/yyyy hh:mm:ss'"
                user_end_date = self.input_handler.input_date(message)

                dt_check = self.input_handler.validate_date(user_start_date, user_end_date)

            self.db_manager.update_session(id_number, user_name, user_language, user_start_date, user_end_date)





            


        



        


        

