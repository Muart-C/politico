"""validation functions"""
import re
import jwt

import datetime
from flask import jsonify, make_response


def validate_password(password):
    passd=re.compile("(?=\D*\d)(?=[^A-Z]*[A-Z])(?=[^a-z]*[a-z])[A-Za-z0-9]{6,}$")
    if re.match(passd, password) is None:
        return False
    return True


def sanitize_input(input_data):
    if input_data.isalpha() == False:
        return False
    return True

def validate_int_data_type(data_passed):
    if not isinstance(data_passed, int):
        return False
    return True
def validate_string_data_type(data_passed):
    if not isinstance(data_passed, str):
        return False
    return True

def return_error(status_code, message):
    response = {
        "status": status_code,
        "error": message,
    }
    return make_response(jsonify(response), status_code)
def return_response(status_code, message, data={}):
    response = {
        "status": status_code,
        "message": message,
        "data": data,
    }
    return make_response(jsonify(response), status_code)
def check_json_party_keys(request):
    request_keys = ["name", "hqAddress", "logoUrl"]
    errors = []
    for key in request_keys:
        if not key in request.json:
            errors.append(key)
        return errors

def validate_office_type(data):
    accepted = ["federal", "legislative", "local", "state"]
    if data not in accepted:
        return False
    return True

def check_json_office_keys(request):
    request_keys = ["name", "office_type"]
    errors = []
    for key in request_keys:
        if not key in request.json:
            errors.append(key)
        return errors


# check if the url is of correct format
def check_is_valid_url(url):
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
               url):
       return True
    return False

def check_json_new_user_keys(request):
    user_keys = ["firstname", "lastname", "othername",\
        "email","phone_number","passport_url", "password"]
    errors = []
    for key in user_keys:
        if not key in request.json:
            errors.append(key)
        return errors


def check_json_new_votes_keys(request):
    vote_keys = ["candidate_id","office_id","user_id"]
    errors = []
    for key in vote_keys:
        if not key in request.json:
            errors.append(key)
        return errors

def check_email_validity(email):
    if re.match(r"(^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z0-9-.]+$)",
               email):
       return True
    return False


def check_phone_number_validity(phone):
    if re.match(r"^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$", phone):
        return True
    return False
