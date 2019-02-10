""""!api/admin/office/offices/py """
from flask import Blueprint, jsonify, request
from api.models.offices_model import Office, OFFICES
from api.utils.validator import return_response
from api.utils.validator import validate_string_data_type
from api.utils.validator import validate_int_data_type

#initialize an office blueprint
OFFICE_BLUEPRINT = Blueprint('offices', __name__)

#create post office route
@OFFICE_BLUEPRINT.route('/offices', methods=['POST'])
def add_offices():
    """post office"""
    data = request.get_json()

    if not data:
        return return_response(400, "fill in all the required values")
    try:
        # validate data from the request
        name=data['name']
        office_type=data['office_type']

        if(validate_string_data_type(name) == False):
            return return_response(400, "the name cannot be empty")
        if(validate_string_data_type(office_type) == False):
            return return_response(400, "the office type cannot be empty")

    except KeyError as e:
        return return_response(400, "an error occurred while creating office  {} is missing".format(e.args[0]))

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
    return return_response(400, "an error occurred while processing your request")

#get a particular office route endpoint
@OFFICE_BLUEPRINT.route('/offices/<int:Id>', methods=['GET'])
def get_office(Id):
    """get a particular political office."""
    if(validate_int_data_type(Id) == False):
        return return_response(400, "please provide id of correct type")

    #initialize an office data structure
    political_office = Office()

    #get an office with the id passed
    office = political_office.get_office(Id)
    print(office)
    #if the office exists then return it as json response
    if office:
        return return_response(200, "request was successful", [office])
    #return error response
    return return_response(404,"no office with that id was found")
