import os
from flask import Flask, redirect, url_for
from flask_jwt_extended import JWTManager
from config import app_config
from api.views.auth import AUTH_BLUEPRINT
from api.views.parties import PARTY_BLUEPRINT
from api.views.offices import OFFICE_BLUEPRINT
from api.views.votes import VOTE_BLUEPRINT
from api.database.database import DatabaseSetup
from api.utils.validator import return_error

def handle_405_error(err):
    return return_error(405, "the action you are undertaking is not allowed")

def handle_404_error(err):
    return return_error(404, "unrecognized resource request")

def handle_500_error(err):
    return return_error(500, "a server error occurred please wait we figure out what went wrong")

def create_app(configuration):
    app = Flask(__name__, instance_relative_config=True)

    JWTManager(app)

    app.register_error_handler(405, handle_405_error)
    app.register_error_handler(404, handle_404_error)
    app.register_error_handler(500, handle_500_error)
    app.config.from_object(app_config[configuration])

    url_prefix_version_2 = "/api/v2"
    DatabaseSetup().create_all_tables()
    DatabaseSetup().create_admin_if_does_not_exist()
    
    @app.route('/')
    def docs():
        return redirect(url_for('flasgger.apidocs'))


    app.register_blueprint(AUTH_BLUEPRINT, url_prefix=url_prefix_version_2)
    app.register_blueprint(PARTY_BLUEPRINT, url_prefix=url_prefix_version_2)
    app.register_blueprint(OFFICE_BLUEPRINT, url_prefix=url_prefix_version_2)
    app.register_blueprint(VOTE_BLUEPRINT, url_prefix=url_prefix_version_2)

    return app



