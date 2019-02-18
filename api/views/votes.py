from flask import Blueprint, request, make_response, jsonify
from api.models.votes_model import Vote
from api.models.candidates_model import Candidate
from api.utils.validator import check_json_new_votes_keys, sanitize_input
from api.utils.validator import return_response, validate_string_data_type, check_json_party_keys
from api.utils.validator import return_error, validate_int_data_type, sanitize_input
#initialize a party blueprint
VOTE_BLUEPRINT = Blueprint('votes', __name__)
# create candidate route
@VOTE_BLUEPRINT.route('/votes', methods=["POST"])
def create_vote():
    """cast a new vote."""
    key_errors=check_json_new_votes_keys(request)
    if key_errors:
        return return_error(400, "please provide valid json keys")
    try:
        data = request.get_json()
        # validate data from the request
        candidate_id=data['candidate_id']
        user_id=data['user_id']
        office_id=data['office_id']

        if(validate_int_data_type(user_id) == False):
            return return_error(400, "provide a valid user id")
        if(validate_int_data_type(office_id) == False):
            return return_error(400, "provide a valid office id")
    except KeyError as e:
        return return_error(400, "an error occurred {} is missing".format(e.args[0]))

    candidate = Candidate(office_id=None, party_id=None, candidate_id=None)
    result = candidate.get_candidate(candidate_id)
    if result is True:
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
        }))
        return return_error(400, "failed")


