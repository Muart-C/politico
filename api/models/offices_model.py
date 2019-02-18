"""#!api/models/offices_model.py"""
from werkzeug.security import generate_password_hash
from api.database.database import DatabaseSetup
class Office(DatabaseSetup):
    """offices model"""
    def __init__(self, name, office_type):
        super().__init__()
        self.name = name
        self.office_type = office_type

    def create_office(self):
        """create an office."""
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
        """get results of a particular office."""
        self.cursor.execute('''SELECT * FROM offices WHERE id='{}';'''.format(office_id))
        office=self.cursor.fetchone()
        office = {'name': office[1], 'office_type': office[2]}
        return office
 
    def get_offices(self):
        """get all offices"""
        self.cursor.execute('''SELECT * FROM offices;''')
        offices=self.cursor.fetchall()
        offices_list = []
        for office in offices:
            office = {'name': office[1], 'office_type': office[2]}
            offices_list.append(office)
        return offices_list

