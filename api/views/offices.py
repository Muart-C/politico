""""!api/admin/office/offices/py """
import json
from flask import Blueprint, request, make_response, jsonify
from api.models.offices_model import Office
from api.models.candidates_model import Candidate
from api.models.users_model import User
from api.models.parties_model import Party
from api.utils.validator import return_response, return_error, check_json_office_keys
from api.utils.validator import validate_string_data_type, sanitize_input
from api.utils.validator import validate_int_data_type, validate_office_type,\
    check_json_new_candidate_keys

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

    office = Office(name=name, office_type=office_type)
    office = office.create_office()
    if office:
        return make_response(jsonify({
            "status":201,
            "message":"office {} created successfully".format(name),
            "data": [{
                "name" : name,
                "office_type":office_type
            }]
        }))
    #if not success return error
    return return_error(400, "the office already exist create another office")

#get all offices route
@OFFICE_BLUEPRINT.route('/offices', methods=['GET'])
def get_offices():
    """get all the offices"""

    #initialize an office data model
    offices = Office(name=None, office_type=None)

    #get a list of all  offices
    political_offices = offices.get_offices()

    #checks if a list of political offices exists then returns it
    if political_offices:
        return return_response(200, "request was successful", political_offices)
    #incase the request is unsuccessful json error response is returned
    return return_error(400, "there are no offices registered")

#get a particular office route endpoint
@OFFICE_BLUEPRINT.route('/offices/<int:id>', methods=['GET'])
def get_office(id):
    """get a particular political office."""
    if(validate_int_data_type(id) == False):
        return return_error(400, "please provide id which is a number")

    #initialize an office data structure
    political_office = Office(name=None, office_type=None)

    #get an office with the id passed
    office = political_office.get_office(id)

    office = json.loads(office)

    #if the office exists then return it as json response
    if office:
        return return_response(200, "request was successful", office)
    #return error response
    return return_error(404,"no office with that id was found")



# create candidate route
@OFFICE_BLUEPRINT.route('/offices/<int:office_id>/register', methods=["POST"])
def create_candidate(office_id):
    """create a new candidate."""
    key_errors=check_json_new_candidate_keys(request)
    if key_errors:
        return return_error(400, "Invalid keys provided")
    try:
        data = request.get_json()
        # validate data from the request
        party_id=data['party_id']
        candidate_id=data['candidate_id']

        if(validate_int_data_type(party_id) == False):
            return return_error(400, "provide an Id for party that is a number")
        if(validate_int_data_type(candidate_id) == False):
            return return_error(400, "provide an Id for a candidate that is a number")


    except KeyError as e:
        return return_error(400, "an error occurred {}\
             is missing".format(e.args[0]))

    # check if user whose id was given exists before attempting candidate registration
    user = User()
    result = user.get_user_by_id(candidate_id)
    user = json.loads(result)

    # check if party whose id was given exists before attempting candidate registration
    party = Party(name=None,hq_address=None, logo_url=None)
    result = party.get_party(party_id)
    party = json.loads(result)

    # check if an whose id was given exists before attempting candidate registration
    office = Office(name=None, office_type=None)
    result = office.get_office(office_id)
    office = json.loads(result)

    if office and party and user:
        candidate = Candidate(office_id=office_id, candidate_id=candidate_id,\
             party_id=party_id)
	    #check if candidate is already registered
        new = candidate.create_a_candidate()
        if new:
            return make_response(jsonify({
            "status":201,
            "message":"candidate created",
            "data": [{
                "office" : office_id,
                "user":candidate_id,
            }]
        }))
        return return_error(400, "candidate already exist")
    else:
        return return_error(400, "you cannot register a candidate if either a user or party or office is not registered ")



# # create candidate route
# @OFFICE_BLUEPRINT.route('/offices/<int:office_id>/results', methods=["GET"])
# def get_results(office_id):
#     """gets the results of an election."""
#     if(validate_int_data_type(office_id) is False):
#         return return_error(400, "provide a office id")

#     office = Office()
#     result = office.get_office(office_id)
#     if result:
#         vote = Vote(office_id=office_id, user_id=None, candidate_id=None)
# 	    #check if candidate is already registered
# 	    election_result = vote.get_vote_results(office_id)
# 	    if election_result:
#             return return_error(200, "request successful results found", election_result)
#     	return return_error(400, "an error occurred while fetching results")
#     return return_error(400, "no such office that exists therefore no results")





