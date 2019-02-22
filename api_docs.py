from app import create_app
from flasgger import Swagger
from flask_cors import CORS


app = create_app('production')
app.config['SWAGGER'] = {
    "swagger": "2.0",
    "API version": "Version 2",
    "info": {
        "title": "Politico API",
        "description": """
        Politico enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency.
        """,
        "version": "2.0",
        "license": {
            "name": "MIT license",
            "url": "https://opensource.org/licenses/MIT"
        }
    },
    'securityDefinitions': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
swagger = Swagger(app)
CORS(app)

@app.route('/api/v2/auth/signup', methods=['POST'])
def signup():
    """ User signup route.
    ---
    tags:
        - User
    parameters:
      - in: body
        name: User
        required: true
        schema:
          type: object
          properties:
            firstname:
              type: string
              example: "Muathe"
            lastname:
              type: string
              example: "Ndirangu"
            othername:
              type: string
              example: "charles"
            email:
              type: string
              example: "muathe.ndirangu@gmail.com"
            phone_number:
              type: string
              example: "+254711245793"
            passport_url:
              type: string
              example: "https://image.png"
            password:
              type: string
              example: "mysecretpassword213"
    responses:
      '201':
        description: User Created
      '409':
        description: User Already Exists
      '400':
        description: Ensure the data is in correct format
    """
@app.route('/api/v2/auth/login', methods=['POST'])
def login():
    """ User login route.
    ---
    tags:
        - User
    parameters:
      - in: body
        name: User
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: "muathe.ndirangu@gmail.com"
            password:
              type: string
              example: "mysecretpassword213"
    responses:
      '200':
        description: Login was successful
      '400':
        description: BAD REQUEST
    """
@app.route('/api/v2/offices', methods=['POST'])
def create_office():
    """ Create an office route.
    ---
    tags:
        - Offices
    parameters:
      -
          name: authorization
          in: header
          type: string
          required: true
          example: Bearer
      - in: body
        name: Offices
        required: true
        schema:
          type: object
          properties:
            office_name:
              type: string
              description: "One name"
              example: "For example Senate"
            office_type:
              type: string
	      description: "Limited to federal, local, state and legislative"
              example: "legislative"
    responses:
      '200':
        description: Office Successfully registered
      '400':
        description: Ensure enter the details correctly
      '401':
        description: You are not allowed to perfom this action
      '409':
        description: The office already exists
    """
@app.route('/api/v2/offices', methods=['GET'])
def get_offices():
    """ Fetch all offices route.
    ---
    tags:
        - Offices
    responses:
      '200':
        description: Some offices were found
    """

@app.route('/api/v2/offices/<int:office_id>', methods=['GET'])
def get_office(office_id):
    """ Get a specific office route.
    ---
    tags:
        - Offices
    parameters:
      - in: path
        name: office_id
        required: true
        type: integer
    responses:
      '200':
        description: Office was found
      '404':
        description: The office does not exist
    """

@app.route('/api/v2/parties', methods=['POST'])
def add_party():
    """ Add a new Party.
    ---
    tags:
        - Parties
    parameters:
      -
          name: authorization
          in: header
          type: string
          required: true
          example: Bearer
      - in: body
        name: Parties
        required: true
        schema:
          type: object
          properties:
            party_name:
              type: string
              example: "Jubilee"
            hq_address:
              type: string
              example: "Muathaiga"
            logo_url:
              type: string
              example: "https://jubilee.png"
    responses:
      '201':
        description: Party was created successfully
      '409':
        description: Party Already exists
      '400':
        description: Ensure your input is correct
      '401':
        description: You are not authorized to perform this action
    """


@app.route('/api/v2/parties', methods=['GET'])
def get_parties():
    """ get a list of parties route.
    ---
    tags:
        - Parties
    responses:
      '200':
        description: Request was successful 
    """


@app.route('/api/v2/parties/<int:party_id>', methods=['GET'])
def get_party(party_id):
    """ get a specific party.
    ---
    tags:
        - Parties
    parameters:
      - in: path
        name: party_id
        required: true
        type: integer
    responses:
      '200':
        description: Party was found
      '404':
        description: Party was not found
    """


@app.route('/api/v2/parties/<int:party_id>', methods=['DELETE'])
def delete_party(office_id):
    """ Delete a party.
    ---
    tags:
        - Parties
    parameters:
      -
          name: authorization
          in: header
          type: string
          required: true
          example: Bearer
      - in: path
        name: party_id
        required: true
        type: integer
    responses:
      '200':
        description: Party was deleted successfuly
      '404':
        description: Party was not found
      '401':
        description: You are unauthorized to perform that action
    """


@app.route('/api/v2/parties/<int:party_id>/name', methods=['PUT'])
def patch_name_of_party(party_id):
    """ Patch the name of the party.
    ---
    tags:
        - Parties
    parameters:
      -
          name: authorization
          in: header
          type: string
          required: true
          example: Bearer
      - in: path
        name: party_id
        required: true
        type: integer
      - in: body
        name: Name
        required: true
        schema:
          type: object
          properties:
            party_name:
              type: string
              example: Nasa
    responses:
      '200':
        description: Party name updated successfuly
      '404':
        description: No party with the id was found
      '401':
        description: You are not allowed to perfom this action
    """

@app.route('/api/v2/api/v2/offices/<int:office_id>/register', methods=['POST'])
def add_candidate():
    """ Add a candidate.
    ---
    tags:
        - Candidates
    parameters:
      - in: body
        name: Candidate
        required: true
        schema:
          type: object
          properties:
            candidate_id:
              type: int
              example: 1
            party_id:
              type: int
              example: 1
    responses:
      '201':
        description: Candidate was added successfuly
      '409':
        description: Candidate Already exists
      '400':
        description: Ensure you add all the required inputs
      '404':
        description: Either the party or the user with that id was not found
    """

@app.route('/api/v2/api/v2/votes', methods=['POST'])
def cast_vote():
    """ vote for a candidate.
    ---
    tags:
        - Votes
    parameters:
      - in: body
        name: Vote
        required: true
        schema:
          type: object
          properties:
            candidate_id:
              type: int
              example: 1
            office_id:
              type: int
              example: 1
    responses:
      '201':
        description: You have voted successfully
      '409':
        description: You have already cast your vote.
      '400':
        description: Ensure you add all the required inputs
      '404':
        description: Either the office or the user with that id was not found
    """
@app.route('/api/v2/office/<int:office_id>/result', methods=['GET'])
def get_results(office_id):
    """ get results.
    ---
    tags:
        - Results
    parameters:
      - in: path
        name: office_id
        required: true
        type: integer
    responses:
      '200':
        description: Results were returned
    """
if __name__ == "__main__":
    app.run()
