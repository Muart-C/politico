from flask import Blueprint, jsonify, request
from api.admin.party.model import Party

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
    except:
        return jsonify({
            "status" : 400,
            "error" : "invalid request payload"
        })
    
    #initialize an instance of a party
    # party = Party()

    #add party to list data structure
    

    #return a json response with the data payload
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

    political_parties_response = {
        "status" : 200,
        "data" : political_parties,
        "success" : "get request is for parties successful",
    }

    return jsonify(political_parties_response), 200

#get a particular party route
@party_blueprint.route('/parties/<int:Id>', methods=['GET'])
def get_party(Id):
    """get a particular party."""
    
    #initialize a party model
    #political_party = Party()

    #get a party
    party = Party().get_party(Id)

    if party:
        return jsonify({
            "party" : party,
            "success" : "request was successful and a result was returned",
    }) 

