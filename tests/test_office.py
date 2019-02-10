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
        self.assertEqual(data["status"], 201)
        self.assertEqual(data["message"], "office of Presidency was created")


    # def test_add_office_with_empty_fields(self):
    #     """ensure all fields are field in order to create a office"""
    #     response = self.client.post(
    #         '/api/v1/offices',
    #         data = json.dumps(self.office_with_empty_fields),
    #         content_type = "application/json",
    #     )
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data["message"], "an error occurred while adding the office")

    def test_get_offices(self):
        """a list of political offices is returned."""
        self.client.post(
            '/api/v1/offices',
            data = json.dumps(self.office_with_data),
            content_type = "application/json",
        )
        response = self.client.get(
                '/api/v1/offices',
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
            '/api/v1/offices/1',
            content_type = "application/json",
        )
        data = json.loads(get_office.data.decode("utf-8"))
        print(data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(data["message"], "request was successful")


