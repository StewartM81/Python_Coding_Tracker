from datetime import datetime

class InputHandler():
    """A class to collect and validate user inputted data"""
    def __init__(self):
        return
    
    def input_string(self, message, min_length, max_length):
        """Display provided message, accept string, ensure it is within given length parameters and return valid input"""
        while True:
            user_input = input(message)
            if len(user_input) <= max_length and len(user_input) >= min_length:
                return user_input
            else:
                print(f"Please enter between {min_length} and {max_length} characters.")        
    
    def input_int(self, message, max_value):
        """Display provided message, accept int, ensure it is within given length parameters and return valid input"""
        while True:
            user_input = input(message)
            if user_input == 'q':
                return -1
            try:
                value = int(user_input)
                if value <= 0 or value > max_value:
                    print(f"Invalid, please enter a value no higher than {max_value}")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    def input_date(self, message):
        """Display provided message, accept date, ensure it is within given date range and return valid input"""
        date_format = "%d/%m/%Y %H:%M:%S"
        earliest_date = datetime.strptime("01/01/2000 00:00:00", date_format)
        latest_date = datetime.strptime("31/12/2030 23:59:59", date_format)
        while True:
            user_input = input(message)
            try:
                dt = datetime.strptime(user_input, date_format)
                if dt >= earliest_date and dt <= latest_date:
                    return dt
                else:
                    print(f"Invalid, please enter a date no earlier than {earliest_date} and no later than {latest_date}")
            except ValueError:
                print(f"Invalid format! Please enter date and time in the format: {date_format}")
    
    def validate_date(self, start_date, end_date):
        """Check that end_date is later than start_date"""
        if end_date > start_date:
            return True
        else:
            print("Error: End date must be after start date.")
            return False
        