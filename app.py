"""Instantiate an instance of the app."""

from flask import Flask
from config import app_config
from api.admin.party.parties import PARTY_BLUEPRINT
from api.admin.office.offices import OFFICE_BLUEPRINT

def create_app(environment="development"):
    """create an instance of the flask app given the passed environment variable and return."""

    #instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    #set configuration
    app.config.from_object(app_config[environment])


    #url prefix for api version 1
    url_prefix_version_1 = "/api/v1"

    #register party blueprint
    app.register_blueprint(PARTY_BLUEPRINT, url_prefix=url_prefix_version_1)

    #register office blueprint
    app.register_blueprint(OFFICE_BLUEPRINT, url_prefix=url_prefix_version_1)

    return app



