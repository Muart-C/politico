"""users unit tests definition"""
import json
from tests.test_base import BaseTest
from api.utils.test_data import new_user,\
     create_user_missing_data,create_user_wrong_email_input,\
         create_user_wrong_firstname_input, create_user_wrong_lastname_input
from api.utils.test_data import create_user_wrong_phone_number_input,\
     create_user_wrong_passport_url_input, user_login,\
         user_login_blank_password, user_login_empty_email,\
              user_login_password_less_than_six_characters,\
                   user_login_wrong_email, user_login_wrong_email_format,\
                       user_login_wrong_password,new_user_2

from api.models.users_model import User


class Users(BaseTest):

    def test_user_sign_up(self):
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(new_user_2),
            content_type="application/json",
            headers=self.user_token
        )
        # get data from the request into json
        data = json.loads(response.data.decode("utf-8"))
        print(data)
        self.assertEqual(data['status'], 201)

    def test_user_sign_up_missing_data(self):
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_missing_data),
            content_type="application/json"
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_email_input(self):
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_email_input),
            content_type="application/json"
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_firstname_input(self):
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_firstname_input),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_lastname_input(self):
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_lastname_input),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_phone_number_input(self):
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_phone_number_input),
            content_type="application/json"
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_sign_up_with_wrong_passport_url_input(self):
        response=self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(create_user_wrong_passport_url_input),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_login_blank_password(self):
        response=self.client.post(
            "/api/v2/auth/login",
            data=json.dumps(user_login_blank_password),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
    
    def test_user_login_empty_email(self):
        response=self.client.post(
            "/api/v2/auth/login",
            data=json.dumps(user_login_empty_email),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_login_wrong_email(self):
        response=self.client.post(
            "/api/v2/auth/login",
            data=json.dumps(user_login_wrong_email),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)

    def test_user_login_wrong_email_format(self):
        response=self.client.post(
            "/api/v2/auth/login",
            data=json.dumps(user_login_wrong_email_format),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 400)


