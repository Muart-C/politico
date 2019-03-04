import json
from werkzeug.security import generate_password_hash
from api.database.database import DatabaseSetup
class Party(DatabaseSetup):
    def __init__(self, name, hq_address, logo_url):
        super().__init__()
        self.name = name
        self.hq_address = hq_address
        self.logo_url = logo_url

    def create_a_party(self):
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
        self.cursor.execute('''SELECT * FROM parties;''')
        parties=self.cursor.fetchall()
        parties_list = []
        for party in parties:
            party = {'party_id': party[0],'name': party[1], 'hq_address': party[2], 'logo_url': party[3]}
            parties_list.append(party)
        return parties_list

    def get_party(self, party_id):
        self.cursor.execute('''SELECT * FROM parties WHERE id='{}';'''.format(party_id))
        party=self.cursor.fetchone()
        self.connection.commit()
        self.cursor.close()
        return json.dumps(party, default=str)

    def patch_party_name(self, party_id):
	    self.cursor.execute('''SELECT * FROM parties WHERE id='{}';'''.format(party_id))
	    party=self.cursor.fetchone()
	    if party:
                self.cursor.execute('''UPDATE parties SET name='{}' WHERE id='{}';'''.format(self.name, party_id))
                self.connection.commit()
                return {'name': party[1], 'hq_address': party[2], 'logo_url': party[3]}


    def delete_party(self, party_id):
        self.cursor.execute('''DELETE FROM parties WHERE id='{}';'''.format(party_id))
        self.connection.commit()
        self.cursor.close()

