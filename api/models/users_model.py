"""#!api/models/users_model.py"""

class User():
    """users model"""
    def __init__(self):
        self.is_admin = False

    def create_user(self, firstname, lastname,email,phone_number,passport_url, password):
        """create a user if one does not exist."""
        return self

    def get_user(self, user_id):
        """get a user whose id was passed."""
        return self

    def check_if_user_exist_before_creating_one(self):
        """checks if a user exists before attempting to create one"""


