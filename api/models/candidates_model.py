import json
from werkzeug.security import generate_password_hash
from api.database.database import DatabaseSetup
from api.models.offices_model import Office
class Candidate(DatabaseSetup):
    def __init__(self, office_id, party_id, candidate_id):
        super().__init__()
        self.office_id = office_id
        self.party_id = party_id
        self.candidate_id = candidate_id

    def create_a_candidate(self):
        insert_candidate = '''INSERT INTO candidates(office_id,\
                 party_id, candidate_id)VALUES ('{}','{}', '{}')\
                      RETURNING office_id, candidate_id, party_id'''\
                          .format(self.office_id,self.party_id, self.candidate_id)

        self.cursor.execute(insert_candidate)
        self.connection.commit()
        self.cursor.close()
        return self

    def get_candidate(self, candidate_id):
        self.cursor.execute('''SELECT * FROM candidates WHERE id='{}';'''.format(candidate_id))
        candidate=self.cursor.fetchone()
        self.connection.commit()
        self.cursor.close()
        return candidate

    def get_all_registered_candidates(self, office_id):
        self.cursor.execute('''SELECT concat_ws(' ', firstname, lastname) AS candidate,
         offices.name as office,parties.name as party, candidates.id as candidate_id, offices.id as office_id,
         users.passport_url
         FROM candidates
         INNER JOIN users ON users.id = candidates.candidate_id
         INNER JOIN parties ON parties.id = candidates.party_id
         INNER JOIN offices ON offices.id = candidates.office_id
         WHERE candidates.office_id = '{}';'''.format(office_id))
        candidates=self.cursor.fetchall()
        return candidates


