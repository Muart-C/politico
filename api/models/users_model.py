"""#!api/models/users_model.py"""
from werkzeug.security import generate_password_hash
from psycopg2.extras import RealDictCursor
from api.database.database import DatabaseSetup
class User(DatabaseSetup):
    """users model"""
    def __init__(self, email=None,password=None,firstname=None,lastname=None,othername=None,passport_url=None,phone_number=None):
        super().__init__()
        self.is_admin = False
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.passport_url = passport_url
        self.phone_number =  phone_number
        self.password = password



    def create_user(self):
        """create a user if one does not exist."""
        self.cursor.execute('''SELECT * FROM users WHERE email='{}';'''.format(self.email))
        user=self.cursor.fetchone()
        if user is None:
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
            return "user created"
        else:
            return False

    def get_user(self, email):
        """get a user whose id was passed."""
        self.cursor.execute('''SELECT * FROM users WHERE email='{}';'''.format(email))
        user=self.cursor.fetchone()
        self.connection.commit()
        return user


