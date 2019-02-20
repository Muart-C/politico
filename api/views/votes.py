import json
from flask import Blueprint, request, make_response, jsonify
from api.models.votes_model import Vote
from api.models.candidates_model import Candidate
from api.models.offices_model import Office
from api.models.users_model import User
from api.utils.validator import check_json_new_votes_keys, sanitize_input
from api.utils.validator import return_response, validate_string_data_type, check_json_party_keys
from api.utils.validator import return_error, validate_int_data_type, sanitize_input

VOTE_BLUEPRINT = Blueprint('votes', __name__)

@VOTE_BLUEPRINT.route('/votes', methods=["POST"])
def create_vote():
    """cast a new vote."""
    key_errors=check_json_new_votes_keys(request)
    if key_errors:
        return return_error(400, "please provide valid json keys")
    try:
        data = request.get_json()
        candidate_id=data['candidate_id']
        user_id=data['user_id']
        office_id=data['office_id']

        if(validate_int_data_type(candidate_id) == False):
            return return_error(400, "Please provide a valid candidate id")
        if(validate_int_data_type(user_id) == False):
            return return_error(400, "Provide a valid user id")
        if(validate_int_data_type(office_id) == False):
            return return_error(400, "Provide a valid office id")
    except KeyError as e:
        return return_error(400, "An error occurred {} is missing".format(e.args[0]))

    user = User()
    result = user.get_user_by_id(user_id)
    user = json.loads(result)

    if not user:
        return return_error(404, "Ensure the voter is registered")

    office = Office(name=None, office_type=None)
    result = office.get_office(office_id)
    office = json.loads(result)

    if not office:
        return return_error(404, "Ensure that the office exists")

    candidate = Candidate(office_id=None, party_id=None, candidate_id=None)
    result = candidate.get_candidate(candidate_id)
    candidate = json.dumps(result)

    if not candidate:
        return return_error(404, "The candidate was not found.")

    vote = Vote(office_id=None,user_id=None, candidate_id=None)
    result =  vote.check_if_has_voted(user_id, office_id)
    vote = json.dumps(result)

    if vote:
        return return_error(409, "You have already voted.")

    vote = Vote(office_id=office_id,user_id=user_id, candidate_id=candidate_id)
    new = vote.vote_for_a_candidate()
    if new:
        return make_response(jsonify({
            "status":201,
            "data": [{
                "office" : office_id,
                "candidate":candidate_id,
                "voter": user_id
            }]
        }),201)
    return return_error(400, "Ensure that you fill all the fields")
