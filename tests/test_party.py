import json
from tests.test_base import BaseTest
from app import create_app
from api.utils.test_data import party_with_data, party_with_empty_fields, party_with_wrong_name_type
from api.utils.test_data import party_with_wrong_address_input, party_with_wrong_logo_url
from api.utils.test_data import party_with_invalid_key_name, party_with_invalid_key_address, party_with_wrong_name_input, party_with_wrong_address_type
class TestParty(BaseTest):
    """test the endpoints for the Party and edge cases"""

    def test_add_party(self):
        """test creation of a party."""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(party_with_data),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))

        self.assertEqual(data["status"], 201)
        self.assertEqual(data["message"], "party ANC was created")

    def test_add_party_with_missing_input(self):
        """test user cannot create party with missing fields"""
        response = self.client.post(
            '/api/v1/parties',
            data = json.dumps(party_with_empty_fields),
            content_type = "application/json",
        )
        data = json.loads(response.data.decode())

        self.assertEqual(data["status"], 400)

    def test_get_all_parties(self):
        """tests if parties are returned."""
        self.client.post(
            '/api/v1/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
        )
        self.client.post(
            '/api/v1/parties',
            data=json.dumps(party_with_data),
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
            data=json.dumps(party_with_data),
            content_type="application/json",
        )
        self.client.post(
            '/api/v1/parties',
            data=json.dumps(party_with_data),
            content_type="application/json",
        )
        response = self.client.get(
            '/api/v1/parties/1',
            content_type = "application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["message"], "a party with the id was returned")
        self.assertEqual(data["status"], 200)
        self.assertEqual(len(data["data"]), 1)

    def test_updating_party_name(self):
        """test update party name."""

        self.client.post(
            '/api/v1/parties',
            data=json.dumps(party_with_data),
            content_type="application/json"
        )

        response = self.client.patch(
            '/api/v1/parties/{}/name'.format(1),
            data=json.dumps({
                "name":"party name"
            }),
            content_type = "application/json",
        )
        data = json.loads(response.data.decode())
        self.assertEqual(data["message"], "party name was updated")
        self.assertEqual(data["status"], 200)

    # def test_updating_party_name_of_party_that_does_not_exist(self):
    #     """test update name of a party that does not exist."""

    #     response = self.client.patch(
    #         '/api/v1/parties/{}/name'.format(100),
    #         data=json.dumps(party_with_data),
    #     )
    #     data = json.loads(response.data.decode())
    #     self.assertEqual(data["status"], 400)

    def test_delete_party(self):
        """ensure a party is deleted."""
        self.client.post(
            '/api/v1/parties',
            data=json.dumps(party_with_data),
            content_type="application/json",
        )

        result_delete=self.client.delete(
            '/api/v1/parties/1',
            content_type="application/json",
        )
        self.assertEqual(result_delete.status_code, 204)

    def test_getting_non_existing_party(self):
        """ensure an error is returned for non existing party"""
        result=self.client.get(
            '/api/v1/parties/24'
        )
        data=json.loads(result.data.decode("utf-8"))
        self.assertEqual(data["status"], 404)

    def test_party_with_name_of_wrong_data_type(self):
        """ensure to only add name of correct data type"""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(party_with_wrong_name_type),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 400)

    def test_party_party_with_wrong_name_input(self):
        """ensure to only add name of correct data type"""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(party_with_wrong_name_input),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 400)

    def test_party_with_wrong_address_input(self):
        """ensure to only add address that is correct"""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(party_with_wrong_address_input),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 400)

    def test_party_with_wrong_address_type(self):
        """ensure to only add address that is correct"""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(party_with_wrong_address_type),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 400)

    def test_party_with_the_wrong_url_format(self):
        """ensure to only add url of correct format."""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(party_with_wrong_logo_url),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 400)

    def test_party_with_invalid_key_name(self):
        """ensure key of name attribute is correct."""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(party_with_invalid_key_name),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 400)

    def test_party_with_invalid_key_address(self):
        """ensure key of name attribute is correct."""
        response = self.client.post(
            "/api/v1/parties",
            data=json.dumps(party_with_invalid_key_address),
            content_type="application/json",
        )

        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(data["status"], 400)
