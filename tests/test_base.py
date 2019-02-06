import unittest
import json

from app import create_app

class BaseTest(unittest.TestCase):
    """define setup and teardown methods."""
    def setUp(self):
        app = create_app()
        self.client = app.test_client()

        #a dictionary containing a party
        self.party = {
                "name" : "ANC",
                "hqAddress" : "Kakamega",
                "logoUrl" : "https://goo.gl/images/B9U4PK",
            }

        #a list of containing dictionaries containing parties
        self.parties = [
            {
                "name" : "ANC",
                "hqAddress" : "Kakamega",
                "logoUrl" : "https://goo.gl/images/B9U4PK",
            },
            {
                "name" : "Jubilee",
                "hqAddress" : "Muthaiga",
                "logoUrl" : "https://goo.gl/images/7hU72H",
            },
            {
                "name" : "Maendeleo Chapchap",
                "hqAddress" : "Machakos",
                "logoUrl" : "https://goo.gl/images/3RKgQ6",
            }
        ]

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




