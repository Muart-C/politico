from flask import Blueprint, request
from api.models.votes_model import Vote
from api.models.candidates_model import Candidate
from api.utils.validator import check_json_new_votes_keys, sanitize_input
from api.utils.validator import return_response, validate_string_data_type, check_json_party_keys
from api.utils.validator import return_error, validate_int_data_type, sanitize_input
#initialize a party blueprint
VOTE_BLUEPRINT = Blueprint('votes', __name__)
# create candidate route
@VOTE_BLUEPRINT.route('/votes/<int:candidate_id>', methods=["POST"])
def create_vote(candidate_id):
    """cast a new vote."""
    key_errors=check_json_new_votes_keys(request)
    if key_errors:
        return return_error(400, "Invalid keys provided")
    try:
        data = request.get_json()
        # validate data from the request
        user_id=data['user_id']
        office_id=data['office_id']

        if(sanitize_input(user_id) == False):
            return return_error(400, "provide a valid user id")
        if(sanitize_input(office_id) == False):
            return return_error(400, "provide a valid office id")
    except KeyError as e:
        return return_error(400, "an error occurred {} is missing".format(e.args[0]))

    candidate = Candidate(office_id=None, party_id=None, candidate_id=None)
    result = candidate.get_candidate(candidate_id)
    if result is True:
        vote = Vote(office_id=office_id,user_id=user_id, candidate_id=candidate_id)
	#check if candidate is already registered
    if vote.check_if_a_user_has_voted_for_a_candidate() is True:
        return return_error(400, "user has already voted")
    new = vote.vote_for_a_candidate()
    if new:
        return return_response(201, "voting was successful")
    return return_error(400, "an error occurred while voting")
    return return_error(400, "no such candidate is registered")


