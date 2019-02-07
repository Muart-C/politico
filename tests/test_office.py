import json
from tests.test_base import BaseTest
from app import create_app
class TestOffice(BaseTest):
    """test the endpoints for the office and edge cases"""

    def test_add_office(self):
        """ensure a new office can be added to the political office list."""
        response = self.client.post(
            '/api/v1/offices',
            data = json.dumps(self.office_with_data),
            content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(data['status'], int)
        self.assertIsInstance(response.status_code, int)

    def test_add_office_with_empty_fields(self):
        """ensure all fields are field in order to create a office"""
        response = self.client.post(
                '/api/v1/offices',
                data = json.dumps(self.office_with_empty_fields),
                content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertIn(data["error"], "Please fill in all the required fields")
        self.assertEqual(response.status_code, 400)

    def test_get_offices(self):
        """a list of political offices is returned."""
        response = self.client.get(
                '/api/v1/offices',
                data = json.dumps(self.offices),
                content_type = "application/json",
            )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['data'], list)

    def test_get_an_office(self):
        """tests if can get a office"""
        self.client.post(
            '/api/v1/offices',
            data = json.dumps(self.office_with_data),
            content_type = "application/json",
        )

        get_office = self.client.get(
            '/api/v1/offices/{}'.format(1),
            content_type = "application/json",
        )
        data = json.loads(get_office.data)
        self.assertEqual(data["status"], 200)
        #self.assertEqual(data["data"][0]["Id"], 1)
        #self.assertEqual(data["data"][0]["name"], self.office_with_data["name"])
        self.assertEqual(data["success"], "request was successful")


