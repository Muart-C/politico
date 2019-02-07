import json
from tests.test_base import BaseTest
from app import create_app
class TestParty(BaseTest):
    """test the endpoints for the Party and edge cases"""

    def test_add_party(self):
        """ensure a new party can be added to the political party list."""
        response = self.client.post(
            '/api/v1/parties',
            data = json.dumps(self.party_with_data),
            content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('ANC was added', data['success'])
        self.assertIsInstance(data['status'], int)
        self.assertIsInstance(response.status_code, int)

    def test_add_party_with_empty_fields(self):
        """ensure all fields are field in order to create a party"""
        response = self.client.post(
                '/api/v1/parties',
                data = json.dumps(self.party_with_empty_fields),
                content_type = "application/json",
        )
        data = json.loads(response.data)
        self.assertEqual(data["status"], 400)
        self.assertIn(data["error"], "Please fill in all the required fields")
        self.assertEqual(response.status_code, 400)

    def test_get_parties(self):
        """a list of political parties is returned."""
        response = self.client.get(
                '/api/v1/parties',
                data = json.dumps(self.parties),
                content_type = "application/json",
            )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['data'], list)

    def test_get_a_party(self):
        """tests if can get a party"""
        self.client.post(
            '/api/v1/parties',
            data = json.dumps(self.party_with_data),
            content_type = "application/json",
        )

        get_party = self.client.get(
            '/api/v1/parties/1',
            content_type = "application/json",
        )
        data = json.loads(get_party.data)
        self.assertEqual(data["status"], 200)
        self.assertEqual(data["data"][0]["Id"], 1)
        self.assertEqual(data["data"][0]["name"], self.party_with_data["name"])
        self.assertEqual(data["success"], "request was successful and a party was returned")

