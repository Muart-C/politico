import json
from flask import Blueprint, request, make_response, jsonify
from api.models.parties_model import Party
from api.utils.validator import return_response, validate_string_data_type, check_json_party_keys
from api.utils.validator import return_error, validate_int_data_type, sanitize_input
from api.utils.validator import check_is_valid_url


PARTY_BLUEPRINT = Blueprint('parties', __name__)

@PARTY_BLUEPRINT.route('/parties', methods=['POST'])
def add_parties():
    key_errors=check_json_party_keys(request)
    if key_errors:
        return return_error(400, "Invalid json keys please provided correct keys")
    try:
        data = request.get_json()
        name=data['name']
        hqAddress=data['hqAddress']
        logoUrl=data['logoUrl']

        if(validate_string_data_type(name) == False):
            return return_error(400, "the name should contain should be a word")
        if(validate_string_data_type(hqAddress) == False):
            return return_error(400, "the HQ contain should be a word")
        if(check_is_valid_url(logoUrl) == False):
            return return_error(400, "the Logo url is not in the correct url format")

        if(sanitize_input(name)) == False:
            return return_error(400, "please enter a valid name nb:should be a word")
        if (sanitize_input(hqAddress)) == False:
            return return_error(400, "the headquarter address should be a word")
    except KeyError as e:
        return return_response(400, "an error occurred while creating party {} is missing".format(e.args[0]))

    party = Party(name,hqAddress, logoUrl)
    party = party.create_a_party()
    if party:
        return make_response(jsonify({
            "status":201,
            "message":"party {} created successfully".format(name),
            "data": [{
                "name" : name,
                "hq_address":hqAddress
            }]
        }), 201)

    return return_error(409, "the party you are trying to register already exists")


@PARTY_BLUEPRINT.route('/parties', methods=['GET'])
def get_parties():
    parties = Party(name=None, hq_address=None, logo_url=None)
    registered_parties=parties.get_parties()

    if registered_parties:
        return return_response(200, "the request to get a list for parties was successful", registered_parties)
    return return_error(200, "there are no parties registered yet")

@PARTY_BLUEPRINT.route('/parties/<int:id>', methods=['GET'])
def get_party(id):
    if(validate_int_data_type(id) == False):
        return return_error(400, "please provide the id as a number")
    political_party = Party(name=None, hq_address=None, logo_url=None)
    party = political_party.get_party(id)
    party = json.loads(party)
    if party:
        return make_response(jsonify({
            "status":200,
            "message":"party was successfully retrieved",
            "data": [{
                "name" : party[1],
                "hq_address":party[2]
            }]
        }), 200)
    return return_error(404, "no party with that id was found")

@PARTY_BLUEPRINT.route('/parties/<int:party_id>/name', methods=['PATCH'])
def change_name(party_id):
    try:
        data = request.get_json()
        name=data["name"]
        if(validate_string_data_type(name)== False):
            return return_error(400, "the name should contain a character of words")
        if(sanitize_input(name) is False):
            return return_error(400, "please enter a valid name i.e should not contain spaces or unrecognized characters")
    except KeyError as e:
            return return_error(400, "an error the party {} is missing".format(e.args[0]))

    political_party = Party(name=name, hq_address=None, logo_url=None)

    updated_party = political_party.patch_party_name(party_id)

    if updated_party:
        return return_response(200, "the party name was updated", updated_party)
    return return_error(404, "the party you are trying to modify does not exist")

@PARTY_BLUEPRINT.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    try:
        if(validate_int_data_type(party_id) is False):
            return return_response(400, "pass the correct party id which should be a number")
    except KeyError as e:
        return return_error(400, "an error occurred while fetching the {}".format(e.args[0]))

    party = Party(name=None, hq_address=None,logo_url=None)
    party = party.get_party(party_id)
    if party:
        party.delete_party(party_id)
        return return_response(200, "the party was deleted successfully")

    return return_error(404, "party of that id does not exist create one before attempting to delete")
