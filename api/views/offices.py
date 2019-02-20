import json
from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models.offices_model import Office
from api.models.candidates_model import Candidate
from api.models.users_model import User
from api.models.parties_model import Party
from api.utils.validator import return_response, return_error, check_json_office_keys
from api.utils.validator import validate_string_data_type, sanitize_input
from api.utils.validator import validate_int_data_type, validate_office_type


OFFICE_BLUEPRINT = Blueprint('offices', __name__)

@OFFICE_BLUEPRINT.route('/offices', methods=['POST'])
@jwt_required
def add_offices():
    """post office"""
    current_user = get_jwt_identity()
    if current_user['is_admin']:
        try:
            data = request.get_json()
            name=data['name']
            office_type=data['office_type']

            if(validate_string_data_type(name) == False):
                return return_error(400, "The name should contain characters that form a word")
            if(validate_string_data_type(office_type) == False):
                return return_error(400, "The office type should contain characters that form a word")
            if(sanitize_input(name) == False):
                return return_error(400, "Provide a valid name i.e it should not contain spaces in between characters other than a word that makes sense")
            if(sanitize_input(office_type) == False):
                return return_error(400, "Provide a valid office type i.e it should not contain spaces in between characters other than a word that makes sense")
            if(validate_office_type(office_type) == False):
                return return_error(400, "Should be either legislative, federal, state or local")
        except KeyError as e:
            return return_error(400, "An error occurred while creating office  {} is missing".format(e.args[0]))

        office = Office(name=name, office_type=office_type)
        office = office.create_office()
        if office:
            return make_response(jsonify({
                "status":201,
                "message":"Office {} created successfully".format(name),
                "data": [{
                    "name" : name,
                    "office_type":office_type
                }]
            }),201)
        return return_error(400, "The office already exist create another office")

    return make_response(jsonify({
            "status":401,
            "message": "You are not authorized to perform this action"
        }), 401)


@OFFICE_BLUEPRINT.route('/offices', methods=['GET'])
def get_offices():
    """get all the offices"""
    offices = Office(name=None, office_type=None)
    political_offices = offices.get_offices()
    if political_offices:
        return return_response(200, "Request was successful", political_offices)
    return return_error(400, "There are no offices found")


@OFFICE_BLUEPRINT.route('/offices/<int:id>', methods=['GET'])
def get_office(id):
    if(validate_int_data_type(id) == False):
        return return_error(400, "Please provide id which is a number")
    political_office = Office(name=None, office_type=None)

    office = political_office.get_office(id)

    office = json.loads(office)

    if office:
        return make_response(jsonify({
            "status":200,
            "message":"Office was successfully retrieved",
            "data": [{
                "name" : office[1],
                "office_type":office[2]
            }]
        }), 200)
    return return_error(404,"No office with that id was found")

@OFFICE_BLUEPRINT.route('/offices/<int:office_id>/register', methods=["POST"])
@jwt_required
def create_candidate(office_id):
    current_user = get_jwt_identity()
    if current_user['is_admin']:
        try:
            data = request.get_json()
            party_id=data['party_id']
            candidate_id=data['candidate_id']

            if(validate_int_data_type(party_id) == False):
                return return_error(400, "Provide an Id for party that is a number")
            if(validate_int_data_type(candidate_id) == False):
                return return_error(400, "Provide an Id for a candidate that is a number")

        except KeyError as e:
            return return_error(400, "An error occurred {}\
                is missing".format(e.args[0]))

        user = User()
        result = user.get_user_by_id(candidate_id)
        user = json.loads(result)

        if not user:
            return return_error(404, "User does not exist")

        party = Party(name=None,hq_address=None, logo_url=None)
        result = party.get_party(party_id)
        party = json.loads(result)

        if not party:
            return return_error(404, "The party does not exist")

        office = Office(name=None, office_type=None)
        result = office.get_office(office_id)
        office = json.loads(result)
        if not office:
            return return_error(404, "The office does not exist")

        candidate = Candidate(office_id=office_id, candidate_id=candidate_id,\
                party_id=party_id)
        result = candidate.get_candidate(candidate_id)
        candidate = json.loads(result)
        if not candidate:
            new = candidate.create_a_candidate()
            if new:
                return make_response(jsonify({
                    "status":201,
                    "message":"The candidate was created",
                    "data": [{
                        "office_id" : office_id,
                        "candidate_id":candidate_id,
                    }]

                }),201)
            return return_error(400, "An error occurred while registering the candidate")
        return return_error(409, "Candidate already registered for that party")
    return return_error(401, "You are not authorized to perform this action")