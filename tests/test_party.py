import json
from tests.test_base import BaseTest

class TestPartyApi(BaseTest):
    """test the endpoints for the Party and edge cases"""

    def test_add_party(self):
        """ensure a new party can be added to the political party list."""
        with self.client:
            response = self.client.post(
                '/api/v1/parties',
                data = json.dumps(self.party),
                content_type = "application/json",
            )
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 201)
            self.assertIn('ANC was added', data['success'])

    def test_get_parties(self):
        """a list of political parties is returned."""
        with self.client:
            response = self.client.get(
                '/api/v1/parties',
                data = json.dumps(self.parties),
                content_type = "application/json",
            )
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(data['data'], list)