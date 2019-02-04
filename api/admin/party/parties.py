from flask import Blueprint, jsonify, request
from api.admin.party.model import Party

#initialize a party blueprint
party_blueprint = Blueprint('parties', __name__)

#create a party route
@party_blueprint.route('/parties', methods=['POST'])
def add_parties():
    try:
        data = request.get_json()
        Id = data.get('Id')
        name = data.get('name')
        hqAddress = data.get('hqAddress')
        logoUrl = data.get('logoUrl')
    except:
        return jsonify({
            "status" : 400,
            "error" : "invalid request payload"
        })
    
    #initialize an instance of a party
    party = Party(Id, name, hqAddress, logoUrl)

    #add party to list data structure
    party.add_party()

    #return a json response with the data payload
    response = {
        "status" : 201,
        "data" : [{
            "Id" : Id,
            "name" : name,
            "hqAddress" : hqAddress,
            "logoUrl" : logoUrl
        }],
        "success" : "party {} was added".format(name),
    }
    return jsonify(response), 201
    