#!api/database/database.py
import os
import psycopg2
from api.utils.validator import return_error
class DatabaseSetup:
    """database instance"""
    def __init__(self):
        self.dbname=os.getenv("DATABASE_POLITICO_TEST")
        self.user=os.getenv("DATABASE_USERNAME")
        self.password=os.getenv("DATABASE_PASSWORD")
        self.host=os.getenv("DATABASE_HOST")
        self.port=os.getenv("DATABASE_PORT")
        self.connection = psycopg2.connect(dbname=self.dbname,\
                user=self.user,host=self.host,\
                     password=self.password, port=self.port)
        self.cursor = self.connection.cursor()
        self.autocommit = True

    #to be used during testing database operations
    def drop_data_from_tables(self):
        self.cursor.execute("DELETE FROM users;")
        self.cursor.execute("DELETE FROM parties;")
        self.cursor.execute("DELETE FROM candidates;")
        self.cursor.execute("DELETE FROM petitions;")
        self.cursor.execute("DELETE FROM votes;")

        #persist the changes to the database
        self.connection.commit()

