"""#!api/models/parties_model.py"""
from werkzeug.security import generate_password_hash
from api.database.database import DatabaseSetup
class Party(DatabaseSetup):
    """parties model"""
    def __init__(self, name, hq_address, logo_url):
        self.name = name
        self.hq_address = hq_address
        self.logo_url = logo_url

    def create_a_party(self):
        """create a party."""
        self.cursor.execute('''SELECT * FROM parties WHERE name='{}';'''.format(self.name))
        party=self.cursor.fetchone()
        if party is None:
            insert_party = '''INSERT INTO parties\
                (name, hq_address, logo_url) VALUES ('{}','{}', '{}')'''\
                    .format(self.name, self.hq_address, self.logo_url)
            self.cursor.execute(insert_party)
            self.connection.commit()
            self.cursor.close()
            return self
        else:
            return False

    def get_parties(self):
        """get all parties"""
        self.cursor.execute('''SELECT * FROM parties;''')
        parties=self.cursor.fetchall()
        parties_list = []
        for party in parties:
            party = {'name': party[1], 'hq_address': party[2], 'logo_url': party[3]}
            parties_list.append(party)
        return parties_list

    def get_party(self, party_id):
        """get a party whose id was passed."""
        self.cursor.execute('''SELECT * FROM parties WHERE id='{}';'''.format(party_id))
        party=self.cursor.fetchone()
        party = {'name': party[1], 'hq_address': party[2], 'logo_url': party[3]}
        return party

    def patch_party_name(self, party_id):
	    """updates the name of a party."""
	    self.cursor.execute('''SELECT * FROM parties WHERE id='{}';'''.format(party_id))
	    party=self.cursor.fetchone()
	    if party:
                self.cursor.execute('''UPDATE parties SET name='{}' WHERE id='{}';'''.format(self.name, party_id))
                self.connection.commit()
                return {'name': party[1], 'hq_address': party[2], 'logo_url': party[3]}

    def delete_party(self, party_id):
        if self.get_party(party_id) is not None:
	        self.cursor.execute('''DELETE FROM parties WHERE id='{}';'''.format(party_id))
	        self.connection.commit()
        return False

