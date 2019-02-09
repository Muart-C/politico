import json
from tests.test_base import BaseTest
from app import create_app
class TestParty(BaseTest):
    """test the endpoints for the Party and edge cases"""

    def test_add_party(self):
        """test creation of a party."""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(self.party_with_data),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))

        self.assertEqual(data["status"], 201)
        self.assertEqual(data["message"], "party ANC was created")

    def test_get_all_parties(self):
        """tests if parties are returned."""
        self.client.post(
            '/api/v1/parties',
            data=json.dumps(self.party_with_data)
        )

        response = self.client.get('/api/v1/parties')

        data = json.loads(response.data)

        self.assertEqual(data["status"], 200)
        self.assertEqual(len(data["data"]), 1)
        self.assertEqual(data["message"], "get request is for parties successful")

    def test_get_party(self):
        """tests to get a party"""

        self.client.post(
            '/api/v1/parties',
            data=json.dumps(self.party_with_data),
            content_type="application/json"
        )
        response = self.client.get(
            '/api/v1/parties/1',
            content_type = "application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 200)
        self.assertEqual(len(data["data"]), 1)
        self.assertEqual(data["message"], "a party with the id was returned")

    def test_updating_party_name(self):
        """test update party name."""

        self.client.post(
            '/api/v1/parties',
            data=json.dumps(self.party_with_data),
            content_type="application/json"
        )

        response = self.client.patch(
            '/api/v1/parties/1/name',
            data=json.dumps({
                "name":"party name"
            }),
        )
        print(response)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "party name was updated")
        self.assertEqual(data["status"], 200)
