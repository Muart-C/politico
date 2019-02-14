"""#!api/models/users_model.py"""
from werkzeug.security import generate_password_hash
from psycopg2.extras import RealDictCursor
from api.database.database import DatabaseSetup
class User(DatabaseSetup):
    """users model"""
    def __init__(self, **kwargs):
        super().__init__()
        self.is_admin = False
        self.email = kwargs.get("email")
        self.firstname = kwargs.get("firstname")
        self.lastname = kwargs.get("lastname")
        self.othername = kwargs.get("othername")
        self.passport_url = kwargs.get("passport_url")
        self.phone_number =  kwargs.get("phone_number")
        self.password = generate_password_hash(kwargs.get("password"))



    def create_user(self):
        """create a user if one does not exist."""
        insert_user= '''INSERT INTO users(\
            email, password, is_admin, firstname, lastname, othername,\
                 passport_url, phone_number) VALUES ('{}','{}','{}', '{}','{}',\
                '{}','{}','{}') RETURNING firstname, lastname,\
                     othername, email'''.format(self.email, \
                    self.password, self.is_admin,\
                         self.firstname, self.lastname,self.othername, \
                             self.passport_url,self.phone_number)

        self.cursor.execute(insert_user)
        self.connection.commit()
        self.cursor.close()
        return self

    def get_user(self, user_id):
        """get a user whose id was passed."""
        self.cursor.execute('''SELECT * FROM users WHERE email='{}';'''.format(self.email))
        user=self.cursor.fetchone()
        if user is not None:
	        return user
        else:
	        return None

    def check_if_user_exist_before_creating_one(self):
        """checks if a user exists before attempting to create one"""
        self.cursor.execute('''SELECT * FROM users WHERE email='{}';'''.format(self.email))
        user=self.cursor.fetchone()
        if user is None:
            return False
        return True


