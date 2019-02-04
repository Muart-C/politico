"""Instantiate an instance of the app."""

from flask import Flask
from config import app_configuration
from api.admin.party.parties import party_blueprint


def create_app(environment="testing"):
    """create an instance of the flask app given the passed environment variable and return."""
    
    #instantiate the app
    app = Flask(__name__)

    #set configuration
    app.config.from_object(app_configuration[environment])

    #url prefix for api version
    url_prefix = "api/v1/"




