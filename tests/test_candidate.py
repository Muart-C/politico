import json
from tests.test_base import BaseTest

register_candidate={
	"party_id":1,
	"candidate_id": 1
}

register_candidate_no_party={
	"candidate_id": 1
}

register_candidate_no_user={
	"party_id": 1
}

class TestCandidate(BaseTest):
    def test_add_candidate_no_office(self):
        response = self.client.post(
            '/api/v2/offices/1/register',
            data = json.dumps(register_candidate),
            content_type = "application/json",
            headers=self.super_token
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
    def test_get_results_for_office_does_not_exist(self):
        response=self.client.get(
            '/api/v2/offices/1/result',
            content_type = "application/json",
        )
        self.assertEqual(response.status_code, 404)