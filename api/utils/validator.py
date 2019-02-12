"""validation functions"""
import re
from flask import jsonify, make_response

def sanitize_input(input_data):
    """check if input is of alphanumeric characters"""
    if input_data.isalpha() == False:
        return False
def validate_int_data_type(data_passed):
    """ ensures the inputs are of int  type"""
    if not isinstance(data_passed, int):
        return False
    return True
def validate_string_data_type(data_passed):
    """ensures the input passed is of str type."""
    if not isinstance(data_passed, str):
        return False
    return True
def generate_id(list_of_items):
    """generates the id of a new item given a list"""
    return len(list_of_items) +1
def return_error(status_code, message):
    """ function to format the response """
    response = {
        "status": status_code,
        "error": message,
    }
    return make_response(jsonify(response), status_code)
def return_response(status_code, message, data=list()):
    """ function to format the response """
    response = {
        "status": status_code,
        "message": message,
        "data": data,
    }
    return make_response(jsonify(response), status_code)
def check_json_party_keys(request):
    """checks if keys of the payload are correct"""
    request_keys = ["name", "hqAddress", "logoUrl"]
    errors = []
    for key in request_keys:
        if not key in request.json:
            errors.append(key)
        return errors

def validate_office_type(data):
    """ensures the office name is of the defined parameters"""
    accepted = ["federal", "legislative", "local", "state"]
    if data not in accepted:
        return False
    return True

def check_json_office_keys(request):
    """checks if keys of the office payload is correct"""
    request_keys = ["name", "office_type"]
    errors = []
    for key in request_keys:
        if not key in request.json:
            errors.append(key)
        return errors


# check if the url is of correct format
def check_is_valid_url(url):
    """check if the url provided is valid"""
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
               url):
       return True
    return False