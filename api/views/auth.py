import datetime
import json
import re
from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from api.utils.validator import check_json_new_user_keys,\
     return_error, validate_string_data_type,\
         sanitize_input, check_email_validity, check_is_valid_url,\
             check_phone_number_validity

from api.utils.validator import validate_password
from api.models.users_model import User

AUTH_BLUEPRINT = Blueprint("auth", __name__)

@AUTH_BLUEPRINT.route('/auth/signup', methods=["POST"])
def create_user():
    key_errors=check_json_new_user_keys(request)
    if key_errors:
        return return_error(400, "Invalid keys provided")
    try:
        data = request.get_json()
        firstname=data['firstname']
        lastname=data['lastname']
        othername=data['othername']
        phone_number=data['phone_number']
        passport_url=data['passport_url']
        email=data['email']
        password=data['password']

        if(check_email_validity(email) is False):
            return return_error(400, "Enter the correct email format i.e should contain @ and .")
        if(validate_string_data_type(firstname) is False):
            return return_error(400, "The first name should contain character of words")
        if(validate_string_data_type(lastname) is False):
            return return_error(400, "The last name should contain character of words")
        if(validate_string_data_type(othername) is False):
            return return_error(400, "The other name should contain character of words")
        if(check_email_validity(email) is False):
            return return_error(400, "Enter the correct email format")
        if(check_phone_number_validity(phone_number) is False):
            return return_error(400, "Enter a correct phone number starts with a zero or +254")
        if(check_is_valid_url(passport_url) is False):
            return return_error(400, "The passport url should be of correct format should be of format https://myimage.com")

        if(sanitize_input(firstname) == False):
            return return_error(400, "Provide a valid first name it should not contain any spaces")
        if(sanitize_input(lastname) == False):
            return return_error(400, "Provide a valid last name, it should not contain any spaces")
        if(sanitize_input(othername) == False):
            return return_error(400, "Provide a valid other name,it should not contain any spaces ")
        if(validate_password(password) == False):
            return return_error(400,\
                 "Password should be more than six characters contain at least a number and uppercase letter")

    except KeyError as e:
        return return_error(400, "An error occurred while creating user  {} is missing".format(e.args[0]))
    pass_hash = generate_password_hash(password)
    user = User(email=email, password=pass_hash, firstname=firstname,\
        lastname=lastname, othername=othername, phone_number=phone_number,\
             passport_url=passport_url)
    if user.create_user():
        return make_response(jsonify({
            "status":201,
            "data" :[{
                "user":{
                    "email":user.email,
                    "firstname": user.firstname,
                }
            }]
        }),201)
    return return_error(409, "User already exists")

# login
@AUTH_BLUEPRINT.route('/auth/login', methods=["POST"])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if(check_email_validity(email) is False):
        return return_error(400, "Add a valid email address")
    if(validate_password(password) is False):
        return return_error(400,"Password should be more than six characters")

    user = User(email=None, password=None, firstname=None,\
        lastname=None, othername=None, phone_number=None,\
             passport_url=None)
    check_user = user.get_user(email=email)
    user = json.loads(check_user)
    if not user:
        return return_error(404, "User is not found")
    check_password= check_password_hash(user[7],password)
    if check_password:
        token = create_access_token({
            'user_id': user[0], 'is_admin':user[8]
        }, expires_delta=datetime.timedelta(minutes=15))
        if token:
            return make_response(jsonify({
                "email":email,
                "token": token,
            }), 200)
    else:
        return return_error(401, "Ensure you input valid email and password")
