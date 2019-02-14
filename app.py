"""Instantiate an instance of the app."""

from flask import Flask
from config import app_config
from api.views.auth import AUTH_BLUEPRINT
from api.views.parties import PARTY_BLUEPRINT
from api.views.offices import OFFICE_BLUEPRINT
from api.utils.validator import return_error

 #handle 405 errors
def handle_405_error(err):
    return return_error(405, "method not allowed")

 #handle 404 errors
def handle_404_error(err):
    return return_error(404, "bad url format")

def create_app(environment="development"):
    """create an instance of the flask app given the passed environment variable and return."""

    #instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    #register 405 error handler
    app.register_error_handler(405, handle_405_error)
    #register 404 error handler
    app.register_error_handler(404, handle_404_error)
    #set configuration
    app.config.from_object(app_config[environment])


    #url prefix for api version 1
    url_prefix_version_2 = "/api/v2"

    # register auth blueprint
    app.register_blueprint(AUTH_BLUEPRINT, url_prefix=url_prefix_version_2)

    #register party blueprint
    app.register_blueprint(PARTY_BLUEPRINT, url_prefix=url_prefix_version_2)

    #register office blueprint
    app.register_blueprint(OFFICE_BLUEPRINT, url_prefix=url_prefix_version_2)

    return app



