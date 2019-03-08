import json
from werkzeug.security import generate_password_hash
from psycopg2.extras import RealDictCursor
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
        return vote

    def get_results_of_a_particular_office(self, office_id):
        self.cursor.execute('''SELECT concat_ws(' ',users.firstname,users.lastname) AS candidate,
            offices.name as office,
            (SELECT COUNT(*)
              FROM  votes As v
              WHERE v.candidate_id = e.candidate_id
              GROUP BY v.candidate_id
            ) AS results
            FROM votes AS e
            INNER JOIN users on users.id = e.candidate_id
            INNER JOIN offices ON offices.id = e.office_id
            WHERE office_id = '{}'
            GROUP BY e.candidate_id,users.firstname,users.lastname,offices.name'''.format(office_id))
        total_votes=self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        return total_votes
