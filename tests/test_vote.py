import json
from tests.test_base import BaseTest
from api.utils.test_data import cast_vote, cast_vote_no_office,\
    cast_vote_no_user, office_with_correct_data, register_candidate,\
        party_with_data,cast_vote_wrong_candidate,\
            cast_vote_wrong_office

class TestVote(BaseTest):
    def test_add_Vote(self):
        self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
            headers=self.super_token
        )
        self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_data),
            content_type="application/json",
            headers=self.super_token
        )

        self.client.post(
            '/api/v2/offices/1/register',
            data = json.dumps(register_candidate),
            content_type = "application/json",
            headers=self.super_token
        )
        response = self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote),
            content_type = "application/json",
            headers=self.user_token
        )
        self.assertEqual(response.status_code, 201)

    def test_vote_with_no_office(self):
        response = self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote_no_office),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_vote_with_wrong_office(self):
        response = self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote_wrong_office),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_vote_with_wrong_candidate(self):
        response = self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote_wrong_candidate),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_vote_with_no_candidate(self):
        response = self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote_no_user),
            content_type = "application/json",
            headers=self.super_token
        )
        self.assertEqual(response.status_code, 400)

    def test_get_results(self):
        self.client.post(
            '/api/v2/offices',
            data = json.dumps(office_with_correct_data),
            content_type = "application/json",
            headers=self.super_token
        )
        self.client.post(
            "/api/v2/parties",
            data=json.dumps(party_with_data),
            content_type="application/json",
            headers=self.super_token
        )

        self.client.post(
            '/api/v2/offices/1/register',
            data = json.dumps(register_candidate),
            content_type = "application/json",
            headers=self.super_token
        )
        self.client.post(
            '/api/v2/votes',
            data = json.dumps(cast_vote),
            content_type = "application/json",
            headers=self.super_token
        )
        response=self.client.get(
            '/api/v2/offices/1/result',
            content_type = "application/json",
        )
        print(response)
        self.assertEqual(response.status_code, 200)
