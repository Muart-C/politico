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


    def get_results_of_a_particular_office(self, office_id):
        self.cursor.execute('''SELECT email as candidate\
             from users inner join votes on users.id = votes.candidate_id;'''.format(office_id))
        total_votes=self.cursor.fetchall()
        # self.connection.commit()
        # self.cursor.close()
        # return json.dumps(total_votes, default=str)

        results = []
        for votes in total_votes:
            votes = {'office': votes[3], 'candidate': votes[4]}
            results.append(votes)
        return results
