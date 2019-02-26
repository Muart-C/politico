import json
from tests.test_base import BaseTest
from api.utils.test_data import register_candidate,\
     register_candidate_no_party, register_candidate_no_user
class TestCandidate(BaseTest):
    def test_add_candidate_no_office(self):
        response = self.client.post(
            '/api/v2/offices/1/register',
            data = json.dumps(register_candidate),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 404)
    def test_get_results_for_office_does_not_exist(self):
        response=self.client.get(
            '/api/v2/offices/1/result',
            content_type = "application/json",
        )
        self.assertEqual(response.status_code, 404)