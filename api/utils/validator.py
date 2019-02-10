"""validation functions"""
from flask import jsonify, make_response


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

def return_response(status_code, message, data=list()):
    """ function to format the response """
    response = {
        "status": status_code,
        "message": message,
        "data": data,
    }
    return make_response(jsonify(response), status_code)

# def checks_if_exist(key, value, collection_of_items):
#     """check if the value of the key attribute passed exists."""
#     return [item for item in collection_of_items if item[key] == value and  len(item) > 0]
