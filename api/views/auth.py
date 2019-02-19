import json
import re
from flask import Blueprint, request, make_response, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from api.utils.validator import check_json_new_user_keys,\
     return_error, validate_string_data_type,\
         sanitize_input, check_email_validity, check_is_valid_url\

from api.utils.validator import validate_password, encode_auth_token
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
            return return_error(400, "enter the correct email format i.e should contain @ and .")
        if(validate_string_data_type(firstname) is False):
            return return_error(400, "the first name should contain character of words")
        if(validate_string_data_type(lastname) is False):
            return return_error(400, "the last name should contain character of words")
        if(validate_string_data_type(othername) is False):
            return return_error(400, "the other name should contain character of words")
        if(check_email_validity(email) is False):
            return return_error(400, "enter the correct email format")
        if(validate_string_data_type(phone_number) is False):
            return return_error(400, "enter a correct phone number")
        if(check_is_valid_url(passport_url) is False):
            return return_error(400, "the passport url should be of correct format should be of format https://myimage.com")

        if(sanitize_input(firstname) == False):
            return return_error(400, "provide a valid first name it should not contain any spaces")
        if(sanitize_input(lastname) == False):
            return return_error(400, "provide a valid last name, it should not contain any spaces")
        if(sanitize_input(othername) == False):
            return return_error(400, "provide a valid other name,it should not contain any spaces ")
        if(validate_password(password) == False):
            return return_error(400,\
                 "password should be more than six characters")

    except KeyError as e:
        return return_error(400, "an error occurred while creating user  {} is missing".format(e.args[0]))
    pass_hash = generate_password_hash(password)
    user = User(email=email, password=pass_hash, firstname=firstname,\
        lastname=lastname, othername=othername, phone_number=phone_number,\
             passport_url=passport_url)
    if user.create_user():
        token = encode_auth_token(email)
        return make_response(jsonify({
            "status":201,
            "token":token.decode("utf-8"),
            "data" :[{
                "user":{
                    "email":user.email,
                    "firstname": user.firstname,
                }
            }]
        }),201)
    return return_error(409, "the user you are trying to register already exists")

# login
@AUTH_BLUEPRINT.route('/auth/login', methods=["POST"])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if(check_email_validity(email) is False):
        return return_error(400, "add a valid email address")
    if(validate_password(password) is False):
        return return_error(400,"password should be more than six characters")

    user = User(email=None, password=None, firstname=None,\
        lastname=None, othername=None, phone_number=None,\
             passport_url=None)
    check_user = user.get_user(email=email)
    user = json.loads(check_user)
    if not user:
        return return_error(404, "the user you are trying to get does not exist")
    check_password= check_password_hash(user[7],password)
    if check_password:
        token = encode_auth_token(email)
        if token:
            return make_response(jsonify({
                    "status":200,
                    "data":[{
                            "email":email,
                            "token": token.decode("utf-8"),
                    }],
            }), 200)
    else:
        return return_error(404, "ensure you input valid email and password")
