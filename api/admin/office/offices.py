from flask import Blueprint, jsonify, request
from api.admin.office.model import Office

#initialize an office blueprint
office_blueprint = Blueprint('offices', __name__)

#create post office route
@office_blueprint.route('/offices', methods=['POST'])
def add_offices():
    try:
        data = request.get_json()
        name = data.get('name')
        office_type = data.get('office_type')

    #returns an error response incase of an error
    except:
        return jsonify({
            "status" : 400,
            "error" : "invalid request"
        })
    if not name or not office_type:
        return jsonify({
                "status" : 400,
                "error" : "Please fill in all the required fields",
            }), 400

    #return a json response of the office created
    response = Office().add_office(name, office_type)
    return jsonify({
        "status" : 201,
        "data" : response,
        "success" : "the office {} was added".format(name)
    }), 201

#get all offices route
@office_blueprint.route('/offices', methods=['GET'])
def get_offices():
    """get all the offices"""

    #initialize an office data model
    offices = Office()

    #get a list of all  offices
    political_offices = offices.get_offices()

    #checks if a list of political offices exists then returns it
    if political_offices:
        political_offices_response = {
            "status" : 200,
            "data" : political_offices,
            "success" : "get list of offices was successful",
        }
        return jsonify(political_offices_response), 200


    #if unsuccessful an error is returned
    return jsonify({
        "status": 404,
        "error": "request was unsuccessful"
        }), 404

#get a particular office route endpoint
@office_blueprint.route('/offices/<int:Id>', methods=['GET'])
def get_office(Id):
    """get a particular political office."""

    #initialize an office data structure
    political_office = Office()

    #get an office with the id passed
    office = political_office.get_office(Id)

    #if the office exists then return it as json response
    if office:
        return jsonify({
            "status" : 200,
            "data" : [office],
            "success" : "request was successful",
        })

    #return error response
    return jsonify({"status": 404, "error": "no office with that id was found"}), 404
