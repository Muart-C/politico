import json
from werkzeug.security import generate_password_hash
from api.database.database import DatabaseSetup
class Vote(DatabaseSetup):
    """votes model"""
    def __init__(self, office_id, user_id, candidate_id):
        super().__init__()
        self.office_id = office_id
        self.user_id = user_id
        self.candidate_id=candidate_id

    def vote_for_a_candidate(self):
        self.cursor.execute('''SELECT * FROM votes WHERE created_by='{}' AND candidate_id = '{}';'''.format(self.user_id, self.candidate_id))
        vote=self.cursor.fetchone()
        self.connection.commit()
        if vote is None:
            insert_vote = '''INSERT INTO votes(office_id, created_by, candidate_id)\
             VALUES ('{}','{}','{}')'''.format(\
                 self.office_id, self.user_id, self.candidate_id)
            self.cursor.execute(insert_vote)
            self.connection.commit()
            self.cursor.close()
            return self
        return True

    def check_if_has_voted(self, user_id, office_id):
        self.cursor.execute('''SELECT * FROM votes WHERE created_by='{}'\
             AND office_id='{}';'''.format(user_id, office_id))
        vote=self.cursor.fetchone()
        self.connection.commit()
        self.cursor.close()
        return json.dumps(vote, default=str)


    def get_results_of_a_particular_office(self):
        self.cursor.execute('''SELECT * FROM votes WHERE office_id='{}';'''.format(self.office_id))
        votes=self.cursor.fetchall()
        votes_list = []
        for vote in votes:
            vote = { "voter": vote[2],'office': vote[3], 'candidate': vote[4]}
            votes_list.append(vote)
        return votes_list
