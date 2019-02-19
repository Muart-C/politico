import json
from werkzeug.security import generate_password_hash
from api.database.database import DatabaseSetup

class Office(DatabaseSetup):
    def __init__(self, name, office_type):
        super().__init__()
        self.name = name
        self.office_type = office_type

    def create_office(self):
        self.cursor.execute('''SELECT * FROM offices WHERE name='{}';'''.format(self.name))
        office=self.cursor.fetchone()
        if office is None:
            insert_office = '''INSERT INTO offices(name, office_type) VALUES ('{}','{}')'''.format(self.name, self.office_type)
            self.cursor.execute(insert_office)
            self.connection.commit()
            self.cursor.close()
            return self
        else:
            return False

    def get_office(self, office_id):
        self.cursor.execute('''SELECT * FROM offices WHERE id='{}';'''.format(office_id))
        office=self.cursor.fetchone()
        self.connection.commit()
        self.cursor.close()
        return json.dumps(office, default=str)

    def get_offices(self):
        self.cursor.execute('''SELECT * FROM offices;''')
        offices=self.cursor.fetchall()
        offices_list = []
        for office in offices:
            office = {'name': office[1], 'office_type': office[2]}
            offices_list.append(office)
        return offices_list

