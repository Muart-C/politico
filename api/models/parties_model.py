"""#!api/models/parties_model.py"""
from werkzeug.security import generate_password_hash
from api.database.database import DatabaseSetup
class Party(DatabaseSetup):
    """parties model"""
    def __init__(self, name, hq_address, logo_url):
        super().__init__()
        self.name = name
        self.hq_address = hq_address
        self.logo_url = logo_url

    def create_a_party(self):
        """create a party."""
        insert_party = '''INSERT INTO parties(name, hq_address, logo_url) VALUES ('{}','{}', '{}')'''.format(self.name, self.hq_address, 			self.logo_url)
        self.cursor.execute(insert_party)
        self.connection.commit()
        self.cursor.close()
        return self

    def get_party(self, party_id):
        """get a party whose id was passed."""
        self.cursor.execute('''SELECT * FROM parties WHERE id='{}';'''.format(party_id))
        party=self.cursor.fetchone()
        if party is None:
	        return False
        parties=[]
        parties.append(party)
        return parties

    def patch_party_name(self, party_id, party_name):
	    """updates the name of a party."""
	    self.cursor.execute('''SELECT * FROM parties WHERE id='{}';'''.format(party_id))
	    party=self.cursor.fetchone()
	    if party:
                self.cursor.execute('''UPDATE parties SET name='{}' WHERE id='{}';'''.format(self.name, party_id))
                self.connection.commit()
                return party

    def delete_party(self, party_id):
        if self.get_party(party_id) is not None:
	        self.cursor.execute('''DELETE * FROM parties WHERE id='{}' CASCADE'''.format(party_id))
	        self.connection.commit()
        return False

    def check_if_party_exist_before_creating_one(self):
        """checks if a party exists before attempting to create one"""
        self.cursor.execute('''SELECT * FROM parties WHERE name='{}';'''.format(self.name))
        party=self.cursor.fetchone()
        if party is None:
            return False
        return True




			