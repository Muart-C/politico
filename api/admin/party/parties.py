from flask import Blueprint, jsonify, request
from api.admin.party.model import Party, parties
from api.utils.validator import return_response,validate_string_data_type, validate_int_data_type

#initialize a party blueprint
party_blueprint = Blueprint('parties', __name__)

#create a party route
@party_blueprint.route('/parties', methods=['POST'])
def add_parties():
        data = request.get_json()

        if not data:
            return return_response(400, "fill in all the required values")
        try:
            # validate data from the request
            name =  data['name']
            hqAddress =  data['hqAddress']
            logoUrl = data['logoUrl']

            if(validate_string_data_type(name) == False):
                return return_response(400, "the name cannot be empty")

            if(validate_string_data_type(hqAddress) == False):
                return return_response(400, "the HQ cannot be empty")

            if(validate_string_data_type(logoUrl) == False):
                return return_response(400, "the Logo is needed add the url")


        except KeyError as e:
            return return_response(400, "an error occurred while creating party {} is missing".format(e.args[0]))

        party = Party()
        party=party.add_party(name=name, hqAddress=hqAddress, logoUrl=logoUrl)
        if party:
            return return_response(201, "party {} was created".format(name), party)
        #if not success return error
        return return_response(400, "an error occurred while creating party")
#get all parties route
@party_blueprint.route('/parties', methods=['GET'])
def get_parties():
    """get all political parties"""

    #initialize the party model
    parties = Party()
    #get a list of all political parties
    political_parties = parties.get_parties()
    #checks if a list of political parties exists then returns it as a json response
    if political_parties:
        return return_response(200, "get request is for parties successful", [political_parties])
    #incase the request is unsuccessful json error response is returned
    return return_response(400, "the party list was empty")

#get a particular party route
@party_blueprint.route('/parties/<int:id>', methods=['GET'])
def get_party(id):
    """get a particular party."""

    if(validate_int_data_type(id) == False):
        return return_response(400, "please provide id of correct type")

    #initialize a party model
    political_party = Party()

    #get a party
    party = political_party.get_party(id)

    #checks if the party exists then returns the party as a json response
    if party:
        return return_response(200,"a party with the id was returned", [party])

    #incase the request is unsuccessful json error response is returned
    return return_response(400, "no party with that id was found")

#update the name route
@party_blueprint.route('/parties/<int:party_id>/<string:name>', methods=['PATCH'])
def change_name(party_id, name):
    try:
        if(validate_string_data_type(name)== False):
            return return_response(400, "the name should of string data type")
    except KeyError as e:
            return return_response(400, "an error the party {} is missing".format(e.args[0]))

    #initialize the Party model class
    political_party = Party()

    #retrieve a particular party of provided id
    updated_party = political_party.update_party(party_id, name)

    #checks if the party exists then modifies the party name and returns the required json response
    if updated_party:
        return return_response(200, "party name was updated", [updated_party])
    #incase the request is unsuccessful json error response is returned
    return return_response(400, "party name not modified an error occurred")

#delete a party route
@party_blueprint.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):

    #initialize the party model
    party = Party()

    #get party of the provided id
    party_delete = party.get_party(party_id)[0]
    print(party_delete)
    #check if the party to delete exist in the model
    if party_delete:
        parties.remove(party_delete)
        return 204
    #if party not in list return error
    return jsonify({"status": 404, "error": "error processing your request"}), 404

