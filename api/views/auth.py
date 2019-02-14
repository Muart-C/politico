"""authentication endpoints"""
import re
from flask import Blueprint, request
from api.utils.validator import check_json_new_user_keys,\
     return_error, return_response, validate_string_data_type,\
         sanitize_input, check_email_validity, check_is_valid_url
from api.models.users_model import User

# add auth blueprint
AUTH_BLUEPRINT = Blueprint("auth", __name__)


# create user route
@AUTH_BLUEPRINT.route('/auth/signup', methods=["POST"])
def create_user():
    """create a new user."""
    key_errors=check_json_new_user_keys(request)
    if key_errors:
        return return_error(400, "Invalid keys provided")
    try:
        data = request.get_json()
        # validate data from the request
        firstname=data['firstname']
        lastname=data['lastname']
        othername=data['othername']
        phone_number=data['phone_number']
        passport_url=data['passport_url']
        email=data['email']
        password=data['password']

        if(check_email_validity(email) is False):
            return return_error(400, "enter the correct email format")

        if(validate_string_data_type(firstname) is False):
            return return_error(400, "the first name should be a string")
        if(validate_string_data_type(lastname) is False):
            return return_error(400, "the last name should be a string")
        if(validate_string_data_type(othername) is False):
            return return_error(400, "the other name should be a string")
        if(check_email_validity(email) is False):
            return return_error(400, "enter the correct email format")
        if(validate_string_data_type(phone_number) is False):
            return return_error(400, "the phone number should alphanumeric")
        if(check_is_valid_url(passport_url) is False):
            return return_error(400, "the passport url should be of correct \
                format")

        if(sanitize_input(firstname) == False):
            return return_error(400, "provide a valid first name")
        if(sanitize_input(lastname) == False):
            return return_error(400, "provide a valid last name")
        if(sanitize_input(othername) == False):
            return return_error(400, "provide a valid other name")

        if re.match('[a-zA-Z0-9@#$&^%+=-]{6,}', password) is None:
            return return_error(400, "password must be 6 or more characters")

    except KeyError as e:
        return return_error(400, "an error occurred while creating user  {} is missing".format(e.args[0]))

    user = User(email=email, password=password, firstname=firstname, \
        lastname=lastname, othername=othername, phone_number=phone_number, passport_url=passport_url)


    if user.check_if_user_exist_before_creating_one() is True:
        return return_error(400, "user already exists")
    new = user.create_user()
    if new:
        return return_response(201, "user was created successfully")
    return return_error(500, "error creating a user")


