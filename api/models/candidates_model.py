"""#!api/models/candidates_model.py"""
from werkzeug.security import generate_password_hash
from api.database.database import DatabaseSetup
from api.models.offices_model import Office
class Candidate(DatabaseSetup):
    """candidates model"""
    def __init__(self, office_id, party_id, candidate_id):
        super().__init__()
        self.office_id = office_id
        self.party_id = party_id
        self.candidate_id = candidate_id

    def create_a_candidate(self):
        """check if an office exists first."""
        # office = Office(name=None,office_type=None).get_office(self.office_id)
        # print(office)
        """create a candidate."""
        insert_candidate = '''INSERT INTO candidates(office_id,\
                 party_id, candidate_id)VALUES ('{}','{}', '{}')\
                      RETURNING office_id, candidate_id, party_id'''\
                          .format(self.office_id,self.party_id, self.candidate_id)

        self.cursor.execute(insert_candidate)
        self.connection.commit()
        self.cursor.close()
        return self

    def get_candidate(self, candidate_id):
        """get a candidate whose id was passed."""
        self.cursor.execute('''SELECT * FROM candidates WHERE id='{}';'''.format(candidate_id))
        candidate=self.cursor.fetchone()
        if candidate is not None:
            return True
        else:
	        return False

    def check_if_candidate_exists_before_creating_one(self, candidate_id):
        """checks if a candidate exists before attempting to create one"""
        self.cursor.execute('''SELECT * FROM candidates WHERE candidate_id='{}';'''.format(self.candidate_id))
        candidate=self.cursor.fetchone()
        if candidate is None:
            return False
        return True


