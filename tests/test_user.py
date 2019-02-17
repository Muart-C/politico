"""users unit tests definition"""
import json
from tests.test_base import BaseTest
from api.utils.test_data import new_user,\
     create_user_missing_data,create_user_wrong_email_input,\
         create_user_wrong_firstname_input, create_user_wrong_lastname_input
from api.utils.test_data import create_user_wrong_phone_number_input, create_user_wrong_passport_url_input
from api.models.users_model import User

class Users(BaseTest):
    """implement unit test functions here."""
    def test_user_sign_up(self):
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(new_user),
            content_type="application/json",
        )
        # get data from the request into json
        data = json.loads(response.data.decode("utf-8"))
        print(data)
        self.assertEqual(data['status'], 201)

    def test_user_sign_up_missing_data(self):
        """"ensures data is provided before registration."""
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_missing_data),
            content_type="application/json"
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_email_input(self):
        """ensure user can only sign up with valid email address"""
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_email_input),
            content_type="application/json"
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_firstname_input(self):
        """ensure user can only sign up with valid firstname"""
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_firstname_input),
            content_type="application/json"
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_lastname_input(self):
        """ensure user can only sign up with valid lastname"""
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_lastname_input),
            content_type="application/json"
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_phone_number_input(self):
        """ensure user can only sign up with valid phone_number"""
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_phone_number_input),
            content_type="application/json"
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_passport_url_input(self):
        """ensure user can only sign up with valid passport url input"""
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_passport_url_input),
            content_type="application/json"
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
