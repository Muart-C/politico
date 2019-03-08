import datetime
import json
import re
from flask import Blueprint, current_app, request, make_response, jsonify
from flask_jwt_extended import create_access_token
from flask_sendgrid import SendGrid
from werkzeug.security import check_password_hash, generate_password_hash
from api.utils.validator import check_json_new_user_keys,\
     return_error, validate_string_data_type,\
         sanitize_input, check_email_validity, check_is_valid_url,\
             check_phone_number_validity,validate_password,\
             return_response

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
            return return_error(400, "Enter a correct phone number with the following format 123-123-3333")
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
        return return_error(400,"Password should be more than six characters, also must contain at least one upper case letter and a number")

    user = User(email=None, password=None, firstname=None,\
        lastname=None, othername=None, phone_number=None,\
             passport_url=None)
    user = user.get_user(email=email)
    if not user:
        return return_error(404, "User is not found")
    check_password= check_password_hash(user['password'],password)
    if check_password:
        token = create_access_token({
            "id" : user["id"],
            "is_admin" : user["is_admin"]
        }, expires_delta=None)
        if token:
            return make_response(jsonify({
                "email":email,
                "token": token,
                "is_admin": user["is_admin"],
            }), 200)
        return return_error("An error occurred when forming a token")
    else:
        return return_error(401, "Ensure you input valid email and password")

@AUTH_BLUEPRINT.route('/users', methods=['GET'])
def get_users():
    """get all the users"""
    user = User(email=None, password=None, firstname=None,\
        lastname=None, othername=None, phone_number=None,\
             passport_url=None)
    users = user.get_users()
    if users:
        return return_response(200, "Request was successful", users)
    return return_response(200, "No government users were found register an office", users)

@AUTH_BLUEPRINT.route('/auth/reset', methods=['POST'])
def send_reset_link():
    data = request.get_json()
    email = data['email']
    if(check_email_validity(email) is False):
        return return_error(400, "Enter the correct email format i.e should contain @ and .")
    user = User(email=None, password=None, firstname=None,\
        lastname=None, othername=None, phone_number=None,\
             passport_url=None)
    user = user.get_user(email=email)
    if not user:
        return return_error(404, "User with that email does not exist kindly register")
    mail_instance = SendGrid(current_app)
    token = create_access_token({
        "id" : user["id"],
        }, expires_delta= datetime.timedelta(days=5))
    reset_link = '''
    https://muart-c.github.io/politico/UI/password_reset.html?token={}
    '''.format(token)
    mail_instance.send_email(
        from_email='administrator@politico.com',
        to_email=email,
        subject='Hello {} Kindly reset your password'.format(user['firstname']),
        html='''Click this link to reset your password {}'''.format(reset_link)
    )
    return make_response(jsonify({
        "email":email,
        "message" : "Check your email for the reset link",
        }), 200)

@AUTH_BLUEPRINT.route('/reset', methods=['POST'])
def change_password():
    data = request.get_json()
    if not data:
        return return_error(400, "ensure you pass the correct data")
    email = data['email']
    password = data['password']
    if(check_email_validity(email) is False):
        return return_error(400, "Add a valid email address")
    if(validate_password(password) is False):
        return return_error(400,"Password should be more than six characters, also must contain at least one upper case letter and a number")

    user = User(email=None, password=None, firstname=None,\
        lastname=None, othername=None, phone_number=None,\
             passport_url=None)
    user = user.get_user(email=email)
    if not user:
        return return_error(404, "User with that email address was not found please register as a new user")
    user = User(email=None, password=None, firstname=None,\
        lastname=None, othername=None, phone_number=None,\
             passport_url=None)
    hash_password = generate_password_hash(password)
    update_password = user.update_password(email, hash_password)
    if update_password:
        return return_response(200, "Your password was successfully update login using your new password")
    return return_error(400, "An error occurred while updating your password please proceed to reset your password again")