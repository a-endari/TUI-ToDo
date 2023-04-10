import sqlite3


class DatabaseConnection:
    # __init__ creates the values this class takes and their name! , now it only takes one value 'database'
    def __init__(self, database):
        self.connection = None  # here we created self.connection to be used!
        self.database = database

    # enter is what a Contex Manager will do upon opening
    def __enter__(self):
        # here we updated self.connection as we enter the context manager
        self.connection = sqlite3.connect(self.database)
        return self.connection  # and here we returned it so it can be used

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()  # after exiting the context manager these two lines will run
        self.connection.close()
