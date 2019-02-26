import json
from tests.test_base import BaseTest
from app import create_app
from api.utils.test_data import office_with_correct_data, office_with_wrong_office_type_data
from api.utils.test_data import office_with_wrong_office_name_data, office_with_invalid_key_name
from api.utils.test_data import office_with_invalid_key_office_type,\
     office_with_wrong_office_type_type_input, office_with_empty_name,\
         office_with_empty_office_type,office_with_wrong_office_type
class TestOffice(BaseTest):

    def test_add_office(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 201)

    def test_add_office_while_unauthorized(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
            headers=self.user_token
        )
        self.assertEqual(response.status_code, 401)

    def test_add_office_twice(self):
        self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
            headers=self.super_token
        )
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 409)

    def test_add_office_with_wrong_type(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_wrong_office_type_data),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_add_office_with_wrong_office_name_data(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_wrong_office_name_data),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_add_office_with_invalid_key_name(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_invalid_key_name),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_add_office_with_invalid_key_office_type(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_invalid_key_office_type),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_add_office_with_wrong_office_type_type_input(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_wrong_office_type_type_input),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_add_office_with_empty_name(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_empty_name),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_add_office_with_empty_office_type(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_empty_office_type),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)


    def test_add_office_with_wrong_office_type(self):
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_wrong_office_type),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_get_offices(self):
        """a list of political offices is returned."""
        self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
            headers=self.super_token
        )
        response = self.client.get(
            '/api/v2/offices',
            content_type = "application/json",
        )

        self.assertEqual(response.status_code, 200)

    def test_get_office_that_does_not_exist(self):
        response = self.client.get(
            '/api/v2/offices/123',
        )
        self.assertEqual(response.status_code, 404)