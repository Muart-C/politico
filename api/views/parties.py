import json
from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models.parties_model import Party
from api.utils.validator import return_response, validate_string_data_type, check_json_party_keys
from api.utils.validator import return_error, validate_int_data_type, sanitize_input
from api.utils.validator import check_is_valid_url


PARTY_BLUEPRINT = Blueprint('parties', __name__)

@PARTY_BLUEPRINT.route('/parties', methods=['POST'])
@jwt_required
def add_parties():
    current_user = get_jwt_identity()
    if current_user['is_admin']:
        try:
            data = request.get_json()
            name=data['name']
            hqAddress=data['hqAddress']
            logoUrl=data['logoUrl']

            if(validate_string_data_type(name) == False):
                return return_error(400, "The name should contain should be a word")
            if(validate_string_data_type(hqAddress) == False):
                return return_error(400, "The address contain should be a word")
            if(check_is_valid_url(logoUrl) == False):
                return return_error(400, "The Logo url is not in the correct url format")

            if(sanitize_input(name)) == False:
                return return_error(400, "Please enter a valid name nb:should be a word")
            if (sanitize_input(hqAddress)) == False:
                return return_error(400, "The headquarter address should be a word")
        except KeyError as e:
            return return_response(400, "An error occurred while creating party {} is missing".format(e.args[0]))

        party = Party(name,hqAddress, logoUrl)
        party = party.create_a_party()
        if party:
            return make_response(jsonify({
                "status":201,
                "message":"Party {} created successfully".format(name),
                "data": [{
                    "name" : name,
                    "hq_address":hqAddress
                }]
            }), 201)
        return return_error(409, "The party already exists")
    return make_response(jsonify({
            "status":401,
            "message": "you are not authorized to perform this action"
        }), 401)


@PARTY_BLUEPRINT.route('/parties', methods=['GET'])
def get_parties():
    parties = Party(name=None, hq_address=None, logo_url=None)
    registered_parties=parties.get_parties()
    if registered_parties:
        return return_response(200, "The request to get a list for parties was successful", registered_parties)
    return return_response(200, "No parties were found register a party", registered_parties)

@PARTY_BLUEPRINT.route('/parties/<int:id>', methods=['GET'])
def get_party(id):
    if(validate_int_data_type(id) == False):
        return return_error(400, "Please provide the id")
    political_party = Party(name=None, hq_address=None, logo_url=None)
    party = political_party.get_party(id)
    party = json.loads(party)
    if party:
        return make_response(jsonify({
            "status":200,
            "message":"The party was found",
            "data": [{
                "name" : party[1],
                "hq_address":party[2]
            }]
        }), 200)
    return return_error(404, "Party was not found")

@PARTY_BLUEPRINT.route('/parties/<int:party_id>/name', methods=['PATCH'])
@jwt_required
def change_name(party_id):
    current_user = get_jwt_identity()
    if current_user['is_admin']:
        try:
            data = request.get_json()
            name=data["name"]
            if(validate_string_data_type(name)== False):
                return return_error(400, "The name should contain a character of words")
            if(sanitize_input(name) is False):
                return return_error(400, "Please enter a valid name i.e should not contain spaces or unrecognized characters")
        except KeyError as e:
                return return_error(400, "An error the party {} is missing".format(e.args[0]))

        political_party = Party(name=name, hq_address=None, logo_url=None)

        updated_party = political_party.patch_party_name(party_id)

        if updated_party:
            return return_response(200, "The party name was updated", updated_party)
        return return_error(404, "The party was not found")
    else:
        return_error(401, "you are not authorized to perform this action")

@PARTY_BLUEPRINT.route('/parties/<int:party_id>', methods=['DELETE'])
@jwt_required
def delete_party(party_id):
    current_user =  get_jwt_identity()
    if current_user['is_admin']:
        try:
            if(validate_int_data_type(party_id) is False):
                return return_response(400, "Pass the correct party id")
        except KeyError as e:
            return return_error(400, "An error occurred while fetching the {}".format(e.args[0]))

        party = Party(name=None, hq_address=None,logo_url=None)
        party = party.get_party(party_id)
        party = json.loads(party)
        if party:
            party_del = Party(name=None, hq_address=None,logo_url=None)
            party_del.delete_party(party_id)
            return return_error(200, "The party was deleted successfully")
        return return_error(404, "Party was not found")
    else:
        return return_error(401, "you are not authorized to perform this action")
