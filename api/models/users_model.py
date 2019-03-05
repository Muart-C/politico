import json
from werkzeug.security import generate_password_hash, check_password_hash
from api.database.database import DatabaseSetup
from api.utils.validator import return_error
class User(DatabaseSetup):
    def __init__(self, **kwargs):
        super().__init__()
        self.is_admin = False
        self.email = kwargs.get('email')
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.othername = kwargs.get('othername')
        self.passport_url = kwargs.get('passport_url')
        self.phone_number =  kwargs.get('phone_number')
        self.hash_password =  kwargs.get('password')

    def create_user(self):
        self.cursor.execute('''SELECT * FROM users WHERE email='{}';'''.format(self.email))
        user=self.cursor.fetchone()
        if user is None:
            insert_user= '''INSERT INTO users(\
                email, password, is_admin, firstname, lastname, othername,\
                    passport_url, phone_number) VALUES ('{}','{}','{}', '{}','{}',\
                    '{}','{}','{}') RETURNING firstname, lastname,\
                        othername, email'''.format(self.email, \
                        self.hash_password, self.is_admin,\
                            self.firstname, self.lastname,self.othername, \
                                self.passport_url,self.phone_number)

            self.cursor.execute(insert_user)
            self.connection.commit()
            self.cursor.close()
            return "user was created"
        else:
            return False

    def get_user(self, email):
        self.cursor.execute('''SELECT * FROM users\
             WHERE email='{}';'''.format(email))
        user=self.cursor.fetchone()
        self.connection.commit()
        self.cursor.close()
        return user

    def get_users(self):
        self.cursor.execute('''SELECT * FROM users WHERE is_admin='f';''')
        users=self.cursor.fetchall()
        return users

    @staticmethod
    def check_password_match(self, password_hash, password):
        return check_password_hash(password_hash, str(password))

    def get_user_by_id(self, user_id):
        self.cursor.execute('''SELECT * FROM users WHERE id='{}';'''.format(user_id))
        user=self.cursor.fetchone()
        self.connection.commit()
        self.cursor.close()
        return user
