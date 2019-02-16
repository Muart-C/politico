#!api/database/database.py
import os
import psycopg2
from flask import current_app
from api.utils.validator import return_error
from api.database.db_manage import create_tables,\
     create_admin_if_does_not_exist, drop_tables_if_exists
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

    def create_all_tables(self):
        """create tables."""
        tables = create_tables()
        for table in tables:
            self.cursor.execute(table)
            self.connection.commit()

    def add_admin(self, connection):
        """create an admin."""
        create_admin_if_does_not_exist(connection)

    def drop_tables(self):
        """drop tables if exist"""
        tables = drop_tables_if_exists()
        for table in tables:
            self.cursor.execute(table)
            self.connection.commit()
            self.connection.close()

    def fetch_a_single_data_row(self, query):
        """retrieve a single data row."""
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        return row

    def fetch_all_data_rows(self, query):
        """retrieve rows of data in table."""
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
    def save_data_row(self, query):
        """save data of a row."""
        self.cursor.execute(query)
        self.connection.commit()
