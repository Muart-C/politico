from flask import Blueprint

party_blueprint = Blueprint('parties', __name__)

@party_blueprint.route('/parties', methods=['GET'])
def get_parties():
    pass