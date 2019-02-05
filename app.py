"""Instantiate an instance of the app."""

from flask import Flask
#from config import app_config
from api.admin.party.parties import party_blueprint
from api.admin.office.offices import office_blueprint

def create_app():
    """create an instance of the flask app given the passed environment variable and return."""
    
    #instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    #set configuration
    #app.config.from_object(app_configuration[environment])
    #app.config.from_pyfile('config.py')

    
    #url prefix for api version 1
    url_prefix_version_1 = "/api/v1"

    #register party blueprint
    app.register_blueprint(party_blueprint, url_prefix=url_prefix_version_1)

    #register office blueprint
    app.register_blueprint(office_blueprint, url_prefix=url_prefix_version_1)

    return app
    


