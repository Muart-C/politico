""""!api/admin/office/offices/py """
from flask import Blueprint, request
from api.models.offices_model import Office, OFFICES
from api.utils.validator import return_response, return_error, check_json_office_keys
from api.utils.validator import validate_string_data_type, sanitize_input
from api.utils.validator import validate_int_data_type, validate_office_type

#initialize an office blueprint
OFFICE_BLUEPRINT = Blueprint('offices', __name__)

#create post office route
@OFFICE_BLUEPRINT.route('/offices', methods=['POST'])
def add_offices():
    """post office"""

    key_errors=check_json_office_keys(request)
    if key_errors:
        return return_error(400, "Invalid keys provided")
    try:
        data = request.get_json()
        # validate data from the request
        name=data['name']
        office_type=data['office_type']

        if(validate_string_data_type(name) == False):
            return return_error(400, "the name should be a string")
        if(validate_string_data_type(office_type) == False):
            return return_error(400, "the office type should be of type string")

        if(sanitize_input(name) == False):
            return return_error(400, "provide a valid name")
        if(sanitize_input(office_type) == False):
            return return_error(400, "provide a valid office type")
        if(validate_office_type(office_type) == False):
            return return_error(400, "should be either legislative, federal, state or local")
    except KeyError as e:
        return return_error(400, "an error occurred while creating office  {} is missing".format(e.args[0]))

    office = Office()
    office = office.add_office(name=name, office_type=office_type)
    if office:
        return return_response(201, "office of {} was created".format(name), [office])
    #if not success return error
    return return_response(400, "an error occurred while creating an office")

#get all offices route
@OFFICE_BLUEPRINT.route('/offices', methods=['GET'])
def get_offices():
    """get all the offices"""

    #initialize an office data model
    offices = Office()

    #get a list of all  offices
    political_offices = offices.get_offices()

    #checks if a list of political offices exists then returns it
    if political_offices:
        return return_response(200, "request was successful", political_offices)
    #incase the request is unsuccessful json error response is returned
    return return_response(400, "there are no offices registered")

#get a particular office route endpoint
@OFFICE_BLUEPRINT.route('/offices/<int:id>', methods=['GET'])
def get_office(id):
    """get a particular political office."""
    if(validate_int_data_type(id) == False):
        return return_response(400, "please provide id of correct type")

    #initialize an office data structure
    political_office = Office()

    #get an office with the id passed
    office = political_office.get_office(id)

    #if the office exists then return it as json response
    if office:
        return return_response(200, "request was successful", [office])
    #return error response
    return return_response(404,"no office with that id was found")
