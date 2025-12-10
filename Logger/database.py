from peewee import *
from datetime import datetime

class DatabaseManager():
    """An class to construct and interact with a SQLite Database via ORM 

        Controls the creation, updating and deletion of Coding sessions records.    
    """

    def __init__(self, db_path="coding_sessions.db"):
        """Initialise a new Coding Session Tracker istance database and ORM scaffolding

            db              sqLite3 connection
            BaseModel       base class, so all database models can inherit Meta data
            CodingSession   database model for Coding Session table 
        """
        self.db = SqliteDatabase(db_path)

        class BaseModel(Model):            
            class Meta:
                database = self.db
        
        class CodingSession(BaseModel):
            user_name = CharField(max_length=50)
            coding_language = CharField(max_length=20)
            start_time = DateTimeField()
            end_time = DateTimeField()
            duration_minutes = IntegerField(null=True)
        
        self.CodingSession = CodingSession

        self.db.connect()
        self.db.create_tables([self.CodingSession])

    def create_session(self, user_name, language, start, end):
        """Takes input from arguments and creates a new record in the database"""
        duration = int((end - start).total_seconds() / 60)
        self.CodingSession.create(
            user_name = user_name,
            coding_language = language,
            start_time = start,
            end_time = end,
            duration_minutes = duration
        )

    def get_session(self):
        """Returns a list of all fields in the database"""
        return list(self.CodingSession.select())

    def update_session(self, session_id, new_user, new_language, new_start, new_end):
        """Updates record goven in arguments with data given in arguments"""
        try:
            session = self.CodingSession.get(self.CodingSession.id == session_id)
                        
            session.user = new_user
            session.coding_language = new_language
            session.start_time = new_start
            session.end_time = new_end
            session.duration = int((session.end_time - session.start_time).total_seconds() / 60)

            session.save()  
            print(f"Session {session_id} updated successfully.")
    
        except self.CodingSession.DoesNotExist:
             print(f"No session found with ID {session_id}")    
    
    def delete_session(self, record_id):
        """Deletes record with id given in arguments"""
        deleted_count = self.CodingSession.delete().where(self.CodingSession.id == record_id).execute()
        if deleted_count:
            print(f"Deleted session {record_id}")
            return True
        else:
            print(f"Session {record_id} not found")
            return False
        
    def count_sessions(self):
        """Returns a count of records contained in the database"""
        return self.CodingSession.select().count()








