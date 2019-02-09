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

    def test_add_party_with_missing_input(self):
        """test user cannot create party with missing fields"""
        response = self.client.post(
            '/api/v1/parties',
            data = json.dumps(self.empty_parties_list),
            content_type = "application/json",
        )
    def test_get_all_parties(self):
        """tests if parties are returned."""
        self.client.post(
            '/api/v1/parties',
            data=json.dumps(self.party_with_data),
            content_type = "application/json",
        )

        response = self.client.get('/api/v1/parties')

        data = json.loads(response.data)

        self.assertEqual(data["status"], 200)
        self.assertEqual(len(data["data"]), 2)
        self.assertEqual(data["message"], "get request is for parties successful")

    def test_get_party(self):
        """tests to get a party"""

        self.client.post(
            '/api/v1/parties',
            data=json.dumps(self.party_with_data),
            content_type="application/json",
        )
        response = self.client.get(
            '/api/v1/parties/1',
            content_type = "application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 200)
        self.assertEqual(len(data["data"]), 2)
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
            content_type = "application/json",
        )
        print(response)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "party name was updated")
        self.assertEqual(data["status"], 200)

    def test_delete_party(self):
        """ensure a party is deleted."""
        self.client.post(
            '/api/v1/parties',
            data=json.dumps(self.party_with_data),
            content_type="application/json",
        )

        result_delete=self.client.delete(
            '/api/v1/parties/{}'.format(0),
            content_type="application/json",
        )
        result_delete=json.loads(result_delete.data.decode())
        self.assertEqual(result_delete["message"], "party was deleted")



