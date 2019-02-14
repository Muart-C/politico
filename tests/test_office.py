import json
from tests.test_base import BaseTest
from app import create_app
from api.utils.test_data import office_with_correct_data, office_with_wrong_office_type_data
from api.utils.test_data import office_with_wrong_office_name_data, office_with_invalid_key_name
from api.utils.test_data import office_with_invalid_key_office_type, office_with_wrong_office_type_type_input
class TestOffice(BaseTest):
    """test the endpoints for the office and edge cases"""

    def test_add_office(self):
        """ensure a new office can be added to the political office list."""
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(data["status"], 201)

    def test_add_office_with_wrong_type(self):
        """ensure a correct office type is chosen."""
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_wrong_office_type_data),
            content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)

    def test_add_office_with_wrong_office_name_data(self):
        """ensure correct name is used."""
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_wrong_office_name_data),
            content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)

    def test_add_office_with_invalid_key_name(self):
        """ensure correct keys for the name."""
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_invalid_key_name),
            content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)

    def test_add_office_with_invalid_key_office_type(self):
        """ensure correct keys for the name."""
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_invalid_key_office_type),
            content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)

    def test_add_office_with_wrong_office_type_type_input(self):
        """ensure correct keys for the name."""
        response = self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_wrong_office_type_type_input),
            content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)


    def test_get_offices(self):
        """a list of political offices is returned."""
        self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
        )
        response = self.client.get(
                '/api/v2/offices',
                content_type = "application/json",
            )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['data'], list)

    def test_get_an_office(self):
        """tests if can get a office"""
        self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
        )

        get_office = self.client.get(
            '/api/v2/offices/1',
            content_type = "application/json",
        )
        data = json.loads(get_office.data.decode("utf-8"))
        print(data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(data["message"], "request was successful")

