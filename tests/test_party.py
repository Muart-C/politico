import json
from tests.test_base import BaseTest

class TestPartyApi(BaseTest):
    """test the endpoints for the Party and edge cases"""

    def test_add_party(self):
        """ensure a new party can be added to the political party list."""
        with self.client:
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
        with self.client:
            response = self.client.post(
                '/api/v1/parties',
                data = json.dumps(self.party_with_empty_fields),
                content_type = "application/json",
            )
            data = json.loads(response.data)
            self.assertEqual(data["status"], 400)
            self.assertIn(data["error"], "Please fill in all the required fields")
            self.assertEqual(response.status_code, 400)

    def test_add_party_with_empty_name(self):
        """ensure add a party cannot be  processed with a blank name on the input"""
        with self.client:
            response = self.client.post(
                '/api/v1/parties',
                data = json.dumps(self.party_with_name_missing),
                content_type = "application/json",
            )
            data = json.loads(response.data)
            self.assertEqual(data["status"], 400)
            self.assertIn(data["error"], "Please add your name")
            self.assertEqual(response.status_code, 400)

    def test_add_party_with_empty_logo(self):
        """ensure add a party cannot be  processed with a blank logo on the input"""
        with self.client:
            response = self.client.post(
                '/api/v1/parties',
                data = json.dumps(self.party_with_logo_missing),
                content_type = "application/json",
            )
            data = json.loads(response.data)
            self.assertEqual(data["status"], 400)
            self.assertIn(data["error"], "Please add your logo")
            self.assertEqual(response.status_code, 400)

    def test_add_party_with_hq_missing(self):
        """ensure add a party cannot be  processed with a blank headquarter on the input"""
        with self.client:
            response = self.client.post(
                '/api/v1/parties',
                data = json.dumps(self.party_with_hq_missing),
                content_type = "application/json",
            )
            data = json.loads(response.data)
            self.assertEqual(data["status"], 400)
            self.assertIn(data["error"], "Please the parties headquarter")
            self.assertEqual(response.status_code, 400)

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