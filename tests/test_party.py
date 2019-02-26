import json
from tests.test_base import BaseTest
from app import create_app
from api.utils.test_data import party_with_data, party_with_empty_fields,\
     party_with_wrong_name_type, party_with_wrong_address_input,\
          party_with_wrong_logo_url, party_with_invalid_key_name,\
               party_with_invalid_key_address, party_with_wrong_name_input,\
                    party_with_wrong_address_type, update_party_name,\
                        update_blank_party_name,update_party_name_not_string,\
                            update_party_name_without_request_object
class TestParty(BaseTest):
    def test_add_party(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_data),
            content_type="application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 201)

    def test_add_party_when_not_authorized(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_data),
            content_type="application/json",
            headers=self.user_token
        )
        self.assertEqual(response.status_code, 401)

    def test_add_party_twice(self):
        self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_data),
            content_type="application/json",
            headers=self.super_token
        )
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_data),
            content_type="application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 409)

    def test_add_party_with_missing_input(self):
        response = self.client.post(
            '/api/v2/parties',
            data = json.dumps(party_with_empty_fields),
            content_type = "application/json",
            headers=self.super_token
        )
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)

    def test_get_all_parties(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
        )
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
        )

        response = self.client.get('/api/v2/parties')
        self.assertEqual(response.status_code, 200)

    def test_get_a_party(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
            headers=self.super_token
        )

        response = self.client.get('/api/v2/parties/1')
        self.assertEqual(response.status_code, 200)

    def test_get_a_party_that_does_not_exist(self):
        response = self.client.get('/api/v2/parties/12')
        self.assertEqual(response.status_code, 404)

    def test_update_party_name(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
            headers=self.super_token
        )

        response= self.client.patch(
            '/api/v2/parties/1/name',
            data=json.dumps(update_party_name),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 200)

    def test_update_party_name_when_not_authorized(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
            headers=self.super_token
        )

        response= self.client.patch(
            '/api/v2/parties/1/name',
            data=json.dumps(update_party_name),
            content_type = "application/json",
        )
        self.assertEqual(response.status_code, 401)

    def test_update_party_with_blank_name(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
            headers=self.super_token
        )

        response= self.client.patch(
            '/api/v2/parties/1/name',
            data=json.dumps(update_blank_party_name),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_update_party_name_without_request_object(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
            headers=self.super_token
        )

        response= self.client.patch(
            '/api/v2/parties/1/name',
            data=json.dumps(update_party_name_without_request_object),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_update_party_with_not_a_string(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
            headers=self.super_token
        )

        response= self.client.patch(
            '/api/v2/parties/1/name',
            data=json.dumps(update_party_name_not_string),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_add_party_with_name_of_wrong_data_type(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_name_type),
            content_type="application/json",
            headers=self.super_token
        )

        self.assertEqual(response.status_code, 400)

    def test_add_party_with_wrong_name_input(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_name_input),
            content_type="application/json",
            headers=self.super_token
        )

        self.assertEqual(response.status_code, 400)

    def test_add_party_with_wrong_address_input(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_address_input),
            content_type="application/json",
            headers=self.super_token
        )

        self.assertEqual(response.status_code, 400)

    def test_add_party_with_wrong_address_type(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_address_type),
            content_type="application/json",
            headers=self.super_token
        )

        self.assertEqual(response.status_code, 400)

    def test_add_party_with_the_wrong_url_format(self):
        response = self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_wrong_logo_url),
            content_type="application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_party_that_does_not_exist(self):
        response = self.client.delete(
            '/api/v2/parties/123',
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_party(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
            headers=self.super_token
        )
        response = self.client.delete(
            '/api/v2/parties/1',
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_party_when_not_authorized(self):
        self.client.post(
            '/api/v2/parties',
            data=json.dumps(party_with_data),
            content_type = "application/json",
            headers=self.super_token
        )
        response = self.client.delete(
            '/api/v2/parties/1',
            headers=self.user_token
        )
        self.assertEqual(response.status_code, 401)