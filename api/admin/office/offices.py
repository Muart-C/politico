from flask import Blueprint

#initialize an office blueprint
office_blueprint = Blueprint('offices', __name__)


#create an office route
@office_blueprint.route('/offices', methods=['POST'])
def get_offices():
    pass

    