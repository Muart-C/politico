from flask import Blueprint, jsonify, request
from api.admin.office.model import Office

#initialize a office blueprint
office_blueprint = Blueprint('offices', __name__)

#create a office route
@office_blueprint.route('/offices', methods=['POST'])
def add_offices():
    try:
        data = request.get_json()
        name = data.get('name')
        office_type = data.get('office_type')
    #returns an error response incase the body of the post request is empty
    except:
        return jsonify({
            "status" : 400,
            "error" : "invalid request payload"
        })
    
    #return a json response with the data payload of the details
    response = Office().add_office(name, office_type)
    return jsonify({
        "status" : 201,
        "data" : response,
        "success" : "office {} was added".format(name)
    }), 201

#get all offices route    
@office_blueprint.route('/offices', methods=['GET'])
def get_offices():
    """get all political offices"""

    #initialize the office model
    offices = Office()

    #get a list of all political offices
    political_offices = offices.get_offices()

    #checks if a list of political offices exists then returns it as a json response
    if political_offices:
        political_offices_response = {
            "status" : 200,
            "data" : political_offices,
            "success" : "get request is for offices successful",
        }
        return jsonify(political_offices_response), 200


    #incase the request is unsuccessful json error response is returned
    return jsonify({
        "status": 404, 
        "error": "the office list was empty"
        }), 404 
    
#get a particular office route
@office_blueprint.route('/offices/<int:Id>', methods=['GET'])
def get_office(Id):
    """get a particular office."""
    
    #initialize a office model
    political_office = Office()

    #get a office
    office = political_office.get_office(Id)

    #checks if the office exists then returns the office as a json response
    if office:
        return jsonify({
            "status" : 200,
            "data" : [office],
            "success" : "request was successful and a result was returned",
        })
    #incase the request is unsuccessful json error response is returned
    return jsonify({"status": 404, "error": "no office with that id was found"}), 404 
