from flask import Blueprint, jsonify, request
from api.admin.party.model import Party, parties

#initialize a party blueprint
party_blueprint = Blueprint('parties', __name__)

#create a party route
@party_blueprint.route('/parties', methods=['POST'])
def add_parties():
    try:
        data = request.get_json()
        name = data.get('name')
        hqAddress = data.get('hqAddress')
        logoUrl = data.get('logoUrl')

        if not logoUrl and not name and not hqAddress:
            return jsonify({
                "status" : 400,
                "error" : "Please fill in all the required fields",
            }), 400

        if not name:
            return jsonify({"status" : 400,
             "error" : "Please add your name"}),400
        if not hqAddress:
            return jsonify({
                "status" : 400,
                "error" : "Please the parties headquarter",
            }), 400
        if not logoUrl:
            return jsonify({
                "status" : 400,
                "error" : "Please add your logo",
            }), 400

    except:
        return jsonify({
            "status" : 400,
            "error" : "invalid request payload"
        })

    #return a json response with the data payload of the details
    response = Party().add_party(name, hqAddress, logoUrl)
    return jsonify({
        "status" : 201,
        "data" : response,
        "success" : "party {} was added".format(name)
    }), 201

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
        political_parties_response = {
            "status" : 200,
            "data" : political_parties,
            "success" : "get request is for parties successful",
        }
        return jsonify(political_parties_response), 200

    #incase the request is unsuccessful json error response is returned
    return jsonify({"status": 404, "error": "the party list was empty"}), 404

#get a particular party route
@party_blueprint.route('/parties/<int:Id>', methods=['GET'])
def get_party(Id):
    """get a particular party."""
    #initialize a party model
    political_party = Party()

    #get a party
    party = political_party.get_party(Id)
    print(party)
    #checks if the party exists then returns the party as a json response
    if party:
        return jsonify({
            "status" : 200,
            "data" : [party],
            "success" : "request was successful and a result was returned",
        })
    #incase the request is unsuccessful json error response is returned
    return jsonify({"status": 404, "error": "no party with that id was found"}), 404

#update the name route
@party_blueprint.route('/parties/<int:party_id>/name', methods=['PATCH'])
def change_name(party_id):
    data = request.get_json()
    name = data.get('name')


    #initialize the Party model class
    political_party = Party()

    #retrieve a particular party of provided id
    party = political_party.get_party(party_id)

    #checks if the party exists then modifies the party name and returns the required json response
    if party:
        data['name'] = name
        return jsonify({
            "status": 200,
            "data": [
                {
                    "id" : party_id,
                    "name" : name,
                }]}), 200
    #incase the request is unsuccessful json error response is returned
    return jsonify({"status": 404, "error": "party name not modified"}), 404

#delete a party route
@party_blueprint.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):

    #initialize the party model
    party = Party()

    #get party of the provided id
    party_delete = party.get_party(party_id)
    print(party_delete)
    #check if the party to delete exist in the model
    if party_delete:
        parties.remove(party_delete[0])
        return jsonify({
            "status" : 204,
            "data" : [
                {"message" : "party was deleted"},
            ]
        }), 204
    #if party not in list return error
    return jsonify({"status": 404, "error": "error processing your request"}), 404

