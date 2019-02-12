"""#!api/models/users_model.py"""
import psycopg2
from werkzeug.security import generate_password_hash
from config import database_url
class User():
    """users model"""
    def __init__(self, email, hash_password):
        self.is_admin = False
        self.email = email
        self.hash_password = hash_password

    def create_user(self, hash_password):
        """create a user if one does not exist."""
        hash_password = generate_password_hash(hash_password)

        insert_user= "INSERT INTO users(email, hash_password,is_admin)"\
            " VALUES ('%s','%s', '%s')" %(self.email, self.hash_password, self.is_admin)

        connection = psycopg2.connect(database_url)
        cursor = connection.cursor()

        cursor.execute(insert_user)
        cursor.commit()

    def get_user(self, user_id):
        """get a user whose id was passed."""
        return self

    def check_if_user_exist_before_creating_one(self):
        """checks if a user exists before attempting to create one"""


