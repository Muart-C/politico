import unittest
import json
from api.app import create_app


class BaseTest(unittest.TestCase):
    """define setup and teardown methods."""
    def setUp(self):
        app = create_app(environment='testing')
        self.client = app.test_client()
        self.party = {
            "Id" : "1",
            "name" : "ANC",
            "hqAddress" : "Kakamega",
            "logoUrl" : "https://goo.gl/images/B9U4PK",
        }

    def test_add_party(self):
        """ensure a new party can be added to the political party list."""
        with self.client:
            response = self.client.post(
                '/parties',
                data = json.dumps(self.party),
                content_type = "application/json"
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('ANC was added', data['success'])
            self.assertIn(201, data['status'])


if __name__ == "__main__":
    unittest.main()
