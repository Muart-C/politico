import os
import unittest
import json
from app import create_app
from config import app_config
from api.models.parties_model import Party
from api.models.offices_model import Office
from api.database.database import DatabaseSetup
from api.utils.test_data import new_user,\
     admin_login, user_login, party_with_data

class BaseTest(unittest.TestCase):
    """define setup and teardown methods."""
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app.config['JWT_SECRET_KEY'] = 'thisismysecret23'
        with self.app.app_context():
            DatabaseSetup().drop_tables_if_exists()
            DatabaseSetup().create_all_tables()
            DatabaseSetup().create_admin_if_does_not_exist()


        response=self.client.post(
            "/api/v2/auth/login",
            data=json.dumps(admin_login),
            content_type="application/json",
        )
        auth_token = json.loads(response.data.decode())
        self.super_token = {"Authorization": "Bearer {}".format(auth_token['token'])}

        self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(new_user),
		    content_type='application/json'
        )

        response=self.client.post(
            "/api/v2/auth/login",
            data=json.dumps(user_login),
            content_type="application/json",
        )
        auth_token = json.loads(response.data.decode())
        self.user_token = {'Authorization': 'Bearer {}'.format(auth_token['token'])}


