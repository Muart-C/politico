#!api/database/database.py
import os
import psycopg2
from flask import current_app
from api.utils.validator import return_error
from api.database.db_manage import create_tables, drop_tables_if_exists

class DatabaseSetup:
    """setup database instance of postgres"""
    def __init__(self):
        try:
            db_url = current_app.config['DATABASE_POLITICO']
            self.connection = psycopg2.connect(db_url)
            self.cursor = self.connection.cursor()
        except psycopg2.DatabaseError:
            return_error(400, "an error occurred\
                 while connecting to database")

    def drop_tables(self):
        """drop tables if exist"""
        tables = drop_tables_if_exists()
        print(tables)

        for table in tables:
            self.cursor.execute(table)
        self.connection.commit()
        self.connection.close()

    def create_all_tables(self):
        """create tables."""
        tables = create_tables()
        for table in tables:
            self.cursor.execute(table)
        self.connection.commit()
        self.connection.close()

    def create_admin_if_does_not_exist(self):
       """create an admin."""
       self.cursor.execute('''SELECT * FROM users WHERE email='ndirangu@gmail.com';''')
       user=self.cursor.fetchone()
       if user is None:
            create_admin= '''INSERT INTO users(\
                    email, password, is_admin, firstname, lastname, othername,\
                        passport_url, phone_number) VALUES \
                            ('muathe.ndirangu@gmail.com', 'ndirangu', 'True',\
                                'muathe', 'ndirangu','muathe', \
                                    'https://mypassport.com','+2342343');'''
            print(create_admin)

       self.cursor.execute(create_admin)
       self.connection.commit()
       self.cursor.close()

    def fetch_a_single_data_row(self, query):
        """retrieve a single data row."""
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        self.cursor.close()
        return row

    def fetch_all_data_rows(self, query):
        """retrieve rows of data in table."""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.cursor.close()
        return rows

    def save_data_row(self, query):
        """save data of a row."""
        self.cursor.execute(query)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
