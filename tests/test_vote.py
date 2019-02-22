import json
from tests.test_base import BaseTest

cast_vote={
	"office_id":1,
	"candidate_id":1
}



cast_vote_no_office={
	"candidate_id": 1
}

cast_vote_no_user={
	"office_id": 1
}

class TestVote(BaseTest):
    def test_add_Vote(self):
        response = self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote),
            content_type = "application/json",
            headers=self.super_token
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
    
    def test_vote_with_no_office(self):
        response = self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote_no_office),
            content_type = "application/json",
            headers=self.super_token
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)

    def test_vote_with_no_candidate(self):
        response = self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote_no_user),
            content_type = "application/json",
            headers=self.super_token
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
